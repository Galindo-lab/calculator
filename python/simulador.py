
Resistividad = {
    "Plata":     1.59E-8,
    "Cobre":      1.7E-8,
    "Oro":       2.44E-8,
    "Aluminio":  2.82E-8,
    "Tungsteno":  5.6E-8,
    "Hierro":      10E-8,
    "Platino":     11E-8,
    "Plomo":       22E-8,
    "Nicromo":    1.5E-6,
    "Carbono":    3.5E-5,
    "Germanio":     0.46,
    "Silicio":     2.3E3,
}

coef_temp = {
     "Plata":      3.8E-3,
     "Cobre":      3.9E-3,
     "Oro":        3.4E-3,
     "Aluminio":   3.9E-3,
     "Tungsteno":  4.5E-3,
     "Hierro":     5.0E-3,
     "Platino":   3.92E-3,
     "Plomo":      3.9E-3,
     "Nicromo":    0.4E-3,
     "Carbono":   -0.5E-3,
     "Germanio":   -48E-3,
     "Silicio":    -75E-3,
}

Materiales = [
    "Plata",
    "Cobre",
    "Oro",
    "Aluminio",
    "Tungsteno",
    "Hierro",
    "Platino",
    "Plomo",
    "Nicromo",
    "Carbono",
    "Germanio",
    "Silicio",
]

res_id       = ""
resistividad = 0
longitud     = 0
area         = 0

res_total = 0 
res = 0
coe = 0
temp_fin = 0
temp_ini = 0
custom = 0


while(1):
    print("\n".join([
        "\n === Resistividad === ",
        "   1) temperatura",
        "   2) geometria",
        " --------------------",
        "   0) Salir\n"
    ]))

    op = int(input("Comando: "))

    if(op == 1):
        i = 0
        print("+----+------------+-----------+------------+")
        print("| id | Material   | Resistiv. | Coef. Tem. |")
        print("+----+------------+-----------+------------+")
        for key in Resistividad:
            print("| %2d | %10s | %.3e | %+.3e |" % (i,key, Resistividad[key], coef_temp[key] ) )
            i += 1
        print("+----+------------+-----------+------------+\n")

        res_id = int(input("   Material (id) : "))
        res = Resistividad[Materiales[res_id]]
        coe = coef_temp[Materiales[res_id]]
        temp_ini = float(input("Temp. inicial(k) : "))
        temp_fin = float(input("  Temp. final(k) : "))

        res_total = res * ( 1 + coe * (temp_ini - temp_fin) )

        print("----------------------------------")
        print("Resistencia(\u03A9): %.5e \n"%( res_total ))
        

        input("Pulsa cualquier tecla para continuar...")

    elif(op == 2):
        i = 0
        print("+----+------------+-----------+")
        print("| id | Material   | Valor     |")
        print("+----+------------+-----------+")
        for key in Resistividad:
            print("| %2d | %10s | %.3e |" % (i,key, Resistividad[key]) )
            i += 1
        print("+----+------------+-----------+\n")
        print("Escribe \"custom\" para añadir un material personalizado")

        res_id = input("Material (id) : ")

        if( res_id.lower() == "custom" ):
            resistividad = float(input("Valor de resistividad: "))
        else:
            resistividad = Resistividad[Materiales[ int(res_id) ]]

        longitud = float(input(" Longitud (m) : "))
        area = float(input("    Área (m²) : "))

        print("----------------------------------")
        print("Resistencia(\u03A9): ", ( resistividad * longitud / area ))
        input("Pulsa cualquier tecla para continuar...")

    elif(op == 0):
        break
    else:
        print("no existe esa opcion")
