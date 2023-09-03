def litros_a_galones(litros):
    return litros *0.264172

def galones_a_onzas_fluidas(galones):
    return galones *128

if __name__=="__main__":
    litros= 10
    galones= litros_a_galones(litros)
    print(f"{litros} litros equivale a {galones:.2f} galones ")