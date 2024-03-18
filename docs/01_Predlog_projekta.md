
# Celovita rešitev organizacije pluženja


### Jošt Eržen, Filip Gros, Sebastjan Kordiš, Matevž Vidovič


## 1 Uvod


Ob novozapadlem snegu se promet skoraj ustavi. Organizacije, ki se ukvarjajo s pluženjem, se na vso moč trudijo, da se situacija ne poslabša do te mere, da bi postala totalen prometni kolaps.
Naš projekt želi biti celovita rešitev organizacije pluženja, da lahko s tem pomagamo pri koordinaciji in nadzorovanju le tega ter z algoritmičnimi pristopi pluženje naredimo učinkovitejše. Poleg tega želimo povezati pravne in fizične osebe, ki potrebujejo pluženje parkirišč in dvorišč, z izvajalci pluženja, kot so kmetje, da lahko zunaj plužne konice omogočimo to storitev, ki koristi obema stranema.





### 1.1 Izzivi


Člani ekipe se bežno poznamo, ker smo se že nekajkrat videli na faksu, vendar še nikoli nismo med seboj sodelovali na projektu. Predvidevamo, da bodo največji izzivi za ekipo medsebojno usklajevanje, torej organizacija časa, čim bolj ustrezna delitev dela in dobra medsebojna komunikacija.
Prav tako noben član ekipe še ni sodeloval na projektu, ki bi vseboval ravno te tehnologije, kar predstavlja svojevrsten izziv. Večina nas pozna posamezne tehnologije, vendar njihovo povezovanje v nek celoten sistem nam je precej tuje. Algoritem za rešitev problema je zelo kompleksen, vendar obstaja na internetu že veliko rešitev, zato bo iskanje najprimernejše za naš specifičen problem tudi izziv. Ocenjevanje zahtevnosti posameznih nalog nam je tudi tuje področje.
Razvoj algoritma za rešitev problema optimizacije pluženja zna biti zelo kompleksna naloga. Tudi uporaba obstoječe rešitve bo verjetno zahtevno, saj ne bo perfektno naslavljala našega problema, temveč jo bo treba pametno prilagoditi. To zna biti zahtevno, saj takšna implementacija hitro izgubi na efektivnosti, če nismo previdni in iznajdljivi.
Prvi sestanek bo bolj družaben. Cilj njega bo team-building. Nato se bomo dobivali vsak teden, kjer bo vsak povedal napredek na svojem delu projekta, izzive in probleme, ki jih je srečal, ter predstavil tudi možne rešitve. Cilj nam je, da celotna ekipa ve, kaj se dogaja na vsakem področju projekta. Same delitve dela v skupini se bomo lotili po principu javljanja, torej bomo poskusili ustrezati željam vseh članom ekipe. Kjer bosta dva imela enako željo, bomo prišli do kompromisa. Za področja, kjer noben želja ne bo izražena, bo tisti z največ izkušnjami prevzel nalogo. Pri programiranju se bomo držali dobrih praks (sprotno pisanje komentarjev, sprotno testiranje, pred implementiranjem funkcije premislek kaj bodo vhodi in izhodi, grafična predstavitev, vnaprej definirane podatkovne strukture, programiranje po nekaj ur na dan več dni, ne pa en dan 10 ur…)
Ekipi sta že znana jezika Python in JavaScript, ostale tehnologije ter njihovo povezovanje pa nam še nista znana.



## 2 Potrebe naročnika


Primarni naročnik je Mestna občina Celje (v nadaljevanju MOC), sekundarni deležniki pa so Zelenice d.o.o., VOC Celje d.o.o. in ekipa predmeta Tehnologija Programske Opreme.
Če nam uspe implementirati vse zamišljene ideje so sekundarni deležniki tudi občani, lokalna podjetja in kmetje, ki se ukvarjajo s pluženjem.
MOC si od projekta želi izboljšano učinkovitost pluženja, zaradi česar se zmanjša možnost prometnega kolapsa in pohitri promet v snežnih razmerah, kar veča zadovoljstvo občanov.
Podjetji, ki opravljata pluženje, si želita intuitiven in zanesljiv nadzor nad situacijo pluženja, ter zmanjšane stroške pluženja zaradi višje učinkovitosti.
Občani in lokalna podjetja želijo možnost kontakta s kmeti, ki bi bili pripravljeni pomagati pri pluženju dvorišč in parkirišč, saj je to za večje površine izvajati ročno zelo zahtevno in zamudno, medtem ko kmet s plugom to nalogo opravi zelo hitro. Kmetje s plugom pa si želijo dostopa do nove potencialne storitvene dejavnosti.
Sistem mora vsakemu od deležnikov biti preprost za uporabo, brez nepotrebnih funkcionalnosti, zaradi katerih bi postal zapleten. Sistem mora biti robusten, saj, če se deležniki nanj zanašajo, njegova napaka lahko povzroči prometni kolaps.

### 2.1 Uporabniške zahteve


Projekt bo izvajan v treh iteracijah. V zgodnejših iteracijah prioritiziramo uporabniške zgodbe povezane z MUST HAVE zahtevami, če le-te nimajo prevelikih odvisnosti, zaradi katerih bi jih morali prestaviti v kasnejšo iteracijo.


Kot neregistriran uporabnik želim:
- imeti dostop do zemljevida stanja spluženosti cest.
- imeti možnost registracije, da lahko postanem Customer.

Glede na to, da sem neregistriran uporabnik,:
- ko zahtevam možnost registracije, sem preusmerjen na stran ki mi to omogoča.

Kot Admin želim:
- na zemljevidu videti lokacije Ustaljenih Plugov.
- ob kliku na Usataljeni Plug dobiti njihovo telefonsko številko. 
- imeti možnost urejanja števila plugov v štartni bazi in lokacije štartnih baz, da se podatki v zaledju spremenijo v realnem času.

Glede na to, da sem admin,:
- ko kliknem na Ustaljeni Plug na zemljevidu, dobim njegovo telefonsko številko.
- ko zahtevam urejanje števila plugov v štartni bazi in lokacije štartnih baz, se te podatki posodobijo v roku 1 minute po oddani zahtevi.

Kot Ustaljeni Plug želim:
- da se mi glede na trenuten GPS izpisujejo navodila za nadaljno pot.
- imeti možnost deaktivacije, da se lahko umaknem iz pluženja (zaradi malice, okvare, premora).

Glede na to, da sem Ustaljeni Plug,:
- ko zahtevam deaktivacijo, je ta objavljena v roku 30 sekund.


Kot Customer želim:
- imeti možnost oddaje zahtevka za pluženje.

Kot Samostojni Plug želim:
- videti trenutno nalogo.

Kot Manager želim:
- videti lokacije Samostojnih Plugov in ob kliku na dotičen plug dobiti njegovo telefonsko številko.
- imeti možnost usmeriti dotičen Samostojni Plug na zemljevidu na določeno opravilo, da se mu posodobi trenutno opravilo.

Glede na to, da sem Manager,:
- ko Samostojnemu Plugu spremenim opravilo, je ta o njem obveščen v roku 2 minut.



## 3 Cilji projekta


Izdelek našega projekta bo celovita informacijska rešitev pluženja. V osnovi bo to spletna aplikacija, ki bo plužnim službam nudila informacijsko podporo za obsežno pluženje manjšega področja (deluje za simultano organizacijo do 100 plugov).
Administrator ima pregled nad stanjem pluženja in lahko dodaja pluge in štartne baze pluženja, plug pa je avtomatsko voden v smeri njemu začrtanega pluženja. Posodabljanje informacij se dogaja v realnem času, torej se za potrebe pluženja mora posodobiti v največ 3 minutah.
Zemljevid stanja na cestah je na voljo tudi neregistriranim uporabnikom in prikazuje stanje za največ 5 minut nazaj.
Ustvarili bomo funkcionalnost, ki bo omogočala kmetom, ki se ukvarjajo s pluženjem, da se povežejo s podjetji in osebami, ki potrebujejo pluženje parkirišč ter dvorišč. Za potrebe MOC moramo omogočati hranjenje vsaj 70.000 zahtevkov naenkrat.
Cilj je, da poskusimo ustvariti algoritem, ki bo sposoben sam najti čim bolj optimalno verzijo pluženja. Za nek del bomo ročno vnesli traso pluženja, ki se zdi najbolj smiselna, ter svoj algoritem primerjali z ročno izrisano traso - algoritem mora biti vsaj tako dober kot ročno določena trasa. To bomo preverjali s simulacijo vožnje po mestu, ki jo bomo ustvarili. Čim boljši algoritem je naš glavni cilj projekta - a če ugotovimo, da ta cilj ni dosegljiv in ne bo mogoče ustvariti algoritma, ki bi bil vsaj tako dober kot ročno izrisane trase, se bomo v kasnejših iteracijah bolj osredotočili na ostale cilje ter razširili funkcionalnosti informacijske rešitve.


### 3.2 Merila uspeha


Idejo smo predstavili primarnemu naročniku - Mestni občini Celje. Po koncu projekta (in, če bo le možno, že med iteracijami) se bomo sestali z naročnikom ter opravili pregled nalog in ciljev, kjer bomo izvedeli, v kolikšni meri smo izpolnili njihove želje.
Naročniku je pomembno zadovoljstvo uporabnikov sistema (občani, izvajalci pluženja) ter da projekt ustreza smernicam trajnostnega razvoja, kar tudi niža stroške goriva in dela.


## 4 Opis sistema


Predstavitev sistema glede na diagram:

MUST HAVE:
- Ustaljeni Plug: avtomatsko planiranje posebej za Zelenice (pločniki) in VOC (ceste) z vodenjem vsakega posameznega pluga.
- Home page: Login funkcionalnost, pobarvan zemljevid stanja cest. Neregistrirano uporabnik pride samo do sem.
- Admin: Dodajanje začetnih baz s številom plugov. Dodajanje Ustaljenih Plugov v sistem. Pregled stanja Ustaljenih Plugov na cestah.

SHOULD HAVE:
- Samostojni Plug lahko opravlja naročila.
- Stranka se lahko registrira in odda zahtevek za pluženje dvorišča.
- Manager vidi lokacije Samostojnih plugov in jih usmeri na opravljanje naročila.


COULD HAVE:
- vključitev kmetov v pluženje z VOC in Zelenice. To za sabo potegne bolj zapleten algoritem.
- Home Page poizvedba kdaj bo neka ulica splužena.
- Neregistriran uporabnik deli svoj GPS in cilj poti, mi pa mu povemo optimalno pot glede na spluženost cest.
- Posodabljanje pomembnosti cest glede na poti po katerih poizvedujejo Neregistrirani uporabniki.

VEČ INFORMACIJ O ALGORITMU:
- Ceste imajo pomembnostno vrednost glede na njihovo prioritetnost (količina prometa na njej) in količino snega (integral padanja od njenega zadnjega pluženja)
- Če hočemo uporabljati PyVRP, moramo imeti baze pluženja. To je smiselno za VOC in Zelenice, a potem kmetje ne morejo pomagati s pluženjem v smislu, ki bi bil integriran s sistemom VOC in Zelenice.
- Če gremo snovati svoj algoritem, lahko delamo glede na to, kje so trenutni plugi. Ko se priključi nov Samostojni Plug se vsem popravijo poti. Tako Samostojni Plugi sodelujejo pri VOC in Zelenice (z določenimi omejitvami, kot je recimo pluženje glavnih cest).



## 5 Predlagan pristop


_V okviru predloga projekta zadostuje osnutek tega poglavja._


- Na kratko opišite, kako bo sistem deloval.
- Katere platforme, orodja in knjižnice boste uporabljali?
  - Kako boste sistem testirali?
  - Kako boste ovrednotili ustrezno strategije testiranja?


## 6 Vodenje projekta

#### Dnevnik sprememb:
29.2. Začetni nabor idej za možne funkcionalnosti. Zažetek projekta.
7.3. Omejitev idej, ki jih želimo podpirati.
13.3. Ob stoječem sestanku smo dokončno razjasnili želje uporabniške zgodbe in arhitekturo. Sedaj definiramo potrebovane funkcionalnosti.

#### Izvajani procesi in prakse
Uporabljali bomo SCRUM in Extreme Programing.
Tedensko se bomo dobivali na stoječih sestankih ob tabli pred enem izmed laboratorijev, ki imajo tablo. Začeli bomo s tem, da vsak pove težave zadnjega tedna ter kako daleč je prišel, potem pa skupaj zasnujemo, kaj bomo izdelali v naslednjem tednu. SCRUM master bo naloge razdelil.

V naslednji iteraciji želimo zgraditi glavno stran z zemljevidom, ki prikazuje trenutno snežno stanje na cestah ter osnovno delovanje algoritma. Podpirati želimo začeti osnovne pluge in administratorske dožnosti.

### 6.1 Usklajevanje ekipe

Delo bomo med člane skupine razporedili glede na predznanje članov, da bo vsak dobil naloge, ki jih bo glede na svoje znanje najbolj sposoben rešiti. Člani si bodo naloge sprva izbrali sami, v kolikor pa bodo ostale določene naloge neizbrane, jih bo vodja skupine dodelil članom.
Sestajali se bomo tedensko v živo, v primeru, da to ne bo mogoče, pa prek aplikacije Discord. Ob tabli pred enem izmed laboratorijev bomo izvajali stoječe sestanke.
Med sestanki bomo pregledali stanje našega projekta, ocenili napredek od zadnjega sestanka ter razdelili naloge, ki jih bodo člani ekipe morali opraviti do naslednjega sestanka. Pogovorili se bomo o problemih, ki so se pojavili v zadnem tednu in jih poskusili nasloviti. Začrtali bomo delovanje nadaljnjih funkcionalnosti ter definirali njihovo arhitekturo.


### 6.2 Projektni načrt


1. iteracija:
- Izbira izziva 2h 1ČD
- Začetni sestanek nabiranja idej 2h 1ČD
- Pregled podatkov in začetna vizualizacija 8h 4ČD
- Snovanje idej pristopa k algoritmu 7h  3ČD
- Pregled obstoječih rešitev 12h   6ČD
- Sestanki definiranja željene rešitve 15h   7ČD
- Definiranje uporabniških zgodb in funkcionalnih zahtev 8h   4ČD
- Planiranje naslednje iteracije 5h   3ČD
- Pregled dokumentacije 5h   2ČD
- Izdelava predloga projekta 15h    8ČD
- Izvedba retrospektive iteracije 1h   1ČD

Suma: 80h
40ČD



2. iteracija:
Obdelava .shp datotek kot predpriprava za izvajanje algoritma. 3h  2ČD
Izvedba okrnjenega algoritma planiranja s pomočjo PyVRP. 15h  7ČD
Izdelava simulacije naključnega nabora voženj po mestu - kot merilo uspešnosti algoritma pluženja. 15h   8ČD
Home page UI: vsebuje zemljevid stanja cest, login 5h   2ČD
avtentikacija Admin-a in Ustaljenih Plugov 8h    4ČD
Admin UI - na zemljevidu vidi lokacije Ustaljenih Plugov. Ob kliku nanje dobi njihovo telefonsko številko. 8h   4ČD
Admin lahko ureja lahko število plugov v štartni bazi in kje so štartne baze. 7h   3ČD
Admin dodajanje Ustaljenih Plugov v podatkovno bazo. 10h   5ČD
Ustaljeni Plug GPS sharing - vsi aktivni Ustaljeni plugi delijo svojo lokacijo z Adminom. 15h   7ČD
Ustaljeni Plug UI - glede na trenuten GPS se mu izpisujejo navodila za nadaljno pot. 15h   7ČD
Ustaljen Plug ima možnost deaktivacije - takrat se ve, da ne pluži (recimo malica ali odmor). 4h   2ČD
Začetni razvoj lastnega algoritma organizacije pluženja na podlagi hevristik 12h 6ČD

Testiranje enot. 8h   4ČD
Dokumentiranje kode. 6h   3ČD
Preurejanje programske kode (refactoring). 10h   5ČD
Organizacija projekta. 5h   2ČD
Planiranje naslednje iteracije 5h   2ČD
Izvedba retrospektive iteracije 3h   2ČD

Suma: 117+37 = 154h
57+18=75ČD


3. iteracija:
Samostojni Plug UI - vidi trenutno nalogo (kater zahtevek za pluženje naj trenutno opravlja) 5h  3ČD
Customer registration UI 5h   2ČD
Registracijska funkcionalnost 8h   4ČD
Customer UI za oddajanje zahtevkov za pluženje 5h   2ČD
Zaledna funkcionalnost zahtevkov za pluženje 7h   3ČD
Nadaljnji razvoj algoritma organizacije pluženja. 40h   20ČD
Manager UI - vidi lokacije Samostojnih Plugov. Ob kliku nanj dobi njihovo telefonsko številko. Usmeri jih na opravljanje naročila, ki so mu blizu. 12h   6ČD
Vključitev kmetov v pluženje z VOC in Zelenice. To za sabo potegne potrebo po bolj zapletenem algoritmu. 15h   8ČD
Home page poizvedba kdaj bo neka ulica splužena. 20h   10ČD

Integracijsko testiranje komponent prve in druge iteracije. 8h   4ČD
Testiranje enot. 8h   4ČD
Dokumentiranje kode 7h   3ČD
Preurejanje programske kode (refactoring). 12h   6ČD
Izvedba retrospektive iteracije 3h   2ČD
Organizacija projekta. 5h   3ČD
Planiranje naslednje iteracije 6h   3ČD

Suma: 117+49=166h
58+25=83ČD

Olajšana verzija:
Razvoj plužnih zahtevkov 20ČD
Nadaljnji razvoj algoritma 28ČD
Home page poizvedba spluženosti ulice 10ČD
Testiranje in dobre prakse 17ČD
Organizacijsko delo 8ČD


4. iteracija:
Neregistriran uporabnik lahko deli svoj GPS in pove cilje (služba) in mu povemo po kakšni poti naj gre, ker je že splužena. 30h   15ČD
Nadaljnji razvoj algoritma organizacije pluženja. 40h   20ČD
Posodobitev pomembnosti posameznih cest glede na njihovo priljubljenost s strani neregistriranih uporabnikov. 30h   15ČD

Ročno testiranje sistema kot celote. 12h   6ČD
Integracijsko testiranje tretje iteracije s prejšnjima 12h   6ČD
Testiranje enot. 6h   3ČD
Dokumentiranje kode 7h   3ČD
Preurejanje programske kode (refactoring). 12h   6ČD
Organizacija projekta. 5h   2ČD
Izvedba retrospektive iteracije 3h   2ČD
Suma: 100+57=157h
50+28=78ČD

Olajšana verzija:
Planiranje poti neregistriranega uporabnika 30ČD
Nadaljnji razvoj algoritma 20ČD
Testiranje in dobre prakse 24ČD
Organizacijsko delo 4ČD


<!-- end of the list -->
</p>



- Povzetek razdelitve projekta na aktivnosti s seznamom izdelkov, vključno z Ganttovim diagramom in grafom PERT.


![Ganttov diagram](https://teaching.lavbic.net/plantuml/svg/dPBFJy8m5CVl_IjUzA3k8aoNO48C0kB5WmTlXCE3lesoqfBs3LmC_xlTc4IcN4oJTlssd-_xqGqye-CC3JDSl5IBtO9Kc3bSNmZHzrngUXJrXV51Xay1m6fDMXcgDm2luNDajNLmcSRLgDM9DNnG0rS6QL-HwFE66k8YpvmjZ6nOwgL9AjkEoMJOUnurE3fdTx-ZdjnPAqsUxJ6x_yHPQEj9dZFuiqYjiYKVAzsB_ctJFU5pPJPOzMxUScA7neSZCYoMIXAarlBSVWYD9Yim8_1QY8spAremr8_bWPS4tGTUWarXGdDNe2iXxiJtmYCNJcBfGv-egK7u4AqbYMaKlRaj0kQijiPwZYAuxdP06dKp0_GmVUhEGACFuIevy1KpTaNMWfAVJ7naO4UK0nhvdJHoxNdbWOoilDuTyQgTmOdRtT4jWKC5v-p48CprJ_e5 "Ganttov diagram")


**Ganttov diagram** (izvorna koda :bar_chart: [PlantUML](./gradivo/plantuml/Gantt.puml))


![PERT diagram](https://teaching.lavbic.net/plantuml/svg/bL9DJyCm3BtdLrZR3MsmTUeqGLN1O9mu8DXjx90rRYdD4kHcV8Zjl-Eq7LJJE718ujX-x_b5kIoT9BTPQ-ZSpnxce7APaLntX2YBtBnAZc4bao8Zkp7gscfBu4YQaajedD2OEd0MAC-U7QC94vTRm_14QeJ1wKI8g7IV6cF1KWvlQW7u4W2IoBvN4S1TRh2cNsdMuznEx4Hqrc1RupnwcWerFHYiYvCqJ9MlM598JJQydKvcrypM8b6OoersS_nmLphFp9hDGC8RagW7XKwKUFovabGGglYUtYJ8mkLlnfOkEgkgSGTa2LT3wAOfZd5yeTd77WBd43NvNdF6Mu3X0BRWbm-UpDRRRwVs-ZUqoLgAjL9GaTP6UytfII5iq30CQzRg4bHR-4jwO6fEw5x-j3NwXwtXpm11kBSrQAU4M9mieR_eDZIzbTLgsO_vzGG_ODz7GHKTQHa9TkvRc4FmN4TwV4LSeb7ycxy1 "PERT diagram")


**Graf PERT** (izvorna koda :bar_chart: [PlantUML](./gradivo/plantuml/PERT.puml))


### 6.3 Finančni načrt
Časovno zahtevnost izdelave aplikacije bomo ocenili s pomočjo modela COCOMO 2 za zgodnji model načrta.

Pri tem bomo za izračun uporabili sledečo formulo:

$$ effort_{ČM} = A * size^B * M $$

kjer bomo dobili rezultat v človek-mesecih.

Za parameter A bomo privzeli vrednost 2,94.

#### 6.3.1 Ocena obsega aplikacija
Velikost aplikacije ocenimo tako, da jo razdelimo na funkcionalnosti in vsaki od njih določimo utež glede na njen obseg. Tipi funkcionalnosti so sledeči:
- Zunanji vhod (External Input - EI)
- Zunanja poizvedba (External Query - EQ)
- Zunanji izhod (External Output - EO)
- Notranja logična datoteka (Internal Logical File - ILF)
- Zunanja vmesniška datoteka (External Interface File - EIF)

| Vrsta FP | Ime funkcionalnosti | Obseg | Utež |
|----------|---------------------|-------|------|
| EI       | Prijava v sistem						| LOW | 3
| EI       | Zahteva za predviden čas prihoda		| LOW | 3
| EI       | Zahteva za izračun plužnih poti		| AVG | 4
| EI       | Posodobitev podatkov o voznem parku	| LOW | 3
| EI       | Oddaja naročila za pluženje			| LOW | 4
| EI       | Potrditev naročila za pluženje			| AVG | 3
| EQ       | Prikaz stanja na cestah				| LOW | 3
| EQ       | Izpis podatkov o določenem plugu		| LOW | 3
| EQ       | Izpis naročil za pluženje				| LOW | 3
| EO       | Izračun optimalnih plužnih poti		| AVG | 5
| ILF      | Interna podatkovna baza				| LOW | 7
| EIF      | Baza vremenskih podatkov				| LOW | 5
| EIF      | Baza geografskih podatkov				| LOW | 5
| vsota ||| 51

Pri implementaciji bomo večinoma uporabljali jezik JavaScript, za katerega velja, da ena funkcijska točka ustreza približno 47 vrsticam izvorne kode. Izračunani obseg je torej
$$ size = 51 * 47 = 2.397 KSLOC $$

#### 6.3.2 Parameter B
Parameter B izračunamo iz 5 dejavnikov, ki opisujejo lastnosti projektne skupine.

| Dejavnik | Opis | Vrednost | Utež |
|----------|------|----------|------|
| PREC	   | Stopnja precedenčnosti 			 			 | zelo nizka | 5
| FLEX	   | Stopnja fleksibilnosti zahtev 		 			 | visoka 	  | 2
| RESL	   | Stopnja pripravljenosti na tveganja			 | nominalna  | 3
| TEAM	   | Stopnja uigranosti skupine 					 | nominalna  | 3
| PMAT	   | Zrelostni nivo razvojnega procesa po modelu CMM | zelo nizek | 5
| vsota    |      |			 | 18

Vrednost B je za naš projekt torej enaka
$$ B = 1.01 + 0.01 * 18 = 1.19$$

#### 6.3.3 Parameter M
Parameter M izračunamo iz 7 dejavnikov, ki dodatno vplivajo na trud, ki bo potreben pri razvoju aplikacije.

| Dejavnik | Opis | Vrednost | Razpon uteži | Utež |
|----------|------|----------|--------------|------|
| PERS     | Stopnja usposobljenosti članov ekipe | nominalna | 1.5 - 0.5 | 1.0
| PREX     | Stopnja izkušenosti članov ekipe z uporabljeno tehnologijo | nizka | 1.5 - 0.5 | 1.2
| RCPX     | Ocena kompleksnosti projekta | visoka | 0.5 - 1.5 | 1.2
| RUSE     | Potreba po izdelavi komponent, namenjenih za ponovno uporabo |zelo nizka | 0.5 - 1.5 | 0.5
| PDIF     | Kombinacija spremenljivosti platforme in potrebe po učinkovitosti | nizka | 0.5 - 1.5 | 0.7
| *SCED*   | Krčitev/raztezanje predvidene porabe časa ||| 1.0
| FCIL     | Kombinacija razpoložljivosti razvojnih orodij in komunikacijskih sredstev | zelo visoka | 1.5 - 0.5 | 0.7
| produkt |||| 0.3528

Vrednost M je za naš projekt torej enaka
$$ M = \prod{dejavnik_i} = 0.3528 $$

#### 6.3.4 Končni izračun časovne zahtevnosti

Vrednosti *A*, *size*, *B* in *M* vstavimo v formulo za izračun:
$$ effort_{ČM} = 2.94 * 2.397^{1.19} * 0.3528 = 2.94 ČM $$

Ocena časovne zahtevnosti za naš projekt je torej približno **2,94** človek-mesecev dela.

#### 6.3.5 Finance

| Strošek		 | Cena |
|---------		 |------|
| Delo			 |
| Elektrika		 |
| Kosila		 |
| Pijače		 |
| Kava			 |
| Potni stroški	 |


## 7 Ekipa


### 7.1 Predznanje


Ekipo sestavljamo štirje študenti 3. letnika univerzitetnega programa Fakultete za računalništvo in informatiko. Izkušenj z realnimi projekti imamo koolektivno bolj malo. Tudi naše znanje spletnega programiranja ni na zavidljivem nivoju. To bomo poskusili nadoknaditi z večjim interesom in zagnanostjo.

Matevž Vidovič vešč programer v Python-u, s spletnimi tehnologijami pa nima veliko izkušenj. Zanimata ga tako backend kot frontend, zato glede tega nima preferenc. Razvijanje algoritma pluženja se mu zdi zanimiv izziv za katerega že ima nekaj idej.
Filip Gros je moralni steber naše ekipe. Izkušen programer umetnega zaznavanja v programskemu jeziku Python bo poskrbel za celovino povezanost aplikacije. Poleg Pythona je vešč tudi v jezikih Go, Java, C.
Jošt Eržen je izkušen programer pri večjem projektu v programskemu jeziku Java, prav tako pa ima nekaj znanja v programskih jezikih Python, C in JavaScript ter SQL.
Sebastjan Kordiš - naš strokovnjak matematike bo poskrbel za optimalne algoritme. Ima izkušnje programiranja v programskih jezikih Python, Go, Java, C ter Javascript.


### 7.2 Vloge


Pri našem projektu bomo vsi člani razvijalci. Poleg vloge razvijalca pa bo Matevž Vidovič zaradi njegove predhodne komunikacije z stranko prevzel vlogo lastnika izdelka, Filip Gros pa bo prevzel vlogo SCRUM voditelja.


## 8 Omejitve in tveganja


### Matrika izpostavljenosti tveganj:
Ustvarjamo aplikacijo, katere nedelovanje lahko povroči popolen prometni kolaps, kar ima velik vpliv na veliko število ljudi. Prav tako je etično problematično, da s tem onemogočimo urgentne zdravstvene prevoze, ki so lahko za ljudi usodni. Do tega ne sme priti, zato usodne napake niso dopustne niti v primerih z zelo nizko verjetnostjo.

Na drugi strani manjše napake v sistemu niso tako hude - nihče ni tako zelo odvisen od podatkov sistema, da bi manjša napaka imela trajne posledice, zato je leva stran tabele lahko bolj zelena.

![Matrika izpostavljenosti tveganj](./Gradivo/img/Tabela%20tveganj.PNG)


### Družbene, etične, politične in pravne omejitve

- Potrebno se bo pozanimati o zbiranju osebnih podatkov, na primer za lokacijo, ter uporabnike obvestiti o zbiranju ter uporabi teh podatkov pri ponudbi storitve.
- Če v aplikaciji pride do napake in to povzroči prometni kolaps je to lahko etično sporno, sploh recimo v primeru onemogočenih urgentnih zdravstvenih prevozov. Preveriti moramo tudi našo pravno odgovornost v tej situaciji - če je edini razlog za kolaps prav težava v naši aplikaciji, smo morda lahko za to odgovorni.
- Pogledati si moramo, kako bomo obravnavali povezovanje kmetov s strankami - če bo plačilo potekalo preko nas moramo za to pridobiti ustrezna dovoljenja in pravne nastavke. Če prepustimo, da plačilo izvedejo sami, je lahko etično sporno, če je s tem omogočena siva ekonomija.

### Opredelitev tveganj in strategij njihovega obvladovanja


#### Tehnologija:

##### Ime in oznaka: ARSO API (T1)
- Verjetnost: Majhna
- Učinek: Dopusten
- Izpostavljenost: Srednja

- Opis tveganja: Ob izgubi dostopa do podatkov ARSO bi izgubili možnost napovedovanja vremenskih pogojev.

- Vpliva na: Izdelek, Posel

- Strategija obvladovanja: Strategija zmanjševanja.
- Opis obvladovanja: Sistem mora biti na to pripravljen in v tem primeru vseeno delovati, četudi manj precizno. Recimo celotnemu Celju pripisati neko konstantno padanje snega glede na zadnje podatke, ki jih imamo.



##### Okvara transponderja (T2):
- Verjetnost: Visoka
- Učinek: Dopusten
- Izpostavljenost: Srednjevis.

- Opis tveganja: Obstaja možnost okvare transponderja (recimo da telefonu zmanjka baterije), v temu primeru ne bi imeli informacij o danemu plugu

- Vpliva na: Izdelek

- Strategija obvladovanja: Strategija izogibanja
Opis obvladovanja: Za obvladovanje zahtevamo od uporabnikov, da imajo polne telefone in da imajo na voljo power bank. Morda celo nek poceni rezervni telefon. Če tudi ta ne deluje, naj se vrnejo v bazo.



##### Algoritem (T3):
- Verjetnost: Zmerna
- Učinek: Resen
- Izpostavljenost: Srednjevis.

- Opis tveganja: Zaradi pomanjkanja znanja o tem tipu algoritmov nismo sposobni razviti približno optimalnega algoritma.

- Vpliva na: Projekt, Izdelek, Posel

- Strategija obvladovanja: Strategija zmanjševanja
- Opis obvladovanja: Izvedli bomo okrnjeno neoptimalno verzijo algoritma, za kar bomo kompenzirali z boljšo spletno aplikacijo in uporabniško izkušnjo. Dodelane ideje za relaksirane vrste algoritma že imamo, zato smo v to opcijo sigurni.

##### Geografske datoteke (T4):
- Verjetnost: Zelo majhna, Majhna, Zmerna, Visoka, Zelo visoka
- Učinek: Neznaten, Dopusten, Resen, Visok
- Izpostavljenost: Nizka, Srednjeniz., Srednja, Srednjevis., Visoka

- Opis tveganja: Nismo še delali z geografskimi datotekami, kar bi lahko povzročilo težave, saj ne vemo, kaj so optimalna orodja zanje - tako bi lahko zašli v suboptimalna orodja, kjer bi že zgradili velik del kode.

- Vpliva na: Izdelek

- Strategija obvladovanja: Strategija izogibanja
- Opis obvladovanja: Že v prvi iteraciji bomo poskusili narediti osnovno rokovanje s temi datotekami in se pozanimati o optimalnih orodjih za delo z njimi. Tako se verjetnost kasnejših težav zmanjša. Dober začetni projekt je vizualizacija podatkov ter njihova pretvorba v človeku berljivo obliko.

##### Nepreverjenost PyVRP (T5):
- Verjetnost: Majhna
- Učinek: Neznaten
- Izpostavljenost: Nizka

- Opis tveganja: Nihče v ekipi še ni delal s knjižnico PyVRP. Izkazalo bi se lahko, a ni preveč uporabna, ali je polna hroščev.

- Vpliva na: Projekt

- Obvladovanje ni potrebno: Ker je knjižnica javna, je pogosto uporabljana in zato verjetno že nekoliko testirana. Poleg tega ni naša edina ideja za izvedbo algoritma in njena neuporabnost ni tako kritična.



#### Orodja:
##### Github merging(T6):
- Verjetnost: Zelo majhna
- Učinek: Dopusten
- Izpostavljenost: Srednjeniz.

- Opis tveganja: Ker še nismo sodelovali pri večjih projektnih nismo vešči pri uporabi sistema Git, še posebej ne pri merge-anju v situacijah, kjer smo nespretno delali z Git-om (ne pull-ali pred commitanjem; ne odprli svojega brancha, čeprav bi to bilo potrebno; ustvarili preobsežen commit).

- Vpliva na: Projekt

- Strategija obvladovanja: Krizni načrt
- Opis obvladovanja: V primeru incidenta se bomo takoj obvestili ter priskočili na pomoč. Ker smo majhna ekipa bi to moralo zadostovati za premostitev težav.


##### SCRUM težave (T7):
- Verjetnost: Zmerna
- Učinek: Dopusten
- Izpostavljenost: Srednja

- Opis tveganja: SCRUM ne uspe najbolje in se aktivnost na kritični poti podaljša.

- Vpliva na: Projekt

- Strategija obvladovanja: Strategija izogibanja
- Opis obvladovanja: Developerji bomo glede aktivnosti na kritični poti s SCRUM master-jem pogosteje komunicirali, da lahko ta dodeli dodatno pomoč, če se aktivnost zavleče.



#### Ljudje:

##### Kljužni razvijalec (T8):
- Verjetnost: Zmerna
- Učinek: Dopusten
- Izpostavljenost: Srednja

- Opis tveganja: Jošt zaradi bolezni ali drugega razloga za odsotnost ni na voljo. Kot najbolj izkušen s programiranjem backenda njegova odsotnost pusti velik primankljaj v tej vrsti del, kar vpliva na kritično pot.

- Vpliva na: Projekt

- Strategija obvladovanja: Strategija zmanjševanja
- Opis obvladovanja: Poskusili bomo z deli na backendu opraviti čim prej ter si frontend-ovske aktivnosti pustiti za kasneje. Tako bomo v primeru Joštove odsotnosti imeli blazino aktivnosti, na katerih lahko delamo s polno paro v času odsotnosti in tako ni vpliva na kritično pot.


##### Specifična tehnologija (T9):
- Verjetnost: Majhna
- Učinek: Resen
- Izpostavljenost: Srednjevis.

- Opis tveganja: Ob razvoju odkrijemo potrebo po uporabi bolj specifične tehnologije, ki pa je ne znamo uporabljati in osebno ne poznamo osebe, ki bi nam lahko svetovala.

- Vpliva na: Projekt

- Strategija obvladovanja: Krizni načrt
- Opis obvladovanja: Pristopimo do profesorja ali asistenta, ki se spozna na to področje ter nas usmeri na učne materiali, s čimer lahko prebrodimo svoj problem.



##### Bolezen (T10):
- Verjetnost: Zmerna
- Učinek: Resen
- Izpostavljenost: Srednjevis.

- Opis tveganja: Kot ekipa le 4 članov obstaja večja možnost, da zboli večji del ekipe (2 ali 3 bolni predstavlja večjo ustavitev sposobnosti, kot bi pri ekipi 5 članov). To bi lahko močno zamaknilo kritično pot.

- Vpliva na: Projekt

- Strategija obvladovanja: Strategija izogibanja
- Opis obvladovanja: Poskusili bomo čim bolje ohraniti svoje zdravje. V primeru tudi blage bolezni oseba ne bo prišla na sestanek, saj bi okužba še enega člana pomenila ogromen izpad v projektu.


#### Organizacija:

##### Cena host-anja (T11):
- Verjetnost: Zmerna
- Učinek: Dopusten
- Izpostavljenost: Srednja

- Opis tveganja: Za hostanje potrenujemo denar, ki nam ni na voljo, kar oteži izdelavo izdelka.

- Vpliva na: Posel

- Strategija obvladovanja: Krizni načrt
- Opis obvladovanja: Profesor je omenil, da bi se v takšnem primeru dalo prositi za povračilo stroškov. Sicer pa bi lahko poiskali znanca, ki bi nam lahko storitev priskrbel po nizki ceni.


##### MOC rez v proračunu (T12):
- Verjetnost: Zelo majhna
- Učinek: Usoden
- Izpostavljenost: Srednjeniz.

- Opis tveganja: MOC zaradi rezov v proračunu prekliče projekt.

- Vpliva na: Posel

- Strategije obvladovanja ne definiramo. Izpostavljenot je zaradi nizke verjetnosti dovolj nizka.



#### Zahteve:

##### Sprememba zahtev (T13):
- Verjetnost: Majhna
- Učinek: Resen
- Izpostavljenost: Srednjevis.

- Opis tveganja: MOC vmes spremeni zahteve do te mere, da je dotedanja koda neuporabna.

- Vpliva na: Projekt

- Strategija obvladovanja: Strategija izogibanja
- Opis obvladovanja: Že med iteracijami bomo poskusili preveriti, če gremo v pravo smer in če se rešitev ujema z njihovimi zahtevami.

##### Algoritem slabši od trenutnega sistema (T14):
- Verjetnost: Visoka
- Učinek: Resen
- Izpostavljenost: Srednjevis.

- Opis tveganja: Razvit algoritem je slabši od obstoječega sistema pluženja. To se lahko hitro zgodi, saj je težko modelirati vse majhne dejavnike, ki jih domenski eksperti posedujejo.

- Vpliva na: Posel

- Strategija obvladovanja: Strategija izogibanja
- Opis obvladovanja: Sprogramirali bomo simulacijo vožnje po mestu v določenih razmerah pluženja. Skozi celoten proces bomo primerjali rezultate ob pluženju nastavljenem po metodi ostrega očesa, z rezultati našega trenutnega algoritma. Tako bomo bolje vedeli, da razvijamo v pravi smeri.


#### Ocenjevanje:

##### Precenitev sposobnosti (T15):
- Verjetnost: Majhna
- Učinek: Resen
- Izpostavljenost: Srednjevis.

- Opis tveganja: Hudo smo precenili trajanje aktivnosti razvoja spletne aplikacije zaradi slabe ocene svojega znanja.

- Vpliva na: Projekt

- Strategija obvladovanja: Krizni načrt
- Opis obvladovanja: Zmanjšali bomo nabor funkcionalnosti, ki jih imamo namen implementirali, ter povečali komunikacijo, saj vsaj nekdo o tej stvari ve nekoliko več.

#### Varnost:

##### Scam uporabniki (T16):
- Verjetnost: Zelo majhna
- Učinek: Dopusten
- Izpostavljenost: Srednjeniz.

- Opis tveganja: Registracija ljudi, ki namerno želijo škodovati sistemu z veliko količino zahtevkov.

- Vpliva na: Izdelek

- Strategija obvladovanja: Strategija zmanjševanja
- Opis obvladovanja: Omejimo število zahtevkov, ki jih uporabnik lahko odda.


