#!/usr/bin/python3

# predecir como un profesor aplicará las calificaciones. 


import random
import time


dataset = [] # aquí van los valores que no deben ser incluídos como parte del análisis.



global nota1
global nota2 

def first_test():

    
    global peso1

    nota1 = 7
    peso1 = random.uniform(0.1,0.9)

    return (nota1 * peso1)

def second_test():

    
    global peso2

    nota2 = 7
    peso2 = random.uniform(0.1,0.9)

    return (nota2 * peso2)

def final_test():
    
    nota_final  = float((first_test() + second_test())/(peso1 + peso2))

    return nota_final






counter = 0
if __name__ == '__main__':
    print('[*] Starting the training...')


    while True:
        final_test()
        #print("la calificación final: ",nota_final)
        #print("El peso de la nota 1: ",peso1, " el peso de la nota 2:", peso2 )
        time.sleep(1)

        """
        nota_final = (first_test() + second_test())
        print(nota_final)
        break
        """
        if (final_test() > 7.0):
            #print("la calificación final: ",nota_final)
            #print("El peso de la nota 1: ",peso1, " el peso de la nota 2:", peso2 )
            break
        elif(final_test() <= 7.0):
            

            
            #nota1 = random.randint(7,10)
            #nota2 = random.randint(7,10)
            counter += 1
        
    print("la calificación final: ",final_test())
    print("El peso de la nota 1: ",peso1, " el peso de la nota 2:", peso2 )
    print("Las veces que se realizó un recorrido son: ", counter)