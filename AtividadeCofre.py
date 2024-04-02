import paho.mqtt.client as mqtt
import random
import time

nomeEquipe = "equipe01"

#esse método é executado quando nos conectarmos ao servidor
def ao_conectar(client, userdata, flags, rc):
    print("Conectado no Servidor")

#esse método é chamado quando recebermos uma mensagem em um tópico
def ao_receber(client, userdata, msg):
    print(f"{msg.topic} --- {str(msg.payload)}")

def gerar_senha_aleatoria():
    return ''.join(random.sample('0123456789', k=4))

def teste_aleatorio():
    senha_testada = gerar_senha_aleatoria()
    return senha_testada

#tudo gira em torno do Cliente. Então primeiro criamos um objeto cliente,
#depois associamos as funções criadas ao on _connect e on_message e, por fim, nos conectamos ao servidor e ao tópico
cliente = mqtt.Client()

cliente.on_connect = ao_conectar
cliente.on_message = ao_receber
cliente.connect("broker.hivemq.com", 1883, 60)
cliente.subscribe(nomeEquipe + "/resp")

cliente.loop_start() #Esse comando cria uma thread, as linhas abaixo dessa são executadas
while True:
    cliente.publish("cofre", nomeEquipe + str(teste_aleatorio()))
    time.sleep(1)
cliente.loop_finish()









