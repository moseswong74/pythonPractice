"""

 Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it.
 In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.
 https://www.geeksforgeeks.org/decorators-in-python/

"""

# defining a decorator
def hello_decorator(func):
    # inner1 is a Wrapper function in
    # which the argument is called

    # https://www.geeksforgeeks.org/decorators-in-python/

    # inner function can access the outer local
    # functions like in this case "func"
    def inner1():
        print("Hello, this is before function execution")

        # calling the actual function now
        # inside the wrapper function.
        func()

        print("This is after function execution")

    return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
    print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behavior
function_to_be_used = hello_decorator(function_to_be_used)

# calling the function
function_to_be_used()