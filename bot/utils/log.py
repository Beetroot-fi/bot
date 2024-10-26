import logging


def setup_logging(level: int) -> None:
    """Setup logging for bot"""

    logging.basicConfig(
        level=level,
        format="[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s",
        handlers=[logging.StreamHandler()],
    )
