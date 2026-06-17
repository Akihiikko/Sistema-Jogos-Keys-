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

    opcao =  input("✿ Digite a opção desejada: ")
# ================ Controle da Lista ====================
    if opcao == "1":
        imprimir_dic(jogos, "૮ ◜ᵕ◝ ྀིა GameKeys Disponíveis")
        print()
    if opcao == "2":

        idKey = input("/ᐠっ˕ -マ Digite agora o ID do produto: ")
        if idKey in jogosand jogos [idKey]["qtd"] > 0:
            carrinho[idKey] = jogos[idKey]
            jogos[idKey]["qtd"] -= 1
            print("\n|💮| Item Adicionado ao Carrinho!!")

        else:
            print("\n|🚫| Produto Indisponivel! Digite um ID existente")

    elif opcao == "3":
        if carrinho:
            imprimir_dic(carrinho, "🛒 Seu carrinho!!")
        else:
            print("Carrinho vazio! Adicione itens para poder visualiza-lo"
            "e tente novamente")

    elif opcao == "4":
        total = sum(item["Preco"] for item in carrinho.values())
        print(f"🐉 Total da Compra: R$ {total}")
        print("Compra Finalizada")
        carrinho.clear()

    elif opcao == "0":
        print("Encerrando. Obrigada pela preferencia!✮⋆˙◟/づ~ 💌")