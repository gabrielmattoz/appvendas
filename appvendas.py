# Mensagem de boas-vindas com nome e sobrenome
print("Bem-vindo! Desenvolvido por Gabriel Matos Pinho")

# Entrada do usuário: valor do pedido e quantidade de parcelas
valorDoPedido = float(input("Digite o valor do pedido: "))
quantidadeParcelas = int(input("Digite a quantidade de parcelas: "))

# Definindo o valor do juros de acordo com a quantidade de parcelas
if quantidadeParcelas < 4:
    juros = 0 / 100  # Juros de 0%
elif quantidadeParcelas >= 4 and quantidadeParcelas < 6:
    juros = 4 / 100  # Juros de 4%
elif quantidadeParcelas >= 6 and quantidadeParcelas < 9:
    juros = 8 / 100  # Juros de 8%
elif quantidadeParcelas >= 9 and quantidadeParcelas < 13:
    juros = 16 / 100  # Juros de 16%
else:
    juros = 32 / 100  # Juros de 32%

# Cálculo do valor da parcela com juros
valorDaParcela = (valorDoPedido * (1 + juros)) / quantidadeParcelas

# Cálculo do valor total parcelado
valorTotalParcelado = valorDaParcela * quantidadeParcelas

# Exibição dos resultados
print(f"Valor da parcela: R$ {valorDaParcela:.2f}")
print(f"Valor total parcelado: R$ {valorTotalParcelado:.2f}")