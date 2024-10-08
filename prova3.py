numero_secreto = 7
tentativas = 0
tentativas_maximas = 3

print("✨ Olá, bem-vinda ao nosso jogo de adivinhação! ✨")
print("🌟 Você tem 3 tentativas para descobrir qual é o número secreto. Dica: é um número entre 1 e 10! 🌟")

while tentativas < tentativas_maximas:  
    palpite = int(input("💖 Digite seu palpite: "))
    tentativas += 1  # Aumenta o número de tentativas
    if palpite == numero_secreto:
        print(f"🎉 Parabéns! Você acertou o número! 🎉")
        break  # Sai do loop se acertar
    else:
        print(" Que pena! Você não acertou. Tente novamente!")

print("✨ Obrigada por jogar! Até a próxima! ✨")
