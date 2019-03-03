from pytube import YouTube
from bs4 import BeautifulSoup as bs
import requests as r
import os
import sys

def cls():
    os.system("cls")
cls()
n = 1
linkurl = []

title = input("Titre de la vidéo : ")
name = "https://www.youtube.com/results?search_query="+title
req = r.get(name)
soup = bs(req.text,"html.parser")
page = soup.find_all('a')
for link in page:
    if "watch" in link.get('href'):
        if link.string != None:
         print("\n["+str(n)+"]Titre de la vidéo : " + link.string)
         print("URL de la vidéo : " + link.get('href')+"\n")
         print("-----------------------------------------------------------------------------")
         url = "https://www.youtube.com"+link.get('href')
         linkurl.append(url)
         n+=1
choice = int(input("Nombre de la vidéo voulu : "))
todl = linkurl[choice-1]
cls()
yt = YouTube(todl)

print("Titre de la vidéo : " + yt.title+"\n")
print('''
[1] Télécharger la vidéo
[2] Obtenir la miniature de la vidéo
''')
action = input('Que voulez vous faire : ')
if action == "1":
    print('''
    [1] Télécharger le son
    [2] Télécharger la vidéo
    [3] Afficher tout
    ''')
    format = input('Télécharger en format : ')
    if format == "1":
        available = yt.streams.filter(only_audio=True).all()
        n = 1
        for element in available:
            print("["+str(n)+"] "+str(element))
            n+=1
        down_choice = int(input("Choisis la qualité : "))
        download = available[down_choice-1]
        download.download()
        sys.exit('Travail terminé !')
    if format == "2":
        available = yt.streams.filter(only_video=True).all()
        n = 1
        for element in available:
            print("["+str(n)+"] "+str(element))
            n+=1
        down_choice = int(input("Choisis la qualité : "))
        download = available[down_choice-1]
        download.download()
        sys.exit('Travail terminé !')
    if format == "3":
        available = yt.streams.all()
        n = 1
        for element in available:
            print("["+str(n)+"] "+str(element))
            n+=1
        down_choice = int(input("Choisis la qualité : "))
        download = available[down_choice-1]
        download.download()
        sys.exit('Travail terminé !')
elif action == "2":
    print("Voici l'url de la miniature : "+yt.thumbnail_url)
    sys.exit('Travail terminé !')
