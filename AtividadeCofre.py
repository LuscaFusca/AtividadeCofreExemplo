import paho.mqtt.client as mqtt
import webbrowser
import os
from playsound import playsound

#esse método é executado quando nos conectarmos ao servidor
def ao_conectar(client, userdata, flags, rc):
    #print("Nos conectamos com o seguinte código de resultado {}".format(str(rc)))
    print(f"Nos conectamos com o seguinte código de resultado {str(rc)} \n")

#esse método é chamado quando recebermos uma mensagem em um tópico
def ao_receber(client, userdata, msg):
    print(f"{msg.topic} --- {str(msg.payload)} ")
    if "DESLIGAR" in str(msg.payload).upper():
        print("DESLIGANDO O SISTEMA")
        os.system("shutdown -s")
    elif "FIAP" in str(msg.payload).upper():
        webbrowser.open("https://www.fiap.com.br")
    elif "USUARIO" in str(msg.payload).upper():
        client.publish("aula3b", os.getlogin())
    elif "ALARME" in str(msg.payload).upper():
        playsound("c:\\alarme\\teste.mp3")

#tudo gira em torno do Cliente. Então primeiro criamos um objeto cliente,
#depois associamos as funções criadas ao on _connect e on_message e, por fim, nos conectamos ao servidor e ao tópico
cliente = mqtt.Client()

cliente.on_connect = ao_conectar
cliente.on_message = ao_receber
cliente.connect("broker.hivemq.com", 1883, 60)
cliente.subscribe("equipe01/resp")
cliente.subscribe("equipe02/resp")
cliente.subscribe("equipe03/resp")
cliente.subscribe("equipe04/resp")
cliente.subscribe("equipe05/resp")
cliente.subscribe("equipe06/resp")
cliente.subscribe("equipe07/resp")
#cliente.subscribe("cofre")
#cliente.loop_forever() #Esse comando cria uma chamada bloqueadora para o cliente. Nenhuma linha abaixo dela é executada

cliente.loop_start() #Esse comando cria uma thread, as linhas abaixo dessa são executadas
while True:
    cliente.publish("cofre", "equipe01" + input("Envie uma mensagem: "))

cliente.loop_finish()
