from books.models import Book

from correios_utils import (
    FormatoEncomenda,
    SimNao,
    Servico,
    realizar_cotacao,
)

from django.shortcuts import get_object_or_404


def frete(*args, **kwargs):
    zipCode = kwargs['user'].address.zip_code
    medidas = {
        'altura': 0,
        'largura': 0,
        'diametro': 0,
        'comprimento': 0,
        'peso': 0,
        'quantidade': 0,
        'preco_total': 0

    }

    for obj_book in kwargs['data']:
        if obj_book.get('books'):
            book = get_object_or_404(Book, id=obj_book.get('books'))
            if book.weigth > 0:
                medidas['peso'] += book.weigth * obj_book.get('ammount_items')

            if book.width > medidas['comprimento']:
                medidas['comprimento'] = book.width

            if book.length > 0:
                medidas['altura'] += book.length * \
                    obj_book.get('ammount_items')

            if book.width > medidas['largura']:
                medidas['largura'] = book.width

            if book.diameter > medidas['diametro']:
                medidas['diametro'] = book.diameter

        medidas['preco_total'] += book.price * obj_book.get('ammount_items')
        medidas['quantidade'] += obj_book.get('ammount_items')

    frete = realizar_cotacao(
        cep_origem="02912000",
        cep_destino=zipCode,
        codigos_servicos=[Servico.PAC, Servico.SEDEX, Servico.SEDEX_10],
        peso=medidas['peso'],
        comprimento=medidas['comprimento'],
        altura=medidas['altura'],
        largura=medidas['largura'],
        diametro=medidas['diametro'],
        formato_encomenda=FormatoEncomenda.CAIXA_PACOTE,
        valor_declarado=book.price,
        mao_propria=SimNao.NAO,
        aviso_recebimento=SimNao.NAO,
        codigo_empresa="08082650",
        senha_empresa="564321",
    )

    return frete, medidas
