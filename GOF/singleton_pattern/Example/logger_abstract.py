import logging
import threading
from abc import ABC, ABCMeta, abstractmethod


# ---------- Singleton Metaclass ----------
class SingletonMeta(ABCMeta):   # inherit from ABCMeta so it supports abstract classes
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


# ---------- Abstract Logger ----------
class BaseLogger(ABC, metaclass=SingletonMeta):

    @abstractmethod
    def debug(self, message: str):
        pass

    @abstractmethod
    def info(self, message: str):
        pass

    @abstractmethod
    def warning(self, message: str):
        pass

    @abstractmethod
    def error(self, message: str):
        pass

    @abstractmethod
    def critical(self, message: str):
        pass


# ---------- Concrete Logger ----------
class Logger(BaseLogger):

    def __init__(self):
        self.logger = logging.getLogger("my_logger")
        self.logger.setLevel(logging.DEBUG)

        # prevent duplicate handlers
        if not self.logger.handlers:
            file_handler = logging.FileHandler("my_log_file.log")
            file_handler.setLevel(logging.DEBUG)

            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)

            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )

            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)

    def debug(self, message: str):
        self.logger.debug(message)

    def info(self, message: str):
        self.logger.info(message)

    def warning(self, message: str):
        self.logger.warning(message)

    def error(self, message: str):
        self.logger.error(message)

    def critical(self, message: str):
        self.logger.critical(message)


# ---------- Usage ----------
logger1 = Logger()

logger1.debug("hello world")
logger1.info("hello info")
logger1.warning("hello warning")
