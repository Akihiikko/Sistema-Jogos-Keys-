print(" ｡ ˚ ︶︶ꔫ︶︶‌ ₊ ˚ ︶︶ꔫ︶︶‌ ｡˚")
print("     𝑮𝒂𝒎𝒆𝑲𝒆𝒚𝒔 𝑺𝒉𝒐𝒑 ₍^. .^₎⟆")
print("       𝑻𝒆𝒓𝒎𝒊𝒏𝒂𝒍 ᡣ • . • 𐭩 ♡")
print(" ｡ ˚ ︶︶ꔫ︶︶‌ ₊ ˚ ︶︶ꔫ︶︶‌ ｡˚")

print("  (1) Estoque Disponível \n  (2) Adicionar Item ao Carrinho \n  (3) Ver Carrinho \n  (4) Finalizar Compra \n  (0) Finalizar Programa ૮ ◞ ﻌ ◟ ა")
print("      ⊹₊˚‧︵‿₊୨ᰔ୧₊‿︵‧˚₊⊹\n")


print("          ｡ ˚ ︶︶ꔫ︶︶‌ ₊ ˚ ︶︶ꔫ︶︶‌ ｡˚")
print("  ID    ||      Produto         ||  Quantidade    || Valor")
print("          ｡ ˚ ︶︶ꔫ︶︶‌ ₊ ˚ ︶︶ꔫ︶︶‌ ｡˚")

estoque = {"ID", "Preço"}
print(estoque)

def imprimir_dic(dic, descricao):
    print(f"Estoque Disponível {descricao}")
    for k, v in dic.items():
        print(f"{k}:{v}")