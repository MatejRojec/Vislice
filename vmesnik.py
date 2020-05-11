from model import Igra, nova_igra

datoteka = open('besede.txt', encoding='utf-8')
bazen_besed = []
for vrstica in datoteka:
    nova_vrstica = vrstica.strip('\n')
    bazen_besed.append(nova_vrstica)

import random
igra = Igra(random.choice(bazen_besed))

def pozdrav():
    print('VISLICE')
    print(f'Geslo {igra.pravilni_del_gesla()}')

def izpis_zmage():
    print('Bravo, zmagal si! Congrats.')
    
def izpis_poraza():
    print('Preveč napak, izgubil si! :( ')

def izpis_igre():
    print('')
    print('')
    print(f'Nepravilni ugibi: {igra.nepravilni_ugibi()}, ({igra.stevilo_napak()}/10)')
    print(f'Uganjeno: {igra.pravilni_del_gesla()}')

def zahtevaj_vnos():
    print('Ugibaj črko:')
    ugib = input('>')
    return ugib

def pozeni_vmesnik():
    pozdrav()
    while not igra.zmaga() and not igra.poraz():
        igra.ugibaj(zahtevaj_vnos())
        izpis_igre()
    if igra.poraz():
        izpis_poraza()
    else:
        izpis_zmage()

pozeni_vmesnik()