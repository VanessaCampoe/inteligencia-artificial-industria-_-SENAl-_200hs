def coletar_preferencias():
    print("Bem-vindo ao planejador de viagens!")
    destino = input("Qual destino você deseja visitar? ")
    tipo_viagem = input("Você prefere uma viagem cultural, de aventura ou relaxante? ")
    transporte = input("Qual meio de transporte você prefere (avião, carro, ônibus)? ")
    hospedagem = input("Prefere hotel, pousada ou Airbnb? ")
    dias = int(input("Quantos dias pretende viajar? "))

    return {
        "destino": destino,
        "tipo_viagem": tipo_viagem.lower(),
        "transporte": transporte.lower(),
        "hospedagem": hospedagem.lower(),
        "dias": dias
    }

def recomendar_atividades(preferencias):
    print(f"\nPlanejando sua viagem para {preferencias['destino']}...\n")

    if preferencias["tipo_viagem"] == "cultural":
        print("Sugestão: Visite museus, centros históricos e participe de tours guiados.")
    elif preferencias["tipo_viagem"] == "aventura":
        print("Sugestão: Explore trilhas, esportes radicais e parques naturais.")
    elif preferencias["tipo_viagem"] == "relaxante":
        print("Sugestão: Aproveite spas, praias e restaurantes tranquilos.")
    else:
        print("Tipo de viagem não reconhecido. Vamos sugerir um pouco de tudo!")

    if preferencias["dias"] < 3:
        print("Como a viagem é curta, foque nas atrações principais.")
    elif preferencias["dias"] <= 7:
        print("Você tem tempo para explorar com calma e aproveitar experiências locais.")
    else:
        print("Ótimo! Uma viagem longa permite conhecer bem o destino.")

def main():
    preferencias = coletar_preferencias()
    recomendar_atividades(preferencias)

if __name__ == "__main__":
    main()
