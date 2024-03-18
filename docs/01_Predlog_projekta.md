
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
- imeti dostop do zemljevida stanja spluženosti cest, da lahko preverim razmere.
- imeti možnost registracije, da lahko postanem Stranka.

Glede na to, da sem neregistriran uporabnik:
- ko zahtevam možnost registracije, sem preusmerjen na stran ki mi to omogoča.

Kot Administrator želim:
- na zemljevidu videti lokacije Ustaljenih Plugov, da imam pregled nad izvajanjem pluženja.
- ob kliku na Usataljeni Plug dobiti njihovo telefonsko številko, da ga lahko kontaktiram. 
- imeti možnost urejanja števila plugov v štartni bazi in lokacije štartnih baz, da se podatki v zaledju spremenijo v realnem času.

Glede na to, da sem admin:
- ko kliknem na Ustaljeni Plug na zemljevidu, dobim njegovo telefonsko številko.
- ko zahtevam urejanje števila plugov v štartni bazi in lokacije štartnih baz, se te podatki posodobijo v roku 1 minute po oddani zahtevi.

Kot Ustaljeni Plug želim:
- da se mi glede na trenuten GPS izpisujejo navodila za nadaljno pot, da sledim optimalni poti pluženja.
- imeti možnost deaktivacije, da se lahko umaknem iz pluženja (zaradi malice, okvare, premora).

Glede na to, da sem Ustaljeni Plug:
- ko zahtevam deaktivacijo, je ta objavljena v roku 30 sekund.


Kot Stranka želim:
- imeti možnost oddaje zahtevka za pluženje, da lahko s tem naročim pluženje snega za zasebnem zemljišču.

Kot Samostojni Plug želim:
- videti trenutno nalogo, da se lahko odpeljem do nje in jo opravim.

Kot Manager želim:
- videti lokacije Samostojnih Plugov in ob kliku na dotičen plug dobiti njegovo telefonsko številko, da ga lahko kontaktiram.
- imeti možnost usmeriti dotičen Samostojni Plug na zemljevidu na določeno opravilo, da se mu posodobi trenutno opravilo.

Glede na to, da sem Manager:
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

![Opis sistema](https://teaching.lavbic.net/plantuml/png/ZLNDRXen4BxxAKPSQ0zGgSUeQeKsbH8f5CG6L8NaCB2ZhTcrlV9wgKALHyWhzTI-L-tzPrb8EI3ccx_FCvzD6d6Pe4O1MoKI9KaQtpp719c8FpA6MwCq3DJcpolA0M0A2wy29MhrvrNoACUzkLyvzkfWKKZYBCJSvy-l6r-mG-Vw-riIy8CWIHy4IWn9vx5JVrx5OY1uqNJ2XYLso2JA7OUJ7W-hEMCiG8CRJ0a6AqssTXfnI9H58_uetrMO9Q1IWvQ8H_6EtW_W5mFxMU-xIK_ifLtqWOIDt_E0rochcVTK_7gWc2JVKcbEPnu8J0fhkBucWpoc0AOEEwgwJ4cdHS7r98uXSxQBIN0RsS70m9Vg9ynZ-xLGcI6O9OOBVa33bGJ_EJKaNBujKASiRskADqeGp2rQChjJ8PVbxssM6klMiBmjaN8P3H1elc_R4xUMnbnGo2q1xSmNHs42ez7dJjU5rmDQMVIWLW0zg9KNZCV7g8M7qwL_3pUJrTSXEpffKQBDxSHPZe7L4odWvhXmTIIpLc3Ef3Ke6rbQtMhri6n8hcVBHwEJSkgOYPEgxONOdFgIGQgCveRshOHFUOT6CUrjbEqRf_Cw2Nt3FGyBvM0SAblpXt2bHjRlT3QJ2uM1lRIazqxD0En810NDyvMk85OHRlaEEtcknSMyH1dMrbTnXBCPdTYJKRJtSxcIw-tUGB8JPgsh2wCiSObzO-aeAZzSx_Yku52z6l0emMYIcP4K8jWdI1PJgf-EgkF5Gxidvxy2U_daJ7iUkdpFG_zcjhoxRcvKUuZruhaCOQQ3Qj17aZqNr87ULf4ArCREIfLNWCSgl_1UpGz64DcLxGWYPI1mvv3L7mFlhcSyXlKz5tJFuzXrdMWdpFQMCesTf9pYvQGem1ri57o7DFzF8_d55RcKb5CvfwWt4y_l-uNz0m00 "Opis sistema")
*P.S. s črtkano črto so označene neobvezne ali pa priporočkjive razširitve sistema

Predstavitev sistema glede na diagram:
Na zgornjem diagramu je površinsko predstavljen sistem, ki ga želimo implementirati. Sistem lahko razdelimo na “Front-End”, ki je predstavljen v paketu UI, ter “Back-end”, ki obsega 2 glavna modula.
- SnowOnRoads Service predstavlja podatke, ki na zemljevid mestne občine Celje proecira višino snežne odejo na vsaki izmed cest. Upošteva, kdaj se je nazadnje peljal mimo plug, kjer ob njegovem mimohodu ponastavimo višino snega na 0 cm.
- Plow navigation algorithm pa je srce našega problema. Na podlagi stanja snega, prestavljenega z zgoraj opisanim servisom, izračuna najoptimalenjšo pot pluženja za vsakega voznika podjetja VOC in Zelenice. Izračunano pot pošlje vozniku. Le administrator lahko vpliva na parametre algoritma (predstavljene v manager UI). Algoritem upošteva vnaprej določeno prioritetno lestvico cest, kar v grobem pomeni da bodo državne, regionalne in medkrajvne ceste prej splužene kot stranske ulice. Ob intenzivnem sneženju se lahko zgodi, da bodo te ceste splužene večkrat, medtem ko bodo nekatere stranske ulice ostale nedotaknjene.
- Plowing orders so ena izmed možnih razširitev sistema, ki jih sistem po našem mnenju naj bi vseboval (Should have). Občan, ki se je registriral, lahko postane naročnik storitev pluženja. Ko se odloči, pošlje povpraševanje po storitvi. V najkrajšem možnem času mu vodja plužne izmene (manager)odobri ali zavrne storitev. Če je povpraševanje odobreno, se vključi v Plow navigation Algorithm, ali pa se direktno dodeli vozniku pluga, če ta nima trenutno aktivne poti pluženja. 
- TimeTillPlowArrive Service implementira funkcijonalnost povpraševanja po času, kdaj se željena ulica spluži. To ugotovimo na podlagi oddaljenosti plugov od ulice in njihovih plužnih poti. Je ena izmed opcijskih razširitev sistema (Could Have). 


Sistem je v osnovi zastavljen, da zadosti štirim ciljnim množicam.
- Občan predstavlja “navadnega” uporabnika (regular user). Ima dostop do zemljevida, na katerem je predstavljena trenutna snežna odeja na cestnem sistemu MOC
- Naročnik je vsak občan, ki se je registriral. Lahko oddaja povpraševanja po storitvi pluženja. 
vodja plužne izmene ali manager povpraševanja odobri ali pa jih zavrne. Ima pregled nad strenutnin stanjem, vključno z lokacijami plugov. Ob kliku na vsak plug, se mu razširi njegova entita. Tam so prikazani vsi koristni podatki o plugu in vozniku. 
- Voznik pluga je zaposleni pri podjetju VOC ali Zelenice. Ob možni nadgradnji sistema je lahko to tudi kateri izmed lokalnih - - kmetov ali drugih oseb, ki imajo v privatni lasti mehanizacijo zmožno pluženja. Njigova glavna naloga je da plužijo po zagrtani poti.
- Admin predstavlja le en administrativni profil, ki ima vso moč nad sistemom.

## 5 Predlagan pristop

Uporabnik bo obiskal spletno stran projekta. Pokazal se mu bo zemljevid mestne občine Celje, kjer bo na vsaki cesti z barvo označeno koliko je zasnežena. Glede na njegovo vlogo (voznik pluga/manager/administrator..) mu bodo ponujene dodatne možnosti in razširitve, ki pa bodo vplivale na izračun idealne poti pluženja za dano situacijo. Sistem bo skrbel, da bodo te poti čim bolj učinkovite, to pomeni čim hitreje, čim večim ljudem plužiti cesto in omogočiti kar se da tekoč pretok vozil po cestah. 
 
Za razvoj algoritma za iskanje poti bomo uporabili knjižnico PyVRP (Python vehicle routing problem)
V Pythonu bomo napisali skripte za pripravo podatkov za PyVRP in naključne tstne primere.
JavaScript bo poganjal background procese naše spletne strani. Spletni strežnih bo temeljil na Djangotu (odprtokodni Pythonovi rešitvi). S pomočjo SQL poizvedb in uporabe MongoDBja bomo poskrbeli za implementacijo databasa Useres. Razmišljali smo, da bi za frontend uporabili programski jezik React.
Za delo z zemljevidom bomo uporabili nekaj APIjev, podprtih s strani Googla za uporabo v Google maps.

Komunicirali bomo s skupino preko Discorda in v skrajnih primerih po telefonu. Za nadzor verzij in vsem dostopno implementacijo projekta bomo uporabili GitHub. Za prvi izziv bomo markdown dokument urejali v Google Docs. 

Ob pisanju kode si bomo pomagali z umetno inteligenco, najverjetneje ChatGPT in GitHubCopilot.
 
Teste enot bomo pisali sami ali pa s pomogčjo AI. Kolikor bo šlo, bomo avtomatsko izvajali teste integracije. Izvajali bomo tudi ročno testiranje sistema kot celote, kjer bomo najprej napisali protokol izvedenih akcij in bo ročno testiranje ponovljivo. V skupini smo se dogovorili, da mora biti vsak del kode, ki se bo zlil (mergal) v main dobro stestiran. Nekaj testov bomo spisali tudi ročno, vendar jih bo večina avtomatsko generiranih. Kot del zagotavljanja kakovosti (QA), bomo drug drugemu testirali implementirane rešitve, saj je to preverjeno dobra praksa. 

Za vsako strategijo bomo preverili njen obseg tesitranja (pokritost funkcionalnih in nefunkcionalnih zadev, pokritev tveganj…) ter število testnih primerov. Še pred vsem bomo pa temlejito peverili kodo, ki bo pisala testne primere, saj si ne želimo testirati na napačnih ali nepopolnih testnih programih. V okviru pregleda literature, si bomo pogledali smernice ISTQB (Mednarodni odbor za kvalifikacije na področju testiranja programske opreme) in standarde IEEE za načela agilnega testiranja. Intuitivnost uporabe aplikacije pa bomo testirali tako, da bomo prosili svoje bližnje, da odigrajo vlogo poskusnega začka.


## 6 Vodenje projekta

#### Dnevnik sprememb:
- 29.2. Začetni nabor idej za možne funkcionalnosti. Zažetek projekta.
- 7.3. Omejitev idej, ki jih želimo podpirati.
- 13.3. Ob stoječem sestanku smo dokončno razjasnili želje uporabniške zgodbe in arhitekturo. Sedaj definiramo potrebovane funkcionalnosti.

#### Izvajani procesi in prakse
Uporabljali bomo SCRUM in Extreme Programing.
Tedensko se bomo dobivali na stoječih sestankih ob tabli pred enem izmed laboratorijev, ki imajo tablo. Začeli bomo s tem, da vsak pove težave zadnjega tedna ter kako daleč je prišel, potem pa skupaj zasnujemo, kaj bomo izdelali v naslednjem tednu. SCRUM master bo naloge razdelil.

V naslednji iteraciji želimo zgraditi glavno stran z zemljevidom, ki prikazuje trenutno snežno stanje na cestah ter osnovno delovanje algoritma. Podpirati želimo začeti osnovne pluge in administratorske dožnosti.

### 6.1 Usklajevanje ekipe

Delo bomo med člane skupine razporedili glede na predznanje članov, da bo vsak dobil naloge, ki jih bo glede na svoje znanje najbolj sposoben rešiti. Člani si bodo naloge sprva izbrali sami, v kolikor pa bodo ostale določene naloge neizbrane, jih bo vodja skupine dodelil članom.
Sestajali se bomo tedensko v živo, v primeru, da to ne bo mogoče, pa prek aplikacije Discord. Ob tabli pred enem izmed laboratorijev bomo izvajali stoječe sestanke.
Med sestanki bomo pregledali stanje našega projekta, ocenili napredek od zadnjega sestanka ter razdelili naloge, ki jih bodo člani ekipe morali opraviti do naslednjega sestanka. Pogovorili se bomo o problemih, ki so se pojavili v zadnem tednu in jih poskusili nasloviti. Začrtali bomo delovanje nadaljnjih funkcionalnosti ter definirali njihovo arhitekturo.


### 6.2 Projektni načrt


**1. iteracija**

|||
|-|-|
|Oznaka               | A1
|Naziv                | Izbira izziva in nabiranja idej
|Datum začetka        | 28. 2. 2024
|Datum konca          | 28. 2. 2024
|Trajanje v ČD        | 1
|Pričakovani rezultati| Seznam idej za rešitev izbranega izziva

|||
|-|-|
|Oznaka               | A2
|Naziv                | Pregled podatkov in začetna vizualizacija
|Datum začetka        | 29. 2. 2024
|Datum konca          | 29. 2. 2024
|Trajanje v ČD        | 5
|Pričakovani rezultati| Izdelan osnovni načrt projekta

|||
|-|-|
|Oznaka               | A3
|Naziv                | Pregled obstoječih rešitev
|Datum začetka        | 1. 3. 2024
|Datum konca          | 4. 3. 2024
|Trajanje v ČD        | 6
|Pričakovani rezultati| Seznam obstoječih rešitev, ki jih lahko uporabimo/prilagodimo

|||
|-|-|
|Oznaka               | A4
|Naziv                | Sestanki definiranja željene rešitve
|Datum začetka        | 5. 3. 2024
|Datum konca          | 5. 3. 2024
|Trajanje v ČD        | 4
|Pričakovani rezultati| Izdelan drugi načrt projekta

|||
|-|-|
|Oznaka               | A5
|Naziv                | Definiranje uporabniških zgodb in funkcionalnih zahtev
|Datum začetka        | 6. 3. 2024
|Datum konca          | 7. 3. 2024
|Trajanje v ČD        | 6
|Pričakovani rezultati| Seznam definiranih uporabniških zgodb in funkcionalnih zahtev

|||
|-|-|
|Oznaka               | A6
|Naziv                | Planiranje naslednje iteracije
|Datum začetka        | 8. 3. 2024
|Datum konca          | 11. 3. 2024
|Trajanje v ČD        | 4
|Pričakovani rezultati| Dogovorjen načrt druge iteracije

|||
|-|-|
|Oznaka               | A7
|Naziv                | Izdelava predloga projekta
|Datum začetka        | 12. 3. 2024
|Datum konca          | 15. 3. 2024
|Trajanje v ČD        | 16
|Pričakovani rezultati| Predlog Projekta

|||
|-|-|
|Oznaka               | A8
|Naziv                | Izvedba retrospektive iteracije
|Datum začetka        | 18. 3. 2024
|Datum konca          | 18. 3. 2024
|Trajanje v ČD        | 4
|Pričakovani rezultati| Seznam morebitnih izboljšav

**2. iteracija**

|||
|-|-|
|Oznaka               | A9
|Naziv                | Implementacija okrnjenega algoritma planiranja s pomočjo PyVRP
|Datum začetka        | 20. 3. 2024
|Datum konca          | 2. 4. 2024
|Trajanje v ČD        | 15
|Pričakovani rezultati| Delujoč algoritem za načrtovanje pluženja

|||
|-|-|
|Oznaka               | A10
|Naziv                | Izdelava simulacije naključnega nabora voženj po mestu
|Datum začetka        | 20. 4. 2024
|Datum konca          | 29. 4. 2024
|Trajanje v ČD        | 8
|Pričakovani rezultati| Delujoča simulacija voženj

|||
|-|-|
|Oznaka               | A11
|Naziv                | Izdelava domače strani
|Datum začetka        | 20. 3. 2024
|Datum konca          | 21. 3. 2024
|Trajanje v ČD        | 4
|Pričakovani rezultati| Delujoča domača stran z zemljevidom stanja cest in prijavno funkcionalnostjo

|||
|-|-|
|Oznaka               | A12
|Naziv                | Izdelava strani administratorja
|Datum začetka        | 25. 3. 2024
|Datum konca          | 28. 3. 2024
|Trajanje v ČD        | 4
|Pričakovani rezultati| Delujoča stran administratorja

|||
|-|-|
|Oznaka               | A13
|Naziv                | Obdelava .shp datotek
|Datum začetka        | 20. 3. 2024
|Datum konca          | 20. 3. 2024
|Trajanje v ČD        | 1
|Pričakovani rezultati| Datoteke v primernem formatu za uporabo

|||
|-|-|
|Oznaka               | A14
|Naziv                | Avtentikacija Admin-a in Ustaljenih Plugov
|Datum začetka        | 22. 3. 2024
|Datum konca          | 22. 3. 2024
|Trajanje v ČD        | 2
|Pričakovani rezultati| Seznam registriranih uporabnikov

|||
|-|-|
|Oznaka               | A15
|Naziv                | Ustaljeni Plug GPS sharing
|Datum začetka        | 29. 3. 2024
|Datum konca          | 2. 4. 2024
|Trajanje v ČD        | 6
|Pričakovani rezultati| Omogočeno zaznavanje lokacije plugov

|||
|-|-|
|Oznaka               | A16
|Naziv                | Ustaljeni Plug UI
|Datum začetka        | 29. 3. 2024
|Datum konca          | 2. 4. 2024
|Trajanje v ČD        | 6
|Pričakovani rezultati| Delujoča stran za voznike plugov, kjer se glede na trenuten GPS izpisujejo navodila za nadaljno pot

|||
|-|-|
|Oznaka               | A17
|Naziv                | Začetni razvoj lastnega algoritma planiranja
|Datum začetka        | 3. 4. 2024
|Datum konca          | 4. 4. 2024
|Trajanje v ČD        | 4
|Pričakovani rezultati| Osnova lastnega algoritma

|||
|-|-|
|Oznaka               | A18
|Naziv                | Testiranje enot
|Datum začetka        | 5. 4. 2024
|Datum konca          | 8. 4. 2024
|Trajanje v ČD        | 4
|Pričakovani rezultati| Aplikacija opravi zahtevane teste

|||
|-|-|
|Oznaka               | A19
|Naziv                | Preurejanje programske kode
|Datum začetka        | 5. 4. 2024
|Datum konca          | 8. 4. 2024
|Trajanje v ČD        | 3
|Pričakovani rezultati| Bolje strukturirana izvorna koda

|||
|-|-|
|Oznaka               | A20
|Naziv                | Dokumentiranje kode
|Datum začetka        | 9. 4. 2024
|Datum konca          | 9. 4. 2024
|Trajanje v ČD        | 2
|Pričakovani rezultati| Izdelana dokumentacija

|||
|-|-|
|Oznaka               | A21
|Naziv                | Planiranje naslednje iteracije
|Datum začetka        | 9. 4. 2024
|Datum konca          | 9. 4. 2024
|Trajanje v ČD        | 2
|Pričakovani rezultati| Dogovorjen načrt tretje iteracije

|||
|-|-|
|Oznaka               | A22
|Naziv                | Izvedba retrospektive iteracije
|Datum začetka        | 10. 4. 2024
|Datum konca          | 10. 4. 2024
|Trajanje v ČD        | 2
|Pričakovani rezultati| Seznam morebitnih izboljšav


**3. iteracija**

|||
|-|-|
|Oznaka               | A23*
|Naziv                | Delo na 3. iteraciji
|Datum začetka        | 10. 4. 2024
|Datum konca          | 7. 5. 2024
|Trajanje v ČD        | 80
|Pričakovani rezultati| Izpolnjeni zadani cilji 3. iteracije


**4. iteracija**

|||
|-|-|
|Oznaka               | A24*
|Naziv                | Delo na 4. iteraciji
|Datum začetka        | 8. 5. 2024
|Datum konca          | 4. 6. 2024
|Trajanje v ČD        | 80
|Pričakovani rezultati| Izpolnjeni zadani cilji 4. iteracije



- Povzetek razdelitve projekta na aktivnosti s seznamom izdelkov, vključno z Ganttovim diagramom in grafom PERT.


![Ganttov diagram](https://teaching.lavbic.net/plantuml/png/dLZjRjf85FtFKuowFxORjRG1gcPNrQekECHTWf7vqBPLXGOym61x1jbZTyEgZv27o8lih-IzzixOu0ySJA9AJJ9Xvfnxvvvpx-HZ8B0lbfW9WLvqvHSU8PlYfO-z5xNQXq3SkEJFclf09rv6_zOG4jGZBcL4_O1G3xvjSvVxw9T5G_vJgvUSYNWLzjt0qa-v4mTEikiJdZjBduVCJlQIYyMxXLqyyTtbfmkzdMp7liz_7ABcFkDHbmI2xzaz1sVkye3OZnrG6gHBboknZ_HdxSER97krmA5iWsNkPeMJX8zP0ByYJDHMr2PemRcOyNzgBcRB42y92jnQRUFpDPaBf2uhG695qFdlOeNu0bsIcHzY_mOrtZPQjG2BqBVnJG1v8aaCjG3G2akrRsTd0v_O6vzkV1oHipFqyZso6VtjEy81-ZQmzCvtvE80q60TTgijvtL41V7ndAxnsTdBndbcYp7IhVFTdYRwGOW3aCpUaSOYEVRN015ObkSPsndrCQBRBOtW2qCComMs9WXoiPQiSX1VFncMjiCuHt5KZq8aGIvTkCSDjx5meBO1P8llRubW64Lq6sANRfDuyc1mKBUNPg4SBM6KuWqPZ_Ry4QGNwd23aOEmk-G-5LueSHePd67Vd6Zzp_eEgF5OM8hDOMHy1X1hSdzBLyWd3tTmGL4H8zazjVIXtl_yLAGXY0apXoARB2XJzuFHmt_4NHEGM8mPbr0sVqDzEDBwVncLrvLbbe9szbW4XHlkuncZ3tSE1BbTSdicxt4HCcTEESCkayjuLH9vHxyq-d15bGdUqyra63IOC60uW5ohUqtgdnpakAUT19HbT7YRDdT23yoW7299LiTiFmV3sDh4nI2q3IZVvKlv3LIE8rJjjt92w-WzRRANMkletKawMPI8s3CCTI5y7cpWU1eLqfOj4qiVMMQkHWurbf19CIoo9Nx4e28nEpZG-7hqk1WmEKiUriYP6ZfqjKQ5gyNEbxErE0NSyPdK26Hw9t_8-QwgC0h0bZn-VxlcQ70piGOgbBVP2_y2g_jetfPRK0PTWd-DtOqY7syZlbQR2nIu3_qyjZq2V4BGigG3ZWWswU8bHIiIIUkYJh44s-FXoBoUQhskQHcZg-iABr7yCxdUbs10lT2D2J3ikElm_bQHX0O0MaSHLvo03_B0VKBq6ZbSmFS-TJaAeQmUxXW7Whd49e58pXTP9pAknprjP9Zz7TkBap9fpXAozM2rWHs22-8e7fkqTM8m7cXW4LuhezZJER33gy4K13Eew2S52bVSWnkIOy3O-0D50Pc50B8b7dXlHDLMUNDpoD4h19Ach7XXL-QrFXretGfNAW9haG0NeevI1T9iZxBNgaEFOPCqVd3SWHikULGCL1kFhlJ-o6ZdCbuURaekWoon85muzpM4vEoh5B1UeOSxo3u42fqyWc4AJBzUh-UlM-jS6_tfs3XkNWMQAVu-G1KVwWw6A5XXdx8by8a2g3ZfQF3hz8EIdEoEBWKb1o0wlYFEqJPE7lVgCb7D34yuUJgyqYoZtqqDffJgBg17IOuDu2RxXrGJp9I4XN1zCNU2l10AT4C3A1qWn734RUggkcNOXcCO1vr1_NWWEYagY4J5g3B_PeEZBIbo7_J6tKoAJ-OzWa9DMYfXNDIBrJhk6wFf25hnyMezSA7Ct90qq0J5uJQf5qkqRNRqR1CjBywKIwvDXpw9fGxDKpw70YT6GIzzii1pmMMf_7OGcQLVQksHcRtj9yTMFP3akmTC9DE-_lVeU9nPPazguyKkVW9MIYdJ59h51dnHQC3DLCgFDk16XliaRYXo4aQEHuGoYrrx0Fj44xCjlUmhSK52Sr8SVourwrgtXiSDf0XgnUrMol-KRgjkgrNUMVSvR3srGYoO9a3E8fLP06sS00lPjkR4XHPMZ7RuPJZIhtEggyGjcofpe-iZk8r3tCfXDillILeuBzF2j3FHZzTeXbUL7C1fnRfgk5MmayQ9mb3yCk9eLOcZLHH7MQ4sCw7qOK3qHV9C1UEdY15uVL0_43w5f7hxzvR3lU8ibMbQqt4V7W3L8rKUMpMSzNuwhPA9zD54b6CBEhOrxUYJVIhVFwLWUC1jFbEc06CtyMRn0BdX0VR8LWuqSenAsoYmNF68oqSysCbCjblOSD1CB5FhJ0Vc04PCKEENuzUS3I9poQV8jdv4jrDpebjQhtTSlqMccUfcWYnLZGLEZaQnmEMJ1VeV3DzhwXq-6_iZlMkfWUe4EtcSJjcKq2gR4gRDvqAKZ0a7JvraIaX16iVdX6dpn4dXz57XUTXcAgNqZQzWtkN-cc1-rjjGErO6fd94o06TC2GqI-tmMO2rZ_2_-alq_m00 "Ganttov diagram")


**Ganttov diagram** 

![PERT diagram]( "PERT diagram")


**Graf PERT** 


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

| Strošek		     | Cena v € |
|----------------|----------|
| Delo			     | 8400
| Elektrika	     | 250
| Kosila		     | 1400
| Pijače		     | 560
| Kava			     | 200
| Potni stroški	 | 370
| Skupaj         | 11180


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


