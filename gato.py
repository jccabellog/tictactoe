import time
import sys 
import random
import os 

tablero = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

print(tablero)

 
tablero_play = []

for play in tablero:
    tablero_play.append(play)

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
def print_tab_inicial(tab):
    clear()
    print("\n Posiciones a escoger : \n")
    print(tab['7']+"7" + '|' + tab['8']+"8" + '|' + tab['9']+"9")
    print('--+--+--')
    print(tab['4']+"4" + '|' + tab['5']+"5" + '|' + tab['6']+"6")
    print('--+--+--')
    print(tab['1']+"1" + '|' + tab['2']+"2" + '|' + tab['3']+"3")
 
def printTab(tab):
    print(tab['7'] + '|' + tab['8'] + '|' + tab['9'])
    print('-+-+-')
    print(tab['4'] + '|' + tab['5'] + '|' + tab['6'])
    print('-+-+-')
    print(tab['1'] + '|' + tab['2'] + '|' + tab['3'])

def juego():
    for i in range(101):
         time.sleep(0.04)
         sys.stdout.write("\r%d%% Cargando Juego, favor espere " % i)
         sys.stdout.flush()
    print_tab_inicial(tablero)    
    modo = int(input(print("\n Escoja modo de juego : \n 1: Jugador vs CPU \n 2: CPU vs CPU \n")))
    if modo == 1:     
        res= input("\n Escoja su ficha X/O :")
        if res.upper() == "X":            
            jug1 = 'X'
            maq =  'O'
        else:
            jug1 = 'O'
            maq =  'X'
        
        turno= int(input("orden de inicio 1/2 :"))

        cont = 0
        clear()
        for i in range(30):
            printTab(tablero)               
            if turno == 1:
                print("Es tu turno," + jug1 + "...")
                movimiento = input() 
                if tablero[movimiento] == ' ':
                    tablero[movimiento] = jug1
                    cont = cont + 1
                    turno = 2
                    clear()
                else:              
                    print("El lugar está ocupado")
                    continue
            elif turno == 2:
                for i in range(101):                
                    time.sleep(0.02)
                    sys.stdout.write("\r%d%% Pensando... " % i)
                    sys.stdout.flush()
            
                jugada_maquina1 = random.randint(1, 9)
                jugada_maquina = str(jugada_maquina1)
            
                if tablero[jugada_maquina] == ' ':
                    tablero[jugada_maquina] = maq
                    cont = cont + 1
                    turno = 1
                    clear()
                
                
                else:
                    print("El lugar está ocupado")
                    continue

 
            if cont >= 5:
                if tablero['7'] == tablero['8'] == tablero['9'] != ' ':  
                    printTab(tablero)
                    print("\nGame Over.\n")                
                    print("Gana línea 7-8-9 :) ")                
                    break
                elif tablero['4'] == tablero['5'] == tablero['6'] != ' ':  
                    printTab(tablero)
                    print("\nGame Over.\n")                
                    print("Gana línea 4-5-6 :) ")
                    break
                elif tablero['1'] == tablero['2'] == tablero['3'] != ' ':  
                    printTab(tablero)
                    print("\nGame Over.\n")                
                    print("Gana línea 1-2-3 :) ")
                    break
                elif tablero['1'] == tablero['4'] == tablero['7'] != ' ':  
                    printTab(tablero)
                    print("\nGame Over.\n")                
                    print("Gana línea 1-4-7 :) ")
                    break
                elif tablero['2'] == tablero['5'] == tablero['8'] != ' ':  
                    printTab(tablero)
                    print("\nGame Over.\n")                
                    print("Gana línea 2-5-8 :) ")
                    break
                elif tablero['3'] == tablero['6'] == tablero['9'] != ' ': 
                    printTab(tablero)
                    print("\nGame Over.\n")                
                    print("Gana línea 3-6-9 :) ")
                    break 
                elif tablero['7'] == tablero['5'] == tablero['3'] != ' ':  
                    printTab(tablero)
                    print("\nGame Over.\n")                
                    print("Gana línea 7-5-3 :) ")
                    break
                elif tablero['1'] == tablero['5'] == tablero['9'] != ' ':  
                    printTab(tablero)
                    print("\nGame Over.\n")                
                    print("Gana línea 1-5-9 :) ")
                    break 
 
            if cont == 9:
                print("\nGame Over.\n")                
                print("Empate")
    
        restart = input("¿Desea una nueva partida?(s/n) : ")
        if restart == "s" or restart == "S":  
            for play in tablero_play:
                tablero[play] = " "
            juego()

    elif modo == 2:  
        cont = 0
        clear()
        turno =1
        maq1 =  'X'
        maq2 =  'O'
        for i in range(50):
            printTab(tablero)               
            if turno == 1:
                for i in range(101):                
                    time.sleep(0.02)
                    sys.stdout.write("\r%d%% Pensando... " % i)
                    sys.stdout.flush()
            
                jugada_maquina1 = random.randint(1, 9)
                jugada_maquina = str(jugada_maquina1)
            
                if tablero[jugada_maquina] == ' ':
                    tablero[jugada_maquina] = maq1
                    cont = cont + 1
                    turno = 2
                    clear()
                else:              
                    print("El lugar está ocupado")
                    continue
            elif turno == 2:
                for i in range(101):                
                    time.sleep(0.02)
                    sys.stdout.write("\r%d%% Pensando... " % i)
                    sys.stdout.flush()
            
                jugada_maquina1 = random.randint(1, 9)
                jugada_maquina = str(jugada_maquina1)
            
                if tablero[jugada_maquina] == ' ':
                    tablero[jugada_maquina] = maq2
                    cont = cont + 1
                    turno = 1
                    clear()
                
                
                else:
                    print("El lugar está ocupado")
                    continue

 
            if cont >= 5:
                if tablero['7'] == tablero['8'] == tablero['9'] != ' ':  
                    printTab(tablero)
                    print("\nGame Over.\n")                
                    print(" " +maq1 + " Ganador")                
                    break
                elif tablero['4'] == tablero['5'] == tablero['6'] != ' ':  
                    printTab(tablero)
                    print("\nGame Over.\n")                
                    print(" ¡¡¡ La CPU es la mejor para el Gato !!!")
                    break
                elif tablero['1'] == tablero['2'] == tablero['3'] != ' ':  
                    printTab(tablero)
                    print("\nGame Over.\n")                
                    print(" ¡¡¡ La CPU es la mejor para el Gato !!!")
                    break
                elif tablero['1'] == tablero['4'] == tablero['7'] != ' ':  
                    printTab(tablero)
                    print("\nGame Over.\n")                
                    print(" ¡¡¡ La CPU es la mejor para el Gato !!!")
                    break
                elif tablero['2'] == tablero['5'] == tablero['8'] != ' ':  
                    printTab(tablero)
                    print("\nGame Over.\n")                
                    print(" ¡¡¡ La CPU es la mejor para el Gato !!!")
                    break
                elif tablero['3'] == tablero['6'] == tablero['9'] != ' ': 
                    printTab(tablero)
                    print("\nGame Over.\n")                
                    print(" ¡¡¡ La CPU es la mejor para el Gato !!!")
                    break 
                elif tablero['7'] == tablero['5'] == tablero['3'] != ' ':  
                    printTab(tablero)
                    print("\nGame Over.\n")                
                    print(" ¡¡¡ La CPU es la mejor para el Gato !!!")
                    break
                elif tablero['1'] == tablero['5'] == tablero['9'] != ' ':  
                    printTab(tablero)
                    print("\nGame Over.\n")                
                    print(" ¡¡¡ La CPU es la mejor para el Gato !!!")
                    break 
 
            if cont == 9:
                print("\nGame Over.\n")                
                print("Empate conmigo misma xD")
    
        restart = input("¿Desea una nueva partida?(s/n) : ")
        if restart == "s" or restart == "S":  
            for play in tablero_play:
                tablero[play] = " "
            juego()



if __name__ == "__main__":
    juego()
    
   
 