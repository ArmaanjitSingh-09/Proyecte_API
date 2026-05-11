import json
import webbrowser
json_file = '/dades/dades/SMX1B_Armaan/Prog./Projecte/Diccionari_API.json'
arrayJson = "jugadors"

def afegir_jugador():
    with open(json_file, "r", encoding="utf-8") as f:
        datos = json.load(f)
    nom = input("Introdueix el nom del jugador: ")
    posicio = input("Introdueix la posició del jugador: ")
    edat = int(input("Introdueix l'edat del jugador: "))
    equip = input("Introdueix l'equip del jugador: ")
    nacionalitat = input("Introdueix la nacionalitat del jugador: ")
    imatge = input("Introdueix la URL de la imatge del jugador: ")

    if nom in datos[arrayJson]:
        print("El jugador ja existeix!")
    else:
        new_player = {
            "posicio": [posicio],    
            "edat": edat,
            "equip": equip,
            "nacionalitat": nacionalitat,
            "imagen": imatge,
        }
        datos[arrayJson][nom] = new_player
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=2, ensure_ascii=False)
        print("Jugador afegit correctament!")
    
def buscar_jugador():
    with open(json_file, "r", encoding="utf-8") as f:
        datos = json.load(f)
    nom = input("Introdueix el nom del jugador que vols buscar: ")
    if nom in datos[arrayJson]:
        jugador = datos[arrayJson][nom]
        print(f"--- {nom} ---")
        print(f"Posició: {', '.join(jugador.get('posicio', []))}")
        print(f"Edat: {jugador['edat']} anys")
        print(f"Equip: {jugador['equip']}")
        print(f"Nacionalitat: {jugador['nacionalitat']}")
        print(f"URL Imatge: {jugador['imagen']}")
        webbrowser.open(jugador.get('imagen'))
    else:
        print("Jugador no trobat.")

def llistar_jugadors():
    with open(json_file, "r", encoding="utf-8") as f:
        datos = json.load(f)
    print("LLISTA DE JUGADORS (" + str(len(datos[arrayJson])) + " en total):")
    for nom, d in datos[arrayJson].items():
        print(f"   • {nom} - {d['posicio'][0]} - {d['edat']} anys .- {d['equip']} - {d['nacionalitat']}")

def eliminar_jugador():
    with open(json_file, "r", encoding="utf-8") as f:
        datos = json.load(f)
    nom = input("Introdueix el nom del jugador a eliminar: ")
    if nom in datos[arrayJson]:
        del datos[arrayJson][nom]
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=2, ensure_ascii=False)
        print(nom, "eliminat correctament!")
    else:
        print("El jugador no existeix")
    
def menu():
    print("---Benvingut a la API de futbol---")
    print(" 1.Afageir jugador")
    print(" 2.Buscar jugador")
    print(" 3.Llistar")
    print(" 4.Eliminar jugador")
    print(' 5.Sortir')
    option = int(input('Que vols fer?'))
    return option

option = 0
while option != 5:
    option = menu()
    if option == 1:
        afegir_jugador()   
    elif option == 2:
        buscar_jugador()
    elif option == 3:
        llistar_jugadors()
    elif option == 4:
        eliminar_jugador()
    elif option == 5:
        print("Sortint...")
    else:
        print("Opcio no valida, torna a intentar-ho")
    if option != 5:
        input("Prem Enter per tornar al menú...")
