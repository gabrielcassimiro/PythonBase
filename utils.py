class Decorators:
    # Creating a decorator
    @staticmethod
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("before")
            func(*args, **kwargs)
            print("after")

        return wrapper

    # Using decorator
    @decorator
    @staticmethod
    def hello():
        print("Hello")