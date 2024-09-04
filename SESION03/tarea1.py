class CuentaBancaria:
  def __init__(self, numeroCta, nombreCliente, fechaApertura, saldo=0):
        self.__numeroCta = numeroCta
        self.__nombreCliente = nombreCliente
        self.__fechaApertura = fechaApertura
        self.__saldo = saldo
 if self.__saldo < 100000:
            raise ValueError("El saldo inicial debe ser al menos 100,000 pesos.")
def get_numeroCta(self):
        return self.__numeroCta

    def get_nombreCliente(self):
        return self.__nombreCliente

    def get_fechaApertura(self):
        return self.__fechaApertura

    def get_saldo(self):
        return self.__saldo
def set_numeroCta(self, numeroCta):
        self.__numeroCta = numeroCta

    def set_nombreCliente(self, nombreCliente):
        self.__nombreCliente = nombreCliente

    def set_fechaApertura(self, fechaApertura):
        self.__fechaApertura = fechaApertura

    def set_saldo(self, saldo):
        if saldo < 0:
            raise ValueError("El saldo no puede ser negativo.")
        self.__saldo = saldo
def consignar(self, monto):
        if monto <= 0:
            raise ValueError("El monto de la consignación debe ser positivo.")
        self.__saldo += monto
        print(f"Consignación exitosa. Nuevo saldo: {self.__saldo}")

    def retirar(self, monto):
        if monto > self.__saldo:
            raise ValueError("Saldo insuficiente para realizar el retiro.")
        if monto <= 0:
            raise ValueError("El monto del retiro debe ser positivo.")
        self.__saldo -= monto
        print(f"Retiro exitoso. Nuevo saldo: {self.__saldo}")

def menu():
    cuentas = {}

    while True:
        print("\n--- Menú ---")
        print("1. Crear cuenta")
        print("2. Consignar")
        print("3. Retirar")
        print("4. Consultar saldo")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            numeroCta = input("Número de cuenta: ")
            nombreCliente = input("Nombre del cliente: ")
            fechaApertura = input("Fecha de apertura (dd/mm/yyyy): ")
            saldo = float(input("Saldo inicial: "))

            try:
                cuenta = CuentaBancaria(numeroCta, nombreCliente, fechaApertura, saldo)
                cuentas[numeroCta] = cuenta
                print("Cuenta creada exitosamente.")
            except ValueError as e:
                print(e)

        elif opcion == '2':
            numeroCta = input("Número de cuenta: ")
            monto = float(input("Monto a consignar: "))

            if numeroCta in cuentas:
                try:
                    cuentas[numeroCta].consignar(monto)
                except ValueError as e:
                    print(e)
            else:
                print("Número de cuenta no encontrado.")

        elif opcion == '3':
            numeroCta = input("Número de cuenta: ")
            monto = float(input("Monto a retirar: "))

            if numeroCta in cuentas:
                try:
                    cuentas[numeroCta].retirar(monto)
                except ValueError as e:
                    print(e)
            else:
                print("Número de cuenta no encontrado.")

        elif opcion == '4':
            numeroCta = input("Número de cuenta: ")

            if numeroCta in cuentas:
                saldo = cuentas[numeroCta].get_saldo()
                print(f"Saldo actual de la cuenta {numeroCta}: {saldo}")
            else:
                print("Número de cuenta no encontrado.")

        elif opcion == '5':
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    menu()

       
