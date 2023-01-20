import inspect
import logging


class BaseClass:
    def getlogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        filehandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)  # finlehandler  object
        logger.setLevel(logging.INFO)
        return logger