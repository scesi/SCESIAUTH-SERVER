#!/usr/bin/python3.5
# coding: utf-8

from ConexionMQTT import ConnectionMQTT
import signal

def abrir(topic, value):
    print('el valor es '+ value)

def cerrar(topic, value):
    print('el topico es '+ topic)


if __name__ == '__main__':
    client = ConnectionMQTT.getInstance()
    client.addSubscribe('abrir', abrir )
    client.addSubscribe('cerrar', cerrar )
    # client.addPublished('cerrar', 'se cerro la puerta')
    signal.pause()