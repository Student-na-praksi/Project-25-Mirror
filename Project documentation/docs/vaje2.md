# Zapiski - vaje 2

S predlogom projekta mi prepričujemo naročnika, da bo naš projekt zmagal na razpisu. Tu naj še ne varčujemo z besedami.

Kaj vse mora bit v predlogu projekta:

1) **Organizacija projekta:** 
    - predstavitev skupine (kratek opis članov, znanje, izkušnje, kdo koga nadomešča ob odsotnosti, vloga v skupini (ali bo 1 vodja ali pa si bomo razdelili več SCRUM vlog) )
    - upravljanje projekta (kako bomo vodili projekt - sestanki/orodja za komunikacijo/...)
    - razporeditev dela po članih

2) **Obvladovanje tveganj:**
	- identifikacija (predvidimo čim več tveganj - več kot jih je, bolj sposobni in resni izpademo naročniku)
		- poimenujemo in dodelimo oznako
		- opišemo
		- določimo tip - tehnologija, orodja, ljudje, organizacija, zahteve, ocenjevanje (npr. časa), varnost (spletna) - tveganja je pol fajn razvrstit po tipih 
		- na kaj vpliva (projekt, izdelek, posel)
	- analiza
		- verjetnost nastopa tveganja (lestvica: zelo visoka, visoka, zmerna, nizka, zelo nizka)
		- učinek - kakšne bodo posledice (lestvica: usodne, resne, dopustne, neznatne)
        - matrika izpostavljenosti tveganj, ki služi kot pomoč za analizo resnosti tveganj glede na zgornja dva parametra. Glede na matriko jih rangiramo po pomembnosti in določimo ukrepe v koraku načrtovanja (spodaj).
	- načrtovanje - glede na dotično tveganje si izberemo primerno strategijo zanj:
		- strategija izogibanja (zmanjšanje verjetnosti)
		- strategija zmanjševanja (zmanjšanje vpliva)
		- krizni načrt (kako gasiš požar)


3) **Projektni načrt:**
	- povzetek razdelitve projekta na aktivnosti
        - imamo 4 iteracije, 
		- projekt se začne s 1. fazo (iteracijo) (26. 2.) - predlog projekta
		- konča se 26. 5. (pon zjutraj)
		- v načrtu upoštevaj, da se med vikendi in prazniki ne dela!
		- koliko delovnih dni? (62)
		- ČM = 1č * 1m ~= 160 h
		- ČD = 1č * 1d = 8 h
        - mi imamo 4č * 62d = 248 ČD = 1984 h
        - seveda ne delamo 8 ur na dan (160 ur/mesec), ampak 50 - 100 ur/mesec (2,5 - 5 ur/dan) - to je še zmer ful?? ampak očitno se to pričakuje

	- načrt aktivnosti - opis vsake aktivnosti vsebuje:
        - oznako
        - datum začetka
        - datum konca
        - trajanje
        - naziv
        - obseg v ČM (ali ČD?)
        - seznam ciljev (kaj želimo s to aktivnostjo doseči)
        - opis aktivnosti
        - morebitne odvisnosti in omejitve (odvisnosti = aktivnosti, ki morajo biti obvezno zaključene, preden se lahko lotimo te)
        - pričakovani rezultati aktivnosti

        Primeri aktivnosti za 1. iteracijo:
        - izbira izziva
        - pregled dokumentacije
        - planiranje iteracije
        - izdelava predloga projekta
        - sestanek z naročnikom
        - izvedba retrospektive (kaj je blo dobro, kaj slabo, a je kater član skupine zelo nevešč - mu je treba pomagat, a je kdo zlo dober,izkušen, kako bomo to izkoristili ...)

	- seznam izdelkov - KAJ bo narejeno in KDAJ (primeri izdelkov: seznam zahtev, zapiski, delujoča login funkcionalnost ...)
	- časovni potek: (plantUML !)
		- Ganttov diagram
			* Prva iteracija naj bo podrobno razbita v skladu z našim načrtom, ostale pa za zdaj le v osnovni obliki.
			* Označena naj bo tudi kritična pot!
			* Lahko uporabimo barve (vsaka iteracija v svoji barvi ali pa svoja barva za že narejene/trenutno izvajane/še ne izvajane aktivnosti)
		- diagram PERT (odvisnosti med aktivnostmi, trajanje aktivnosti in količina drsenja posamezne aktivnosti)
			- Z njim ugotovimo trajanje projekta in kritično pot.
			- Vsaka aktivnost ima 6 števil: trajanje, drsenje, earliest start & finish, latest start & finish.
			- Aktivnosti, ki imajo drsenje = 0, so na kritični poti.


## Naše iteracije:
1) izdelava predloga projekta
2) ZAJEM ZAHTEV, analiza in načrtovanje, implementacija, testiranje
3) zajem zahtev, ANALIZA IN NAČRTOVANJE, implementacija, testiranje
4) zajem zahtev, analiza in načrtovanje, IMPLEMENTACIJA, TESTIRANJE

Fokus naj bo na odebeljenih aktivnostih - verjetno tudi najdlje trajajo v našem načrtu.
