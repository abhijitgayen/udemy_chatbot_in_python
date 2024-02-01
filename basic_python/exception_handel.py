
try:
    # Code that may raise an exception
    result = 10 / 0
except ZeroDivisionError as e:
    result = 10/1
    # Handle specific exception
    print(f"Caught an exception: {e}")
except ValueError as e:
    result = 10/10
    # Handle another specific exception
    print(f"Caught another exception: {e}")
except Exception as e:
    result = 10
    # Handle any other exception not caught by previous blocks
    print(f"Caught a generic exception: {e}")
else:
    # Code to be executed if no exception occurred
    print("No exception occurred.")
finally:
    # Code that will be executed no matter what, whether an exception occurred or not
    print("This block always executes.")
