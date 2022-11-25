from cmath import pi
from doctest import REPORTING_FLAGS
from importlib.machinery import FrozenImporter
from multiprocessing.connection import wait
from queue import PriorityQueue
from random import sample
import os
import random
from time import sleep
import string
from turtle import clear
from unittest import skip
from colorama import init
init()
from colorama import Fore, Back, Style
testr = 1
balance = 0
ketInput = 0
choice = "" 
choice1 = ""
# listKey = ["TE","TA","TO"]


banner = """
              ██╗     ███████╗    ██████╗ ████████╗██╗████████╗    ████████╗ ██████╗  ██████╗ ██╗     
              ██║     ██╔════╝    ██╔══██╗╚══██╔══╝██║╚══██╔══╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
              ██║     █████╗      ██████╔╝   ██║   ██║   ██║          ██║   ██║   ██║██║   ██║██║     
              ██║     ██╔══╝      ██╔═══╝    ██║   ██║   ██║          ██║   ██║   ██║██║   ██║██║     
              ███████╗███████╗    ██║        ██║   ██║   ██║          ██║   ╚██████╔╝╚██████╔╝███████╗
              ╚══════╝╚══════╝    ╚═╝        ╚═╝   ╚═╝   ╚═╝          ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                                                                                                                  
"""

print(Fore.RED + banner)
print("")
print("")
print("")
InfoSystem = """ [Info System ●] : """

PathMachine = """HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\ComputerName\ """

FileClear = """" : Clear/.'UserCache' """

def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))
# = print(random_char(5)) |5 = Nombre caractere

# Choice

while True:
  print("┌―――――┬――――――――――――――――――――――――――――――――┐")
  print("| [1] | ✶ Comment uitliser?            |")         
  print("| [2] | ✶ Crédit                       |")                    
  print("| [3] | " + Fore.MAGENTA+"✶ ID To Token        " + Fore.RED + "          |")
  print("| [4] | ✶ Exit                         |")
  print("└―――――┴――――――――――――――――――――――――――――――――┘")

  print(Fore.YELLOW + "")
  print(Fore.YELLOW + "")
  


  # line for choice the option 
  choice1 = input("Entrer votre choix : ")
  print("")
  print("")

        


  # answer after enter key 
  hwidchanged = "✅L'HWID a été chnagé avex succés !"
# ┌⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯ KEY ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┐

  if (choice1 == "1"):
    print("Mettez L'ID de la personne dans l'option [3], ensuite suivez les instructions ;)")
    sleep(15)
    os.system('cls')

  # Enter Key 
  elif (choice1 == "3"):
    kekt = input("Entrer l'ID  : ")
    sleep(2)
    os.system('cls')
    print(Fore.BLUE+ "[Info System] : Wait...")
    sleep(6)
    print(Fore.RED +"Try:" + Fore.MAGENTA + " Date.get.user/cookie/cache |  " + Fore.BLUE +"EXEC./Request:IP=Github/leptittool")
    sleep(0.5)
    print(Fore.RED +"Try:" + Fore.MAGENTA + " Date.get.user/cookie/cache |  " + Fore.BLUE +"EXEC./Request:IP=Github/leptittool")
    sleep(0.5)
    print(Fore.RED +"Try:" + Fore.MAGENTA + " Date.get.user/cookie/cache |  " + Fore.BLUE +"EXEC./Request:IP=Github/leptittool")
    sleep(0.5)
    print(Fore.RED +"Try:" + Fore.MAGENTA + " Date.get.user/cookie/cache |  " + Fore.BLUE +"EXEC./Request:IP=Github/leptittool")
    sleep(0.5)
    print(Fore.RED +"Try:" + Fore.MAGENTA + " Date.get.user/cookie/cache |  " + Fore.BLUE +"EXEC./Request:IP=Github/leptittool")
    sleep(0.5)
    print(Fore.RED +"Try:" + Fore.MAGENTA + " Date.get.user/cookie/cache |  " + Fore.BLUE +"EXEC./Request:IP=Github/leptittool")
    sleep(0.5)
    print(Fore.RED +"Try:" + Fore.MAGENTA + " Date.get.user/cookie/cache |  " + Fore.BLUE +"EXEC./Request:IP=Github/leptittool")


    print(Fore.GREEN + "----------------------------  FINISH  ----------------------------")
    print("")
    print("")
    print("")

    print(Fore.CYAN + "Token : NT"+ random_char(25) + "." + random_char(30) )
    sleep(1000000)
    print("")
    print("")
    print("")
    print("")






  if (choice1 == "TFEN-LZZE-OYVX-LIFE"):
    ketInput = input("Vous voulez vraiment changer d'HWID(ProfilGuildPC) ? Si oui, appuyez sur ENTRER.")



  # Credit
  elif (choice1 == "2"):
    # Output the balance
    print("By Le P'tit Tool | https://discord.gg/wWM9tS36bR ")  

  # Exit 
  elif (choice == "4"):
    exit()
    break


  # Invalid Option #
  else:
    print(Fore.MAGENTA + "Option invalide. Réssayez !")
    sleep(2)
    print(Fore.WHITE)


