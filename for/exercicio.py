# Lista com as notas dos funcionários
notas = [1, 2, 3 ,4, 5, 6, 7, 8, 9, 10]

# Percorrendo a lista com o laço for
for i, nota in enumerate(notas, start=1):
    if nota >= 7:
        print(f"Funcionário {i}: Nota {nota} → Aprovado")
    else:
        print(f"Funcionário {i}: Nota {nota} → Em acompanhamento")