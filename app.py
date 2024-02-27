from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melância', 5.0, 'grande')
prato_paozinho = Prato('Paozinho', 2.00, 'O melhor pão da cidade')
restaurante_praca = Restaurante.adicionar_item_cardapio(bebida_suco)
restaurante_praca = Restaurante.adicionar_item_cardapio(bebida_suco)


def main():
    print(bebida_suco)
    print(prato_paozinho)


if __name__ == '__main__':
    main()