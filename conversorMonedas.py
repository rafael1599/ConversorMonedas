global soles, pesosMex, pesosCol
soles = 3.95
pesosMex = 24.00
pesosCol = 3875.00


def cambiar(moneda, valorDolares):
    cantidadM = input(
        "======================================================================\nCuantos "
        + moneda
        + " quieres cambiar a dolares: "
    )
    cantidadM = float(cantidadM)
    cambio = cantidadM / valorDolares
    cambio = round(cambio, 2)
    cambio = str(cambio)
    print("==> Tu cambio es de $" + cambio + " dolares <==")
    otraMoneda = input(
        "======================================================================\nQuieres cambiar otra moneda?\n1. Si\n2. No\n "
    )
    if otraMoneda == "2":
        print("Esta bien, que tengas un buen dia!!")
        exit()
    else:
        print(
            "======================================================================\nPerfecto!!"
        )


for i in range(500):
    moneda = input(
        "Qué tipo de moneda quiere cambiar a dolares?: \n1. Soles\n2. Pesos mexicanos\n3. Pesos colombianos\n"
    )

    if moneda == "1":
        cambiar("soles", soles)

    elif moneda == "2":
        cambiar("pesos mexicanos", pesosMex)
    elif moneda == "3":
        cambiar("pesos colombianos", pesosCol)
    else:
        print("Opción incorrecta, vuelva a intentarlo")
