import logging


def configure_logging(level=logging.WARNING):
    """configure logging module"""
    logging.basicConfig(
        level=level,
        format="%(asctime)s: %(levelname)7s: [%(name)s]: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
