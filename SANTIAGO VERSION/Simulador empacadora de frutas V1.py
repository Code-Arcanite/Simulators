import sys,os
import time
#print("importing python")
try :

    import pygame as pyg
    from pygame.locals import *
    pyg.init()
    
#    print("[+]load pygame OK")
except:
#    print("[-] failed to load pygame ...")
#    print("[-] closing program....")
    sys.exit(1)
pantX,pantY=500,400
pantalla=pyg.display.set_mode((pantX,pantY))
pyg.display.set_caption("SIMULADOR de empacadora de frutas V1")
#=========== CONTROL DEL TIEMPO
FPS = 60
RELOJ=pyg.time.Clock()

#=========== IMAGENES USADAS EN EL PROGRAMA

background_img=pyg.image.load('img/fondo.png')
fruta_img=pyg.image.load('img/manzana.png')
box_E=pyg.image.load('img/cajavacia.png')
box_ME=pyg.image.load('img/cajamedia.png')
box_F=pyg.image.load('img/cajafull.png')


pyg.display.set_icon(box_ME)

#========= COLORS
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)

#========= DEFINICION DE COORDENADAS
#PB1

caja_E_coorX=140
caja_E_coorY=130

#PB2

caja_E_coorXb=-50
caja_E_coorYb=40

#PB3

caja_E_coorXc=-220
caja_E_coorYc=-50


#========= CORRECTOR DE COORDENADAS

def coor(X,Y):
    X=X+250
    Y=-Y+200
    return (X,Y)
#========= IMAGENES DINAMICAS


def caja_e(X,Y):
    pantalla.blit(box_E,(X,Y))

def caja_me(X,Y):
    pantalla.blit(box_ME,(X,Y))

def caja_f(X,Y):
    pantalla.blit(box_F,(X,Y))

def fruit(X,Y):
    pantalla.blit(fruta_img,(X,Y))

def caja_E_s(film):
    caja_e(coor(140-film,0)[0],coor(0,int((140-film)*9/17)+int(1210/17))[1])

def caja_F_s(film):
    caja_f(coor(140-film,0)[0],coor(0,int((140-film)*10/17)+int(1210/17))[1])
    #caja_f(coor(-50-film,0)[0],coor(0,int((-50-film)*(9/17)+int(1130/17)))[1])


def fruta_s(film):
    fruit(coor(-150+film,0)[0],coor(0,int((120-film)*6/13)+int(660/13))[1])
    #print("coordenadas fruta :",coor(-150+film,0)[0],coor(0,int((120-film)*6/13)+int(660/13))[1])

def cajas_dinamicas(film):
    #print(film,"coor X :",coor(140-film,0)[0])

    if coor(140-film,0)[0]>198:
    #ccaja vacia que va
        caja_E_s(film)
    #caja llena que sale
    elif coor(140-film,0)[0]<208:

        caja_F_s(film)

    else:
        pass
#================ GUI DINAMICA

def GUI(status,fc,fpc,promedio):
    os.system("cls")
    os.system("color a")
    os.system("TITLE Empacadora de Frutas GUI-V1")

    #punto=["██╗","╚═╝","░░░","░░░","██╗","╚═╝"]
    #nueve_n=["░█████╗░","██╔══██╗","╚██████║","░╚═══██║","░█████╔╝","░╚════╝░"]

    running=("║█▀█ █░█ █▄░█ █▄░█ █ █▄░█ █▀▀\n║█▀▄ █▄█ █░▀█ █░▀█ █ █░▀█ █▄█")
    MARCHA=("║█▀▄▀█ ▄▀█ █▀█ █▀▀ █░█ ▄▀█\n║█░▀░█ █▀█ █▀▄ █▄▄ █▀█ █▀█")
    PARO=("║█▀█ ▄▀█ █▀█ █▀█\n║█▀▀ █▀█ █▀▄ █▄█")
    REINICIO=("║█▀█ █▀▀ █ █▄░█ █ █▀▀ █ █▀█\n║█▀▄ ██▄ █ █░▀█ █ █▄▄ █ █▄█")
    
    print("╔══════EMPACADORA DE FRUTAS GUI V1════════╗")
   # print("║ Version 2021-V1 \n║ Creado por Santiago Torres \n║ Exp:2016247083 \n║ COMPUTACION II\n║ UNEXPO")
    print("║ GRAPHIC USER INTERFACE ")
    print("║ ")
    print("║ Estado actual de la maquinaria :")
    if status==0:
        os.system("color c")
        print(PARO)
      
    elif status==1:
        os.system("color a")
        print(MARCHA)
      
    elif status==2:
        
        os.system("color d")
        print(REINICIO)
    else:
        
        print("║█▀▀ █▀█ █▀█ █▀█ █▀█\n║██▄ █▀▄ █▀▄ █▄█ █▀▄\n║ HERRAMIENTA DE COLISION DE ERRORES EN MARCHA \n║  (EL PROGRAMA SE REINICIARA)")
        

    if promedio=="MAS":
        print("║ ")
        os.system("color e")
        print("║ ▄█▄   █▀▀ █▀█ █░█ ▀█▀ ▄▀█\n║ ░▀░   █▀░ █▀▄ █▄█ ░█░ █▀█")
     

    elif promedio=="MENOS":
        print("║ ")
        os.system("color e")
        print("║ ▄▄   █▀▀ █▀█ █░█ ▀█▀ ▄▀█\n║ ░░   █▀░ █▀▄ █▄█ ░█░ █▀█")
      
    else:
        pass
    print("║ ")
    print("║ Frutas en caja:",fc)
    print("║ ")
    print("║ Frutas por caja :",fpc)
    print("╚═════════════════════════════════════════╝")



def presentacion():

    os.system("cls")
    os.system("color F")
    os.system("TITLE Empacadora de Frutas GUI-V1")
    print("╔════════════════════════════════════╗")
    os.system("color c")
    print("║ █▀ █ █▀▄▀█ █░█ █░░ ▄▀█ █▀▄ █▀█ █▀█\n║ ▄█ █ █░▀░█ █▄█ █▄▄ █▀█ █▄▀ █▄█ █▀▄")
    print("║  DE EMPAQUETADO DE FRUTA \n║ Version 2021-V1 \n║ Creado por Santiago Torres \n║ Exp:2016247083 \n║ MATERIA:COMPUTACION II\n║ UNIVERSIDAD:UNEXPO")
    print("║ █░█ █▄░█ █▀▀ ▀▄▀ █▀█ █▀█\n║ █▄█ █░▀█ ██▄ █░█ █▀▀ █▄█\n║ sede CHARALLAVE")
    os.system("color a")
    print("╚════════════════════════════════════╝")


def espera():
    os.system("color c")
    print("╔════════════════════════════════════╗")
    print("║ █▀▀ █▀ █▀█ █▀▀ █▀█ ▄▀█\n║ ██▄ ▄█ █▀▀ ██▄ █▀▄ █▀█\n║ ")
    print("║ ESPERA DE 3 SEGUNDOS")
    print("║ ")
    print("║ ")
    print("╚════════════════════════════════════╝")
#=========== CICLO
def ciclo():
    print("1)caja vacia")
    print("2)caja medio llena")
    print("3)caja llena")

#============ MALLA GUIA
def malla():
    for i in range(0,10):

        pyg.draw.line(pantalla,BLUE,(0,i*40),(500,i*40),1)
        pyg.draw.line(pantalla,GREEN,(50*i,0),(50*i,400),1)
    pyg.draw.line(pantalla,RED,(0,200),(500,200),1)
    pyg.draw.line(pantalla,RED,(250,0),(250,400),1)
    
#=========== VARIABLES DE ENTORNO ===============
pantalla.fill(WHITE)

film=0
film_f=0
#global Frutas_en_caja
Frutas_en_caja=2
frutas=0
ACTIVE=False
fuente=pyg.font.Font(None,35)
#pygame.font.Font.render
fuente_sp=pyg.font.Font(None,25)
last_state=0
llenando=False

#==========BUCLE PRINCIPAL
presentacion()

while True:
    

    pantalla.blit(background_img,(-100,0))

    #===== MALLA USADA COMO GUIA ============
    malla()
    #====== cantidad de frutas
    #sello=fuente_sp.render("Andrés Pabón",0,(BLACK))
    #sello2=fuente_sp.render("Exp:2016247003",0,(BLACK))
    #sello3=fuente_sp.render("Computacion II",0,(BLACK))

    if ACTIVE and last_state!=1:
        GUI(1,int(frutas/129),Frutas_en_caja,0)
        last_state=1

    #text=fuente.render(str(Frutas_en_caja),0,(BLACK))
    #text2=fuente.render(str(int(frutas/129)),0,(BLACK))

    if ((frutas/129)==Frutas_en_caja) and llenando :
        #caja_me(205,161)
        print("espera de 3 segundos")
        espera()

        time.sleep(3)
        print("finalizo la espera")
        llenando=False

        
    #pantalla.blit(sello3,(0,40))
    #pantalla.blit(sello2,(0,20))
    #pantalla.blit(sello,(0,0))
    #pantalla.blit(text,(350,360))
    #pantalla.blit(text2,(215,360))

    pos= pyg.mouse.get_pos()
    if ACTIVE:

        cajas_dinamicas(film)
        
        #print("position of mouse is :",pos)   
        if coor(140-film,0)[0]==200:
            if frutas!=129*Frutas_en_caja:
                    
                
                    
                #print("guia fruta :",film_f%129)

                fruta_s(film_f%129) 
                if int(frutas/129)>0:
                    llenando=True
                    caja_me(205,161)

                film_f+=1
                frutas+=1
                if film_f%129==0:

                    GUI(1,int(frutas/129),Frutas_en_caja,0)

                #if frutas%129==0:
                    #print(int(frutas/129))

            else :    
                film+=1       
        else:
            film+=1
            frutas=0

            
    if ACTIVE==False:
        fruta_s(film_f%129)
        #fruit(coor(-150,0)[0],coor(0,120)[1])
        cajas_dinamicas(film)
    #===== Activo
    if (pos[0]>=350 and pos[0]<=370 and pos[1]>=290 and pos[1]<=310) and pyg.mouse.get_pressed()[0]==1:
        ACTIVE=True
        
        GUI(1,int(frutas/129),Frutas_en_caja,0)
    #===== Paro
    elif (pos[0]>=400 and pos[0]<=420 and pos[1]>=290 and pos[1]<=310) and pyg.mouse.get_pressed()[0]==1:
        ACTIVE=False
        GUI(0,int(frutas/129),Frutas_en_caja,0)
        fruta_s(film_f%130)
    #==== reset
    elif (pos[0]>=450 \
        and pos[0]<=470 \
        and pos[1]>=290 \
        and pos[1]<=310) \
        and pyg.mouse.get_pressed()[0]==1:


        film=0
        film_f=0
        Frutas_en_caja=10
        frutas=0
        ACTIVE=False
        GUI(2,0,Frutas_en_caja,0)
    #==== +fruta
    elif (pos[0]>=250 \
        and pos[0]<=270 \
        and pos[1]>=290 \
        and pos[1]<=310) \
        and pyg.mouse.get_pressed()[0]==1:

        Frutas_en_caja+=1
        #print("añadiste , actual :",Frutas_en_caja)
        GUI(1,int(frutas/129),Frutas_en_caja,"MAS")
        time.sleep(0.8)
        time.sleep(0.3)
    #==== -fruta
    elif (pos[0]>=300 \
        and pos[0]<=320 \
        and pos[1]>=290 \
        and pos[1]<=310) \
        and pyg.mouse.get_pressed()[0]==1:



        if Frutas_en_caja<=0:
            Frutas_en_caja=0
        else:
            Frutas_en_caja-=1
        time.sleep(0.3)
        GUI(1,int(frutas/129),Frutas_en_caja,"MENOS")
        time.sleep(0.8)
        


    
    
    for event in pyg.event.get():
        if event.type==QUIT:
            pyg.quit()
            sys.exit()
    RELOJ.tick(FPS)
    if coor(140-film,0)[0]<0:
        film=0
    pyg.display.update()
