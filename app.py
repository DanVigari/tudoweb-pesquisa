
# --------------------------------------------------------------------
# Configuração da pesquisa
# --------------------------------------------------------------------
# Alterer o valor para quantidade de entrevistados que deseja realizar a pesquisa.

total_entrevistados = 10

# --------------------------------------------------------------------
# Contadores da pesquisa
# --------------------------------------------------------------------
total_excelente = 0
total_bom = 0
total_ruim = 0

# --------------------------------------------------------------------
# Estrutura de repetição "FOR" porque sabemos exatamente quantas vezes o
# número de entrevistados deve se repetir.
# --------------------------------------------------------------------
for entrevistado in range(1, total_entrevistados + 1):
    print(f"\n--- Entrevistado {entrevistado} de {total_entrevistados} ---")

    nome = input("Digite o nome do entrevistado: ")

    # ----------------------------------------------------------------
    # Estrutura de repetição "WHILE" para enquanto o que for digitado não for
    # um número, o programa avisa e pede a idade novamente. Assim, o
    # int(idade_texto) só é chamado depois de garantir que o valor é numérico.
    # ----------------------------------------------------------------
    idade_texto = input("Digite a idade do entrevistado: ")
    while not idade_texto.isdigit():
        print("Idade inválida! Digite apenas números.")
        idade_texto = input("Digite a idade do entrevistado: ")
    idade = int(idade_texto)

    # ----------------------------------------------------------------
    # Estrutura de repetição "WHILE" para enquanto o que for digitado não for
    # um número válido entre 1 e 3.
    # opiniao_texto.isdigit() garante que é número (evita erro com
    # letras) e a comparação garante que é 1, 2 ou 3.
    # ----------------------------------------------------------------
    opiniao_texto = input(
        "Como foi o atendimento?\n"
        "1 - EXCELENTE\n"
        "2 - BOM\n"
        "3 - RUIM\n"
        "Digite sua opção: "
    )
    while not opiniao_texto.isdigit() or int(opiniao_texto) not in (1, 2, 3):
        print("Opção inválida! Digite apenas 1, 2 ou 3.")
        opiniao_texto = input(
            "Como foi o atendimento?\n"
            "1 - EXCELENTE\n"
            "2 - BOM\n"
            "3 - RUIM\n"
            "Digite sua opção: "
        )
    opiniao = int(opiniao_texto)

    # ----------------------------------------------------------------
    # Estrutura de decisão para verificar a opinião do entrevistado
    # ----------------------------------------------------------------
    if opiniao == 1:
        print(f"{nome} ({idade} anos) avaliou o atendimento como EXCELENTE.")
        total_excelente += 1
    elif opiniao == 2:
        print(f"{nome} ({idade} anos) avaliou o atendimento como BOM.")
        total_bom += 1
    else:
        print(f"{nome} ({idade} anos) avaliou o atendimento como RUIM.")
        total_ruim += 1

# --------------------------------------------------------------------
# Resultado final da pesquisa
# --------------------------------------------------------------------
print("\n===== RESULTADO DA PESQUISA DE SATISFAÇÃO =====")
print(f"Total de entrevistados: {total_entrevistados}")
print(f"Quantidade de respostas EXCELENTE: {total_excelente}")
print(f"Quantidade de respostas RUIM: {total_ruim}")