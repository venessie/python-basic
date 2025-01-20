class employee():
    def __init__(self):
       print("Employee created.")
    def __del__(self):
       print("2 minutes later...")
       print("Destructor called, employee deleted.")

obj = employee()
del obj

