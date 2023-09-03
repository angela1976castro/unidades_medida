def kilogramos_a_libras(kilogramos):
    return kilogramos * 2.20462

def libras_a_gramos(libras):
    return libras *453.592

if __name__=="__main__":
    kilogramos= int(input("Ingrese la cantidad de kilogramos: "))
    libras= kilogramos_a_libras(kilogramos)
    print(f"{kilogramos} kilogramos equivale a {libras:.2f} libras")