def mostrar_cabecera_credito():
    """
    Impresión de resultados
    """
    print("\n---------------------------------------")
    print(" DETALLE DE CLIENTE - CRÉDITO HIPOTECARIO")
    print("-"*40)
def agregar_telefono(diccionario_cliente,telefono_nuevo):
    diccionario_cliente["fonos"].append(telefono_nuevo)
    print(f"[ÉXITO] Fono {telefono_nuevo} agregado correctamente")
def calcular_dividendo(monto_uf,tasa_anual,plazo_anios):
    i = (tasa_anual / 100)/12
    n = plazo_anios * 12
    if i == 0:
        return monto_uf / n
    return monto_uf * (i *(1 + i)**n)/ ((1*i)**n-1)
	 
def confirmar_desactivacion():
    print("¿Está seguro de que desea desactivar este cliente?")
    respuesta = input("Escriba si para confirmar proceso: ").lower()
    if respuesta == "si" or respuesta == "sí":
        return True
    return False