import funciones
def main():
    cliente= {
	    "nombre":"Juan Perez",
	    "fonos":[98659865,63365412,8796542],
	    "activo":True,
        "email":"juan@gmail.com"
    }
    while True:
        print("\n===================================")
        print("1.- Mostrar información del cliente (Búsqueda)")
        print("2.- agregar nuevo fono de contacto (Insertar)")
        print("3.- Calcular simulación de dividendo (Cálculo)")
        print("4.- Desactivar y limpiar registros(Actualización/Eliminación)")
        print("5.-salir")
        opcion= input("seleccione opción (1-5): ").strip()
        if opcion == "1":
            funciones.mostrar_cabecera_credito()
            if "activo" in cliente:
                estado = "Vigente (activo)" if cliente["activo"] else "inactivo"
            else:
                estado = "Registro de estado eliminado"
            print(f"Estado del cliente: {cliente['activo']}")
            print(f"Nombre del Deudor: {cliente['nombre']}")
            print(f"Fonos: {cliente['fonos']}")
        elif opcion == "2":
            try:
                nuevo_fono = int(input("Ingrese el nuevo número telefónico: "))
                funciones.agregar_telefono(cliente, nuevo_fono)
            except ValueError:
                print("[ERROR] El fono debe ser un valor número entero")
        elif opcion == "3":
            try:
                monto = float(input("Monto del crédito hipotecario (en UF): "))
                tasa = float(input("Tasa de interés anual fija (ej: 3.8): "))
                anios = int(input("Plazo del crédito en años (ej: 20): "))
                cuota_mensual = funciones.calcular_dividendo(monto,tasa,anios)
                print(f"[INFO] Dividendo mensual estimado: {cuota_mensual:.2f} UF")
            except ValueError:
                print("[ERROR] Ingrese valores númericos válidos para la simulación")
        elif opcion == "4":
            if funciones.confirmar_desactivacion():
                cliente["activo"] = False
            else:
                print("El cliente ya se encuentra bloqueado")
if __name__ == "__main__":
    main()
