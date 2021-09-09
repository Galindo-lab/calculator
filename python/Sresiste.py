
_suffix_lookup = {
    'T': 1e12,
    'G': 1e9,
    'M': 1e6,
    'k': 1e3,
     '': 1e0,
    'm': 1e-3,
    'u': 1e-6,
    'n': 1e-9,
    'p': 1e-12,
    'f': 1e-15,
    'a': 1e-18,
}

def input_ing2():
    x = input().split();
    if len(x) > 0:
        if len(x) > 1 and x[1] in _suffix_lookup:
            return float(x[0]) * _suffix_lookup[x[1]]
        else:
            return float(x[0])
    else:
        return None

def input_ing(message=""):
    x = input(message).split();
    try:
        if len(x) > 0:
            if len(x) > 1 and x[1] in _suffix_lookup:
                return float(x[0]) * _suffix_lookup[x[1]]
            else:
                return float(x[0])
    except ValueError:
        print((
            "El valor ingresado\n"
            "no es valido, ej:\n"
            "       10 M \n"
            "debe llevar espacio"
        ))
        input()
    return None
        

def cls():
    print("\n\n\n\n\n\n")

def parallel_resistance(r1, r2):
    return 1/((r1+r2)/(r1*r2))

def serial_resistance(r1, r2):
    return r1 + r2
        
def run():
    total_resistance = 0        # omhs
    value = 1
    cls()
    while True:
        print("Resistencia inicial:")
        total_resistance = input_ing()
        if total_resistance != None and total_resistance != 0:
            break;

    
    while value != 0:
        
        while True:
            print("Total(ohms):\n%f\n"%(total_resistance))
            print("ingrese 0 para salir\n\n")
            value = input_ing("Resistencia: ")
            if value != None:
                break;

        while True and value != 0:
            print((
                "Tipo:\n"
                "  1) Serie\n"
                "  2) Paralelo\n"
                "  0) cancelar\n"
            ))
            vtype = input()
            if vtype == '1':
                total_resistance = serial_resistance(total_resistance,value)
                break;
            elif vtype == '2':
                total_resistance = parallel_resistance(total_resistance,value)
                break;
            else:
                print("Cancelado")
                break;

        cls()
        print("Total(ohms):\n%f"%(total_resistance))
    
                
run()
