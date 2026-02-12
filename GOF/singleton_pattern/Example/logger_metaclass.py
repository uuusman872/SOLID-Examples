import logging
import threading


class SingletonMeta(type):
    _instance = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instance:
                cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]   # <-- return the instance, not dict


class Logger(metaclass=SingletonMeta):
    def __init__(self):
        self.__initialize_logger()

    def __initialize_logger(self):
        self._logger = logging.getLogger("my_logger")
        self._logger.setLevel(logging.DEBUG)

        # prevent duplicate handlers
        if not self._logger.handlers:
            file_handler = logging.FileHandler("my_log_file.log")
            file_handler.setLevel(logging.DEBUG)

            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)

            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )

            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            self._logger.addHandler(file_handler)
            self._logger.addHandler(console_handler)

    def getLogger(self):
        return self._logger


logger = Logger().getLogger()

logger.info("This is an info message")
logger.warning("This is a warning message")
