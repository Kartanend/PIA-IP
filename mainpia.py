#PIA PROGRAMACIÓN
#Comentario x
import requests
import os
from bs4 import BeautifulSoup as bs

fuente=list()
def bustxt(cpath,fuente):
    carpeta=os.listdir(cpath)
    for file in carpeta:
        if ".txt" in file:
            nom=str(file)
            filepath=os.path.join(cpath,nom)
            fo=open(filepath,"r")
            print("\nArchivo txt: ",nom,"\nURLS encontrados:")
            for url in fo:
                print("\t",url.rstrip())#URLS
                fuente.append(url.rstrip())
            fo.close()
    return fuente

#Seleccionar carpeta
cpath=os.getcwd()
print("Actualmente se encuentra en la carpeta: ", cpath)
opc=int(input("¿Desea cambiar de carpeta? 1-SI 2-NO: "))
while opc!=1 and opc!=2:
    opc=int(input("Opción no válida! Ingrese 1-SI 2-NO: "))
if opc==1:
    cpath=input("Ingrese el path absoluto de la carpeta Ej. C:\\Users\\name\\Desktop: ")
    valpath=os.path.exists(cpath)
    while valpath==False:
        cpath=input("No existe la carpeta, ingrese otra carpeta: ")
        valpath=os.path.exists(cpath)
    os.chdir(cpath)
print("Carpeta actual: ",os.getcwd())

#BUSCAR TXT EN CARPETA
print("Realizando busqueda de archivos de texto...")
fuenteurl=bustxt(cpath,fuente)

#MENU AGREGAR ELIMINAR FUENTES DE INFORMACIÓN
mod=int(input("¿Quiere agregar más fuentes de información? 1-SI 2-NO: "))
while mod!=1 and mod!=2:
    mod=int(input("Opción no válida! Ingrese 1-SI 2-NO: "))
if mod==1:
    fi=open("NuevaFuente.txt","a")
    añadir=""
    while añadir!="S":
        if añadir!="":
            fi.write(añadir+"\n")
        añadir=input("Ingrese url, \"S\" para salir y guardar: ")
    fi.close()
    print("Fuentes actualizadas...")
    fuenteurl.clear()
    fuenteurl=bustxt(cpath,fuenteurl)

print(fuenteurl)
mod2=int(input("\n¿Quiere eliminar fuentes de información? 1-SI 2-NO: "))
while mod2!=1 and mod2!=2:
    mod2=int(input("Opción no válida! Ingrese 1-SI 2-NO: "))
if mod2==1:
    elim="1"
    for fu in range(len(fuenteurl)):
        print(str(fu+1)+".- "+fuenteurl[fu])
    while elim!=-1:
        elim=int(input("\nIngrese el número de url a eliminar, -1 para salir y guardar: "))
        if elim!=-1:
            fuenteurl.pop(int(elim)-1)
            for fu in range(len(fuenteurl)):
                print(str(fu+1)+".- "+fuenteurl[fu])

    print(fuenteurl)


#EXP REGULARES
#correo=re.compile(r"")
#telefono=re.compile(r"")
#fundacion=re.compile(r"")
#WEB SCRAPING
for elem in fuenteurl:
    try:
        page=requests.get(elem)
        if page.status_code==200:
            print("BIEN")
            soup=bs(page.content,"html.parser")
            po=soup.find_all("p")#parrafos
            for parr in range(len(po)):
                potext=po[parr].getText()
                #buscar expr
            po2=soup.find_all("title")#titulos
            for title in range(len(po2)):
                po2text=po2[title].getText()
                #print(po2text)
            po3=soup.find_all("a")#URL
            for url in po3:
                if (url.get('href')) is not None:
                    #print(url.get('href'))
                    if "palmares" in (url.get('href')):#url buscar premios?
                        print(url.get('href'))
                    if "jugadores" in (url.get('href')):#url buscar jugadores?
                        print(url.get('href'))
            #Descargar imagenes

        else:
            print("La página no existe")
            print(page.status_code,elem)
    except ValueError:
        print("No es una página válida")

    #TITULARES
    #DESCARGAR IMAGENES -->CARPETA MODULO OS

    #INTEGRAR EN EST DATO --> PREGUNTAR USUARIO

    #3 FECHAS PARTIDOS  API OPENWEAHTER TEMPERATURA

    #INFO A EXCEL
