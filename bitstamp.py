import json
import ssl

import websocket


def comprar():
    print("Bitcoin comprado")


def vender():
    print("Bitcoin vendida")



def ao_abrir(ws):
    print("Abriu a conxão")

    json_subscribe = """ 
{
    "event": "bts:subscribe",
    "data": {
        "channel": "live_trades_btcusd"
    }
}
"""

    ws.send(json_subscribe)

def ao_fechar(ws):
    print("Fechou a conexão")


def ao_receber_mensagem(ws, mensagem):
    mensagem = json.loads(mensagem)
    price = mensagem['data']['price']
    print(price)

    if price > 31000:
        vender()
    elif price < 30000:
        comprar()
    else:
        print("Aguardando")

def erro(ws, erro):
    print("Erro")
    print(erro)


if __name__ == "__main__":
    ws = websocket.WebSocketApp("wss://ws.bitstamp.net.",
                                on_open=ao_abrir,
                                on_close=ao_fechar,
                                on_message=ao_receber_mensagem,
                                on_error=erro)

    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})