nome = input("Digite o nome do herói: ")
xp = 0

while input("Deseja enfrentar um monstro (s/n): ") == "s":
    nivel_do_monstro = int(input("Qual o nível do monstro? "))
    nivel_de_dificuldade = int(input("Qual o nível de dificuldade? "))

    xp += nivel_do_monstro * nivel_do_monstro * 100

    print("XP:", xp)
    print()

if xp < 1000:
    nivel = "Ferro"
elif xp < 2000:
    nivel = "Bronze"
elif xp < 5000:
    nivel = "Prata"
elif xp < 7000:
    nivel = "Ouro"
elif xp < 8000:
    nivel = "Platina"
elif xp < 9000:
    nivel = "Ascendente"
elif xp < 10000:
    nivel = "Imortal"
else:
    nivel = "Radiante"

print(f"O Herói de nome **{nome}** está no nível de **{nivel}**")
