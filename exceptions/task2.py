try:
    var = 1/0
except ValueError as err:
    print(f"Value error {err}")
except ZeroDivisionError as err_:
    print(f"Division by zero {err_}")
except Exception:
    print("Unexpected error")
else:
    print(var, "hello")
finally:
    var = 1