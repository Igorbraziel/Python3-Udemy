perguntas = [
    {
        "Pergunta": "Quanto é 2 + 2?",
        "Opção": [1, 2, 3, 4, 5],
        "Resposta": 4
    },

    {
        "Pergunta": "Quanto é 5 * 5?",
        "Opção": [55, 5, 10, 25, 20],
        "Resposta": 25
    },

    {
        "Pergunta": "Quanto é 10 / 2?",
        "Opção": [2, 1, 5, 10, 15],
        "Resposta": 5
        }
]

for jogo in perguntas:
    while True:
        print(jogo["Pergunta"])
        print(f"Opções: {jogo['Opção']}")
        resp = int(input("Resposta: "))
        if resp == jogo["Resposta"]:
            break
        else:
            jogo["Opção"].pop(jogo["Opção"].index(resp))
            print("Você errou, tente novamente")