class Operation():
    def __init__(self, nombre1=1, nombre2=2):
        self.nombre1= nombre1
        self.nombre2= nombre2


an_operation = Operation()


an_operation.nombre1=1
an_operation.nombre2=3

print(f"Le nombre1 est {an_operation.nombre1}")
print(f"Le nombre2 est {an_operation.nombre2}")