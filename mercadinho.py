produtos = ["Arroz", "Feijão", "Macarrão", "Óleo", "Sal", "Açúcar", "Café", "Leite", "Pão", "Manteiga"]
precos = [5.99, 7.49, 3.89, 8.99, 1.49, 4.59, 12.99, 4.19, 6.39, 9.89]
estoque = [10] * len(produtos)
produtoEscolhido = []
quantidadeEscolhida = []
contaProduto = []

for indice, produto in enumerate(produtos):
    preco = precos[indice]
    print(f"{indice}: {produto} - R${preco:.2f}")

total_compra = 0.0

while True:
    escolha = int(input("Digite o número do produto que você deseja, ou digite '10' para finalizar sua compra: "))
    if escolha == 10:
        break

    if 0 <= escolha < len(produtos):
        produto = produtos[escolha]
        preco = precos[escolha]
        estoque_produto = estoque[escolha]

        quantidade = int(input(f"Quanto do produto {produto} você deseja comprar? "))

        if quantidade <= estoque_produto:
            conta = preco * quantidade
            total_compra += conta

            produtoEscolhido.append(produto)
            quantidadeEscolhida.append(quantidade)
            contaProduto.append(conta)

            estoque[escolha] -= quantidade

            print(f"{quantidade} unidade(s) de {produto} adicionada(s) ao carrinho por R${conta:.2f}")
        else:
            print(f"Desculpe, temos apenas {estoque_produto} unidade(s) de {produto} em estoque. Por favor, escolha uma quantidade menor.")
    else:
        print("Escolha inválida, tente novamente.")

with open("nota_fiscal.txt", "w") as nota_fiscal:
    nota_fiscal.write("Nota Fiscal\n")
    nota_fiscal.write("=====================================\n")
    for i in range(len(produtoEscolhido)):
        nota_fiscal.write(f"Produto: {produtoEscolhido[i]}, Quantidade: {quantidadeEscolhida[i]}, Valor: R${contaProduto[i]:.2f}\n")
    nota_fiscal.write("=====================================\n")
    nota_fiscal.write(f"Valor total da compra: R${total_compra:.2f}\n")

print(f"\nNota fiscal gerada com sucesso! Valor total da compra: R${total_compra:.2f}")