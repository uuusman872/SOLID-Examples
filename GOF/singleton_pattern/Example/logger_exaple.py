import logging
import threading



class SingletonLogger:
    
    _instance = None
    _lock = threading.Lock()


    @classmethod
    def get_instance(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = cls()
                cls._instance._initialize_logger()
            return cls._instance

    def _initialize_logger(self):
        
        self.logger = logging.getLogger("my_logger")
        self.logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler("my_log_file.log")
        file_handler.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        formatter = logging.Formatter("%(asctime)s - %(name)s  - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)



logger = SingletonLogger.get_instance().logger

logger.info("This is an info message")
logger.warning("This is an warning message")
