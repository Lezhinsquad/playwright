##
 # singleton_meta.py
 ##
from threading import Lock


class SingletonMeta(type):
    """
    A thread-safe implementation of Singleton using metaclasses.
    """

    _instances = {}
    _lock = Lock()  # Thread-safe

    def __call__(cls, *args, **kwargs):
        # Ensure thread-safe access
        with cls._lock:
            if cls not in cls._instances:
                # If an instance does not exist, create one and store it.
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]
