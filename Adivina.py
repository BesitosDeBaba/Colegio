import numpy as np

'''
Funcion que ejecuta el juego.
secuencia - arreglo o lista con una secuencia de números a adivinar
nivelDif - Número de intentos que se le permite al usuario
'''
def adivinaNumero(secuencia, nivelDif):
    #El numero
    eleccion = np.random.choice(secuencia)
    print(eleccion, '----------------')


    for i in range(nivelDif):
        print('Adivina que número estoy pensando....')
        respuesta = int(input())

        if respuesta < eleccion:
            print('El número es más grande')
        elif respuesta > eleccion:
            print('El número es más pequeño')
        elif respuesta == eleccion:
            print('GANASTE!')
            break
        else:
            print('No es un número')
    print('Los intentos se han acabado :c')
    print('El número que estaba pesnando era ', eleccion)

if __name__ == '__main__':
    print('JUEGO: ADIVINA EL NÚMERO *0*')
    print('Para poder jugar ingresa un secuencia de números, separados por comas.')
    print('Por ejemplo: 1, 2, 3, 4, 5')
    secuencia = input().split(sep = ',')
    secuencia = [int(e) for e in secuencia]
    
    print('Ahora ingresa el nivel de dificultad, es decir, el número \n de oportunidades a adivinar')
    nivelDif = int(input())

    adivinaNumero(secuencia, nivelDif)
