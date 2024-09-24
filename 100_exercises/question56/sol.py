def error_test():
    return 5/0


try:
    error_test()
except ZeroDivisionError:
    print("You can't division by zero!")
except Exception as e:
    print(f"Nuknown error: {e}")
finally:
    print("This is the finally block.")
