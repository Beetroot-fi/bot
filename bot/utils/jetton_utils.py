from pytoniq import LiteBalancer, HighloadWallet, Cell, Address, begin_cell

from core.config import settings

from redis.asyncio import Redis

MAX_WALLETS_PER_TR = 200


def get_transfer_body(
    response_address: Address,
    destination_address: Address,
    amount: int,
    is_usdt: bool = False,
    query_id: int = 0,
) -> Cell:
    """Return jetton transfer body without forward payload"""

    return (
        begin_cell()
        .store_uint(0xF8A7EA5, 32)
        .store_uint(query_id, 64)
        .store_coins(int(amount * 1e6) if is_usdt else int(amount * 1e9))
        .store_address(destination_address)
        .store_address(response_address)
        .store_bit(0)
        .store_coins(1)
        .store_bit(0)
        .end_cell()
    )


async def transfer_jettons(redis: Redis):
    async with LiteBalancer.from_testnet_config(trust_level=2) as provider:
        highload_wallet = await HighloadWallet.from_mnemonic(
            provider=provider,
            mnemonics=settings.mnemonics,
        )

        jetton_wallet = (
            await provider.run_get_method(
                address="kQBxPxYRD9IOrnIEQysG7D9enWnxg8AGx-wUdcA55mxaKdTK",
                method="get_wallet_address",
                stack=[
                    begin_cell()
                    .store_address(highload_wallet.address)
                    .end_cell()
                    .begin_parse()
                ],
            )
        )[0].load_address()

        destinations = await redis.smembers(name="addresses")
        if len(destinations) > MAX_WALLETS_PER_TR:
            for destination in list(destinations)[:MAX_WALLETS_PER_TR]:
                await redis.srem("addresses", destination)
            destinations = list(destinations)[:MAX_WALLETS_PER_TR]
        elif len(destinations) == 0:
            return
        else:
            for destination in destinations:
                await redis.srem("addresses", destination)

        bodies = []
        for destination in destinations:
            body = get_transfer_body(
                response_address=highload_wallet.address,
                destination_address=Address(destination),
                amount=1000,  # 1000 USDT
                is_usdt=True,
            )
            bodies.append(body)

        await highload_wallet.transfer(
            destinations=[jetton_wallet] * len(bodies),
            amounts=[int(0.05 * 1e9)] * len(bodies),
            bodies=bodies,
        )
