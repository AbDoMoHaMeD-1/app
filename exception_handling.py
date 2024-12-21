try:
    x = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print("Error:", e)
else:
    print("Division was successful!")
finally:
    print("This will always execute.")
