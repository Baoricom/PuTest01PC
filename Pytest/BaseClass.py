import logging


class BaseClass:
    def test_logging(self):
        logger = logging.getLogger(__name__)

        filehandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)  # finlehandler  object
        logger.setLevel(logging.INFO)
        return logger