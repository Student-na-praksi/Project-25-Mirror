# Celovita rešitev organizacije pluženja

### Jošt Eržen, Filip Gros, Sebastjan Kordiš, Matevž Vidovič

## 1 Uvod

Tretja iteracija je temeljila na pisanju kode ter opisu sistema.
V dokumentu predstavimo:
večje spremembe projekta, do katerih je prišlo v zadnji iteraciji (razdelki 1, 2 in 3)
diagrame opisa sistema (razdelek 4),
stanje projekta (razdelek 5)
in stanje ekipe in ovrednotenje procesa dela (razdelka 7 in 9).

### 1.2 Poudarki

Cilj je bil vzpostaviti spletni sistem za prikaz stanja cest, navigacijo plugov, ter upravljanje z zahtevki za pluženje. Osnove sistema smo uspešno postavili, a je razvoj šel počasneje kot pričakovano, saj smo zelo neizkušena ekipa, zato nas v naslednji iteraciji čaka še zaključno delo na spletnem sistemu.

### 1.3 Spremembe

Večjih sprememb v tej iteraciji ni bilo.

## 2 Potrebe naročnika

Podjetji, ki opravljata pluženje, si želita intuitiven in zanesljiv nadzor nad situacijo pluženja, ter zmanjšane stroške pluženja zaradi višje učinkovitosti.
Občani in lokalna podjetja želijo možnost kontakta s kmeti, ki bi bili pripravljeni pomagati pri pluženju dvorišč in parkirišč, saj je to za večje površine izvajati ročno zelo zahtevno in zamudno, medtem ko kmet s plugom to nalogo opravi zelo hitro. Kmetje s plugom pa si želijo dostopa do nove potencialne storitvene dejavnosti.
Sistem mora vsakemu od deležnikov biti preprost za uporabo, brez nepotrebnih funkcionalnosti, zaradi katerih bi postal zapleten. Sistem mora biti robusten, saj, če se deležniki nanj zanašajo, njegova napaka lahko povzroči prometni kolaps.

## 3 Cilji projekta

Projekt bo samodejno organiziral pluženje po približku optimalnega načrta plužnih poti. Poti bo spremenil ob sprotnem dodajanju in odvemanju plugov, kar naročniku omogoča večjo prilagodljivost. Na ta način bo zmanjšal stroške goriva dela, ter občanom izboljšal izkušnjo s prometom na dni sneženja.
Z delom aplikacije, ki samostojnim plugom omogoča povezovanje s pravnimi in fizičnimi osebami za pluženje parkirišč in dvorišč, bomo izboljšali kaotično stanje, ki nastane ob novozapadlem snegu. Tako bo delo lažje organizirano in razporejeno, saj se ne bo vsako podjetje potrebovalo dogovarjati z določenim opravljalcem plužnih storitev, da to poskrbi za njih. Prav tako lahko pomaga šibkejšim članom družbe, naprimer starejšim, ki svojih dvorišč ne morejo očistiti sami, kar povzroča tudi poledico in nevarnost poškodbe zaradi padca.

## 4 Opis sistema

### 4.1 Pregled sistema

- Predstavite sistem in glavne izzive.
  - Povzemite utemeljitve izbranih načrtovalskih odločitev.
  - Narišite kontekstni diagram, ki prikazuje, kako sistem sodeluje z zunanjimi storitvami, podatkovnimi bazami ipd. Jasno označite meje sistema.
- Na kratko pojasnite zunanje interakcije sistema.

### 4.2 Osrednji arhitekturni pogledi

- Za vsak pogled zagotovite osrednji diagram (npr. postavitveni ([deployment](https://plantuml.com/deployment-diagram)), paketni ([class](https://plantuml.com/class-diagram)) diagram oz. komponentni ([component](https://plantuml.com/component-diagram)) diagram).

  - Pri predlogu upoštevajte arhitekturne in načrtovalske vzorce.
  - Priporoča se uporaba naslednjih diagramskih tehnik (ne nujno vseh):

    - **Razredni diagram** ([Class Diagram](https://plantuml.com/class-diagram), izvorna koda :bar_chart: [PlantUML](./gradivo/plantuml/RD.puml))

      ![RD](https://teaching.lavbic.net/plantuml/svg/TPDDRi8m48NtFiN8tK2heEOFQ1O8bRO7oBeR4xlWujYLROf4sxjtY0KaG3RHwFbblZVnPEuyitvRAoXVYDj8_SKigw5Ip3du8G1BLcrMrcmrNnXbBEpMqek3RYmNDcXt-Tlpz7M1AhFMx8AuLFWc-MirFRUg6eUtJ3iy4jgJjUG2Acah9GXPD7HQihqL768Ap44PDt4YvgrSRdrSm8Sop2FWmfu4UzAn9mKuhFIgfQLjBSB7GosyuImUD76H8BKV5ZYfKOBfQr8QI6c7b1N0cHTUrgAbvZsi9B1EyOR7iKwET33i7JKB0R9EWF6vnL6QzD2pmJKl3udIynZz_3pmymv_Uir_wk6FR_0dDxHfo9JTk17y-ZG62YQAi1YDxh4kqKZ12LpjR_KfzBkMUvXHWZj17uEbSH-iES75YgBV6TxZmN0ioLneZh_5Fm00)

    - **Diagram zaporedja** ([Sequence Diagram](https://plantuml.com/sequence-diagram), izvorna koda :bar_chart: [PlantUML](./gradivo/plantuml/DZ.puml))

      ![DZ](https://teaching.lavbic.net/plantuml/svg/bPDFRvj04CNlyob6xiKvL14OgYfAhVnhJvLQkN4EKIu3Z9EjOOSk2qvTzRjt5YU69kwX1v1sv_VUl9s5iyQJysrLujKjm8Cf65SYFfD7W6PjR4sEAimeNzyxQMsHIoaElIFRQ8cj7r45hwWj_JK_-lFItDjAovZhYzs8ejoBkn1NiBlipR9ItLy1-uuxQFDWF8yXvsGpqYEEYWt_QDdc_DcizB4yxlOc_NJn_kFb0Vgh3iBafYRh_rzmC2xqHy79iXP7cJLhZ2Pu_WsN4PwUzhNv7A0UR72oeAtZ0jC9KeEBLBaik9BxgUWXCjwHiPAvME-a_0UOxC14GRqIuuDX26WwygoHG5EzdMlF4wmZFFc05NifwDtqQA0MAMYcGCLAnGCLJQFPc8i1If4QjuHTGsl1JYDOQJnWo1eS4dMO3Gw9za4S79909dio6SXqQcKpFJgCFsSBwuB_hhzSFmLH_FWOhzJvE_wgPq7y-yxgLgStlRLK0Ti28D1Fyz7QJSFxCvcUbgpWaYp3k4tSpqjbowYNVSawLW6spry40PoflVw0Vm00)

    - **Diagram aktivnosti** ([Activity Diagram](https://plantuml.com/activity-diagram-beta), izvorna koda :bar_chart: [PlantUML](./gradivo/plantuml/DA.puml))

      ![DA](https://teaching.lavbic.net/plantuml/svg/VL5DJyCm3BtxLqJY0gTfV4Y8JcDbWpCI_06lyRhGrAaIbpAX_NVSRaWH1mwnvFTU_9wJLHACqhVUR4g0r3ZkC69hBEsmz_9ENr9wLtDBBARIGZ5JRR5gwXXwjbNm8Hg9o4afrMMgj4SR1iUrsQ5Fb35LOEl41NwJWoTZ7RQA02pIs2y1At6VJWuRX_Me_mQJUQudps7lX1JtZkc4NDozFDq_hnN36CCmtShvhTSHYXtrd2t_qHnXCJl7WUcn029rX68UoaRZSKXYveLgi_xwJtzJm9Xxm6WpzBRu7QLBwFwNhw4E7sR-U3LQXGvWHMprStu0)

    - **Diagram stanj** ([State Diagram](https://plantuml.com/state-diagram), izvorna koda :bar_chart: [PlantUML](./gradivo/plantuml/DS.puml))

      ![DS](https://teaching.lavbic.net/plantuml/svg/NP91Ri8m44NtFiK8TfMG6Zkqm09HABs0kwkw66ANXYHsvJYYKjMxTuABIRoneZVFyx-bR5gFpdTD3S-IiROgpHSwRE20HNLqjZEgiBLru1sQbaRQ-86bz0TsjN_Lt_wfBe-ceJ4KT6WtiD0vUzvTrXngsZiOKRhNyCC0jZ4mcEVFqkkUMwUq2smwVzakzZkYic-TmltrxXNzqeik0HFopKb3DW5iGMPCPYjGTWLO5UK98Kj57aJE91-98XL540MJOYJEKp4FOivaFewcxBUxTvYj-rvK36Rz9uy2Zqn4Hbj4wZrGrzHxZDwDBIBB8rjIgz3WrkkU_KDgnzX66qL_oHy0)

    - **Psevdokoda**

      > **assume** vrednost1 &subseteq; C, vrednost2 &subseteq; C  
      > **let** maxVrednost1 = max {r | (s,r) &in; vrednost1}  
      > **for** (s, r) **in** vrednost2:  
      > &nbsp;&nbsp;&nbsp;&nbsp;**if** r &le; maxVrednost1 **return false**  
      > **return true**

- Za arhitekturne elemente v diagramu dodajte katalog elementov z imenom in namenom vsakega elementa.
- Za vsak element določite enega člana ekipe (tudi, če je več članov ekipe prispevalo k elementu), ki bo njen skrbnik.

## 5 Trenutno stanje

- Kakšni dodatni cilji te iteracije, poleg tega, kar je že navedeno v [uvodu](#1-uvod)?
  - Kaj deluje? Vključite posnetke zaslona.
  - Kakšni izzivi?
  - Uporabite blokovni diagram za razlago trenutnega sistema.
- Katere teste ste izvedli?
- Koliko vrstic kode ste napisali (skupno do tega trenutka)?

## 6 Vodenje projekta

- 17.4. Dogovorili smo se, da bomo znotraj obstoječega repozitorija imeli povezavo na nov repozitorij, od koder se bo naša spletna aplikacija avtomatsko deploy-ala.
- 18.4. Za frontend bomo namesto create-react-app uporabljali Vite, saj omogoča delo s Shadcn in je bolj splošno uporabljano, zato zanj obstaja več pomoči na forumih. 
- 24.4. Namesto izrisa poti navigiranja bomo plugu le izrisali oštevilčene marker-je na križiščih. To olajša rešitev, saj dosedanje rešitve za prikaz poti navigiranja niso delovale dobro. Poleg tega nova zastavitev bolje deluje z našim algoritmom in za uporabnika ne bi smela predstavljati problema.
- 3.5. Stanje cest v največ 7 barvah. Sprva smo stanje cest želeli prikazovati z barvo na zvezen način, a se je izkazalo, da brskalnik to težko podpira in začne delati bolj počasi. Iz tega razloga se omejimo na 7 barv.

Cilji naslednje iteracije:
Dokončati želimo delovanje spletne aplikacije. Želeli smo, da bi bila že dokončana, a nam to ni uspelo. Zaradi uporabe nekaterih slabše zamisljenih rešitev imamo nekaj tehnološkega dolga, ki ga moramo nadoknaditi, saj bo kasneje postal večji problem.
Izvesti želimo tusi splošen refactoring kode, da bo ta lažje dostopna za odpravljanje programskih hroščev. Nato imamo namen izvesti testiranje sistema kot celote ter odpraviti programske hrošče. Napisali bomo krajši program uvajanja novih uporabnikov v sistem in njegovo efektivnost preverili pri znancih brez tehničnega znanja. Tako bomo dobili vpogled v morebitne nejasnosti pri uporabi in jih naslovili. Napisali bomo tudi dokumentacijo za dele sistema, kjer je to nujno, saj tako olajšamo uvajanje razvijalcev, ki bi v prihodnosti projekt razvijali naprej in dodajali funkcionalnosti.


### 6.2 Projektni načrt

- Posodobljen Ganttov diagram in graf PERT.

## 7 Ekipa

Filip je izvajal vlogo SCRUM master-ja, Matevž pa vlogo product owner-ja.
Sebastjan in Matevž sta delala na razvoju frontend-a, Jošt in Filip pa na razvoju backenda.
Filip je namenil veliko časa Continuous Deploymentu preko repozitorija vsebovanega znotraj trenutnega repozitorija. Tovrsten deployment nam še ni uspel, kljub temu da je Filip v to vložil ogromno dela. Upamo, da nam uspe v naslednji iteraciji.
Jošt in Matevž sta se ukvarjala z Google Maps API-jem, namreč kako naše podatke cest pretvoriti v pravilen format, da jih lahko v React-u prikažemo nad prikazanim Google Maps-om, ter kako prikazati markerje v različne namene.
Matevž je postavil okolje Vite in omogočil delo s Shadcn (po dolgotrajnem neuspelem poskusu s create-react-app) ter osnoval osnovno obliko strani z osnovnimi gumbi in pasico.
Sebastjan je nadgradil frontend, da gumbi delujejo pravilno in kličejo backend, se zahtevki pravilno izpisujejo in so lahko izbrani, ter ustvaril prijavno okno za login.
Jošt in Filip sta vložila veliko časa v raziskovanje možnosti deploymenta, saj smo želeli, da bi ga postavili preden zares razvijamo backend, saj bi tako sproti videli vse probleme realnega okolja. Prav tako je problem s podatkovno bazo, saj ko ni host-ana lokalno, temveč v deploymentu, deluje drugače. To nam še ni uspelo. Iz tega razloga sta bila primorana backend postaviti na lokalni bazi.

Groba ocena prispevkov:
Filip 30%
Matevž 30%
Jošt 25%
Sebastjan 15%


## 9 Refleksija


Glede na cilj refleksije predhodne iteracije smo uspešno povečali komunikacijo prek spletnih kanalov in bili bolj aktivni na platformi Discord ter bolje obveščeni o dogajanju.
Spodletelo pa nam je s sklicevanjem kriznih sestankov v primeru prepočasnega napredka. Sklicali nismo nobenega kriznega sestanka, kljub temu da je napredek bil prepočasen.
V naslednji iteraciji se moramo dogovorili za redni termin, na katerega se bo zgodil krizni sestanek, če je napredek prepočasen. Tako je zmanjšana neprijetnost sklicevanja sestanka in je veliko verjetneje, da si ga posameznik odloči sklicati.

V tej iteraciji smo imeli veliko težav, saj smo na področju spletnega razvoja zelo neizkušena ekipa. Iz tega razloga se je razvoj zelo zavlekel in nismo uspeli doseči začrtanih ciljev. Glede tega težko na običajni način uvedemo neko rešitev, ki bi to zlahka odpravila. Kar lahko naredimo je, da sprejmemo svojo neizkušenost in se pri implementaciji rešitve sprva ne obremenjujemo s podrobnostmi (manjše kozmetične napake pri UI-ju, nestandardna postavitev sistema). Raje najprej privedimo sistem do v celoti delujočega stanja in, če ostane čas, nato izboljšujmo podrobnosti. Res je, da je bolj praktično in hitreje, če podrobnostno napako odpravljamo takoj, a to vseeno vzame dodaten razvojni čas, še posebej ker smo neizkušeni in takih napak še nismo odpravljali. Bolje je torej, da se najprej poskušamo prebiti do delujočega sistema, da smo sploh lahko prepričani, da nam bo to uspelo v zadanih časovnih okvirjih. Šele nato gremo nazaj in poskušamo popraviti najbolj pereče podrobnostne napake.

Pojavila se je težava pri delitvi na frontend in backend. Sebastjan in Matevž sta delala na frontendu ter o sistemu komunicirala večinoma en z drugim, Jošt in Filip pa sta delala na backendu ter prav tako o razvoju komunicirala večinoma en z drugim. Pri združevanju obeh sistemov so se pojavili problemi, saj smo se o povezavah med sistemoma začeli pogovarjati šele na koncu.
Kot rešitev bomo ob nadaljnjem razvoju zagotovili, da vsake toliko en član dela ekipe (npr. Matevž iz frontend dela ekipe in Filip iz backend dela ekipe) poskusi vzpostaviti sistem drugega dela ekipe ter se pozanimati o njegovem delovanju in stanju. Tako bosta oba dela ekipe v svoji komunikaciji imela vizijo tega, kako se bo v resnici njihov sistem združil z drugim.

