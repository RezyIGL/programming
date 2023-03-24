try:
    func()
except (ValueError, TypeError, SystemError) as e:
    print(type(e).__name__)
else:
    print("No Exceptions")