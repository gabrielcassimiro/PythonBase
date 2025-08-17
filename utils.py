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

class Iterators:

    @staticmethod
    def interator_example():
        iterator_list = [1, 2, 3, 4, 5]
        it = iter(iterator_list)
        for i in iterator_list:
            print(next(it))
    pass

class Yields:

    #Explanation
    #* When the function reaches the keyword `yield`, it returns the provided value directly to the caller.
    #* The function’s execution is automatically paused, but its internal state (such as local variables) is preserved.
    #* When the generator is asked to produce the next value (usually with `next()`), the function resumes execution from the exact point where it was paused.
    @staticmethod
    def yield_example(maximo):
        n = 1
        while n <= maximo:
            yield n
            n += 1
    pass