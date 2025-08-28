import random 

def jokenpo():
    p = input("Insira pedra, papel ou tesoura: ").lower()
    b = ["papel", "pedra", "tesoura"]

    b_b = random.choice(b).lower()

    print(f"Jogador: {p}")
    print(f"Bot: {b_b}")

    if p == "tesoura" and b_b == "papel":
        print("O jogador venceu!")

    elif p == "pedra" and b_b == "tesoura":
        print("O jogador venceu!")

    elif p == "papel" and b_b == "pedra":
        print("O jogador venceu!")

    elif b_b == "tesoura" and p == "papel":
        print("O Bot venceu!")

    elif b_b == "pedra" and p == "tesoura":
        print("O Bot venceu!")

    elif p == "papel" and p == "pedra":
        print("O Bot venceu!") 
    
    elif p == b_b:
        print("Empate!")
    else:
        print("Bot venceu!")

    for i in b_b:
         
        retornar = input("Deseja reiniciar o jogo (s/n): ").lower()

        if (retornar == "s"):
            return jokenpo()
        else:
            break 

jokenpo()
        