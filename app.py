#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

import random

def obtener_opcion_usuario():
    while True:
        print("Elige una opción: ")
        print("1 - Piedra")
        print("2 - Papel")
        print("3 - Tijera")
        opcion = input("Ingresa 1, 2 o 3: ")
        
        if opcion in ['1', '2', '3']:
            return int(opcion)
        else:
            print("Opción inválida. Ingresa 1, 2 o 3.")

def traducir_opcion(numero):
    if numero == 1:
        return "Piedra"
    elif numero == 2:
        return "Papel"
    elif numero == 3:
        return "Tijera"

def piedra_papel_tijera():
    print("¡Bienvenido a Piedra, Papel o Tijera!")
    while True:
        usuario = obtener_opcion_usuario()
        computadora = random.randint(1, 3)
        
        print(f"Tú elegiste {traducir_opcion(usuario)}. La computadora eligió {traducir_opcion(computadora)}.")

        if usuario == computadora:
            print("¡Es un empate!")
        elif (usuario == 1 and computadora == 3) or (usuario == 2 and computadora == 1) or (usuario == 3 and computadora == 2):
            print("¡Ganaste!")
        else:
            print("¡La computadora gana!")

        jugar_nuevamente = input("¿Quieres jugar de nuevo? (s/n): ")
        if jugar_nuevamente.lower() != 's':
            break

piedra_papel_tijera()

