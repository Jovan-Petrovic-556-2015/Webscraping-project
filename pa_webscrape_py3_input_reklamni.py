from urllib.request import urlopen as zahtev
from bs4 import BeautifulSoup as supa
from timeit import default_timer as tajmer
import codecs												#ubacivanje potrebnih biblioteka

veza = input('Nalepi URL ka zeljenoj pretrazi: \n')      	#unos html veze

pocetak = tajmer()                                          #pocetak merenja vremena izvrsenja

klijent = zahtev(veza)										#preuzimanje internet stranice
html_stranica = klijent.read()            
klijent.close()												#zatvaranje konekcije

stranica_supa = supa(html_stranica, "html.parser")   		#pravljenje html objekta

automobili = stranica_supa.findAll("article",
 {"class":"single-classified"})    							#uzima sve automobile

fajl = "automobili.csv"										#fajl za smestanje podaka, upisivanje zaglavlja
f = codecs.open(fajl, "w","utf-8")
#f = open(fajl, "w")										#obican open ne pise dobro cirilicu
zaglavlja = "Назив;Цена;Годиште;Километража;Гориво;Запремина мотора;Снага;Локација\n"
f.write(zaglavlja)

for automobil in automobili:								#za svaki article sa klasom single-classified:...
	try:
	
		atributi = automobil.find('a').attrs
		naziv = atributi['title']
		naziv = naziv.replace(",","")
		naziv = naziv.replace(";","")
		naziv = naziv.replace("|","")
		naziv = naziv.replace("\\","")
		
	
		div = automobil.findAll('div')
	
		godiste = div[7].text
		godiste = godiste.replace("|","")
		godiste = godiste.replace(";","")
		godiste = godiste.replace(",","")
		godiste = godiste.replace("\\","")
		godiste = godiste.strip()
	
		kilometraza = div[8].text
		kilometraza = kilometraza.replace("|","")
		kilometraza = kilometraza.replace(",","")
		kilometraza = kilometraza.replace(";","")
		kilometraza = kilometraza.replace("\\","")
		kilometraza = kilometraza.strip()
	
		gorivo = div[9].text
		gorivo = gorivo.replace("|","")
		gorivo = gorivo.replace(";","")
		gorivo = gorivo.replace(",","")
		gorivo = gorivo.replace("\\","")
		gorivo = gorivo.strip()
		
		zapremina_motora = div[10].text
		zapremina_motora = zapremina_motora.replace(",","")
		zapremina_motora = zapremina_motora.replace("|","")
		zapremina_motora = zapremina_motora.replace(";","")
		zapremina_motora = zapremina_motora.replace("\\","")
		zapremina_motora = zapremina_motora.strip()
		
		snaga = div[12].text
		snaga = snaga.replace(",","")
		snaga = snaga.replace("|","")
		snaga = snaga.replace(";","")
		snaga = snaga.replace("\\","")
		snaga = snaga.strip()
		
		lokacija = div[17].text
		lokacija = lokacija.replace(",","")
		lokacija = lokacija.replace("|","")
		lokacija = lokacija.replace(";","")
		lokacija = lokacija.replace("\\","")
		lokacija = lokacija.strip()								#u slucaju pogresnog unosa, stampa prazno
		if len(lokacija)>23:
			lokacija = ""
		
		
		spanovi = automobil.findAll('span')
		cena = spanovi[1].text
		cena = cena.replace(";","")
		cena = cena.replace(",","")
		cena = cena.replace("|","")
		cena = cena.replace("\\","")
		cena = cena.strip()
		
		f.write(naziv + ";" + cena + ";" + godiste + ";" +
		kilometraza + ";" + gorivo + ";" + zapremina_motora +
		";" + snaga + ";" + lokacija + "\n")
		
	except:
	
		naziv = automobil.a.string
		cena = automobil.find("span",{"class":"price"}).string
		cena = cena[:-1]
		detalji = automobil.findAll("span", {"class":""})
		
		godiste = detalji[0].text
		godiste = godiste.replace("|","")
		godiste = godiste.replace(",","")
		godiste = godiste.replace(";","")
		godiste = godiste.replace("\\","")
		godiste = godiste.strip()
		
		kilometraza = detalji[1].text
		kilometraza = kilometraza.replace("|","")
		kilometraza = kilometraza.replace(",","")
		kilometraza = kilometraza.replace(";","")
		kilometraza = kilometraza.replace("\\","")
		kilometraza = kilometraza.strip()
		
		gorivo = detalji[2].text
		zapremina_motora = detalji[3].text
		zapremina_motora = zapremina_motora.replace("|","")
		zapremina_motora = zapremina_motora.replace(",","")
		zapremina_motora = zapremina_motora.replace(";","")
		zapremina_motora = zapremina_motora.replace("\\","")
		zapremina_motora = zapremina_motora.strip()
		
		lokacija = detalji[5].text
		lokacija = lokacija.replace(",","")
		lokacija = lokacija.replace(";","")
		lokacija = lokacija.replace("|","")
		lokacija = lokacija.replace("\\","")
		lokacija = lokacija.strip()
		
		snaga = ""
		
		
		f.write(naziv + ";" + cena + ";" + godiste + ";" + kilometraza + ";" + gorivo + ";" + zapremina_motora + ";" + snaga + ";" + lokacija + "\n")
	
f.close()													#zatvori fajl
kraj = tajmer()												#zaustavi merenje vremena
vreme = str(round(kraj - pocetak, 2))
broj_automobila = str(len(automobili))
print ("Pronadjeno " + broj_automobila + " automobila za " +	#stampanje rezultata skripte
 vreme + " s" )
print ("Pritisni Enter za izlazak")
input()														#da se ne bi zatvorio prozor odmah ceka se ulaz
