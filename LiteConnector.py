import sqlite3
import barcode
import cv2 as cv
import sys
import os
from barcode.writer import ImageWriter
from PIL import Image, ImageDraw, ImageFilter
import time

ints = 0; i = 1; dodaj = ''
img = cv.imread('bckg.jpg')
putanja = (r'C:\Users\matijaoreskovic2\PycharmProjects\SQLconnector')


def kartica(ime):
    font=cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, ime, (60, 128), font, 1, (0, 0, 0), 2, cv.LINE_AA)
    cv.putText(img, time.asctime(), (60, 180), font, 0.5, (0, 0, 0), 2, cv.LINE_4)
    cv.imwrite(ime + '_created.png', img)
    img1 = Image.open(ime + '_created.png')
    img2 = Image.open(ime +'.png')
    img2 = img2.resize([200, 100])
    img2_c=img2.copy()
    img1.paste(img2, (320,106))
    img1.save(ime+'_created.png')
    Image.open(ime + '_created.png').show()
2
def barcode_get(text, name):
    ean = barcode.get('ean13', text, writer=ImageWriter())
    ean.save(name)

def digit_check(input):
    return any(char.isdigit() for char in input)

con = sqlite3.connect('TestnaBaza.db')
c = con.cursor()

c.execute("CREATE TABLE IF NOT EXISTS SQLBase (id INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(50), number int);")

f_select = input("Odaberite funkciju:\n 1 - Dodavanje\n 2 - Brisanje\n 3 - Drop table\n --Odabir: ")

if f_select=="1":
    ime = input("Unesite ime za dodavanje: ")
    broj = input("Unesite broj korisnika: ")
    while (len(dodaj) + len(broj)) < 12:
        dodaj = dodaj + '0'
    broj = dodaj + broj
    c.execute("SELECT id FROM SQLBase order by id desc;")
    index = c.fetchone()  # ispisi samo najveću vrijednost
    try:
        index = index[0] + 1  # pretvori u integer i povećaj vrijednost za 1
    except:
        index = 0
    barcode_get(str(broj), ime)
    c.execute("INSERT INTO SQLBase (id, name, number) VALUES (?, ?, ?);", (index, ime, broj))
    kartica(ime)
elif f_select=="2":
    while i == 1:
        selector=input("Unesite ime korisnika ili broj koji želite obrisati: ")
        if digit_check(selector):
            c.execute("SELECT * FROM SQLBase WHERE number LIKE ?", ("%" + selector + "%",))
        else:
            c.execute("SELECT * FROM SQLBase WHERE name LIKE ?", ("%" + selector + "%",))
        rez = c.fetchall()
        if not rez:
            print("Nema rezultata. Ponovite pretragu\n")
            i = 1
        else:
            i = 0
            print("Pronadeni su ovi rezultati:\n")
            print(rez)
            pass
        delete = input("Odaberite index sa popisa: ")
        c.execute("DELETE FROM SQLBase where id = ?", delete)
elif f_select=="3":
    c.execute("DROP TABLE SQLBase")
    popis = os.listdir(putanja)
    for slika in popis:
        if slika.endswith(".png") and not "bckg" in slika:
            os.remove(os.path.join(putanja, slika))

try:
    c.execute("SELECT * FROM SQLBase;")
    print(c.fetchall())
except:
    pass

con.commit()
con.close()


