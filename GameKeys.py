# =========== Produtos ====================
jogos = {
    "001": {"nome": "಄ God Of War: Laufey", "qtd": 5, "preco": 240},
    "002": {"nome": "಄ GTA V", "qtd": 23, "preco": 80},
    "003": {"nome": "಄ Elden Ring - Deluxe Version", "qtd": 10, "preco": 120}
}
# =========== Biblioteca ====================
carrinho = {}

def imprimir_dic(dic, descricao):
    print(f"\n{descricao}")
    for k, v in dic.items():
        print(f"ID: {k} | Nome: {v['nome']} | Quantidade: {v['qtd']} | Preço: R${v['preco']}")

# ================== Menu em Loop =======================
while True:
    print(" ｡ ˚ ︶︶ꔫ︶︶‌ ₊ ˚ ︶︶ꔫ︶︶‌ ｡˚")
    print("     𝑮𝒂𝒎𝒆𝑲𝒆𝒚𝒔 𝑺𝒉𝒐𝒑 ₍^. .^₎⟆")
    print("       𝑻𝒆𝒓𝒎𝒊𝒏𝒂𝒍 ᡣ • . • 𐭩 ♡")
    print(" ｡ ˚ ︶︶ꔫ︶︶‌ ₊ ˚ ︶︶ꔫ︶︶‌ ｡˚")
    print("""  
    (1) Estoque Disponível  
    (2) Adicionar Item ao Carrinho 
    (3) Ver Carrinho  
    (4) Finalizar Compra
    (0) Finalizar Programa ૮ ◞ ﻌ ◟ ა
    """)
    print("      ⊹₊˚‧︵‿₊୨ᰔ୧₊‿︵‧˚₊⊹\n")

    opcao = input("✿ Digite a opção desejada: ")

    # ================ Controle da Lista ====================
    if opcao == "1":
        imprimir_dic(jogos, "૮ ◜ᵕ◝ ྀིა GameKeys Disponíveis")
        print()

    elif opcao == "2":
        idKey = input("/ᐠっ˕ -マ Digite agora o ID do produto: ")
        if idKey in jogos and jogos[idKey]["qtd"] > 0:
            if idKey in carrinho:
                carrinho[idKey]["qtd"] += 1
            else:
                carrinho[idKey] = {"nome": jogos[idKey]["nome"], "qtd": 1, "preco": jogos[idKey]["preco"]}
            jogos[idKey]["qtd"] -= 1
            print("\n|💮| Item Adicionado ao Carrinho!!")
        else:
            print("\n|🚫| Produto Indisponível! Digite um ID existente")

    elif opcao == "3":
        if carrinho:
            imprimir_dic(carrinho, "🛒 Seu carrinho!!")
        else:
            print("Carrinho vazio! Adicione itens para poder visualizá-lo e tente novamente")

    elif opcao == "4":
        if not carrinho:
            print("\n|🚫| Carrinho vazio. Não é possível finalizar.\n")
            continue

        subtotal = sum(item["preco"] * item["qtd"] for item in carrinho.values())
        print(f"\n🌸 Subtotal da Compra: R$ {subtotal:.2f}")

        cupom = input("✿ Digite um cupom de desconto (ou Enter para prosseguir): ").strip().upper()
        desconto = 0

        if cupom == "DEV10":
            desconto = subtotal * 0.10
            print("💎 Cupom DEV10 aplicado! 10% OFF ⋆˚࿔𓏲𝄢")
        elif cupom == "DEV20":
            if subtotal > 500:
                desconto = subtotal * 0.20
                print("💎 Cupom DEV20 aplicado! 20% OFF ⋆˚࿔𓏲𝄢")
            else:
                print("🚫 Cupom DEV20 válido apenas para compras acima de R$ 500.00.")
        elif cupom != "":
            print("🚫 Cupom inválido. Prosseguindo sem desconto.")

        total = subtotal - desconto
        print("\n｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
        print("      ✦ Resumo do Pedido ✦")
        print(f"Subtotal: R$ {subtotal:.2f}")
        print(f"Desconto: R$ {desconto:.2f}")
        print(f"Total a Pagar: R$ {total:.2f}")
        print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆\n")

        confirmacao = input("✿ Confirmar pagamento (S/N)? ").strip().upper()
        if confirmacao == "S":
            print("\n✅ Pagamento confirmado! Obrigado pela compra.\n")
            carrinho.clear()
        else:
            print("\n❌ Compra cancelada. Devolvendo itens ao estoque...\n")
            for item_id, item in carrinho.items():
                jogos[item_id]["qtd"] += item["qtd"]
            carrinho.clear()

    elif opcao == "0":
        print("Encerrando. Obrigada pela preferência!✮⋆˙◟/づ~ 💌")
        break

    else:
        print("❌ Opção inválida. Tente novamente.\n")