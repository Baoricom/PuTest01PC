import logging


def test_logging():
    logger = logging.getLogger(__name__)

    filehandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    filehandler.setFormatter(formatter)

    logger.addHandler(filehandler)  # finlehandler  object
    logger.setLevel(logging.DEBUG)
    logger.debug("A debug statement is executed")
    logger.info("Information messages")
    logger.warning("Something in the warning mode")
    logger.error("A major error has happened")
    logger.critical("Critical issue")
