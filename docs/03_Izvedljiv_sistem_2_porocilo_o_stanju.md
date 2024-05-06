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

  - #### **Komponenti diagram**
  ![Komponenti diagram](https://teaching.lavbic.net/plantuml/png/RLBBRi8m4BpxAqQvq1xu0Gv88AGs9w8YkBGzECa6h0HlP9j4IjL_hvFoSk1cxypipdWzmOeAfGbAEpA5pCYYO0EIsG4P7slMf9sueeYQ8rcjIdJoIsCfEvbmBbt9JGHfiLh65-gzQ1kZfTHoLfAp0t4RFoMcXbjB1c_91lPKrspSGFVtWIN4vEBuwiwAwp4m98Aw7wtp3PccRt83rhLJHzL9noPXfyGzjlNZPQgLBTNkdFf709y-JUADVMCQnFZrub4xJ7DkzJHubi0AnjZD_WXwOkQ_-VpkSKQzp_X3nX5j7iHup337o-9ZiyOYYL_x1Ipo73dPp2ZFP6t5HBCZ6BK_E70HB04pHEz6QeMAO9si_ERg0QD83BAAYa4r7kk5E-FPtDVFEgVyf-ia6akGfLDDNwrEUz_h3m00 "Komponenti diagram")

  - #### **Deployment diagram**
  ![Deployment diagram](https://teaching.lavbic.net/plantuml/png/TLJBRjim4BppAnQ--6J4FVHM572G10tG6e83dGeVrk929YoJAKarJGB_UvUa7fGV5vapmnrobmDZvOs5sKeUbPu1EbW9JDIQBDNAUQiiQcXVZSMTLeUugLptkugchHDL2A6D96WCLjZiZVFmAG2upYiDNvVBPOTCwnb-2P09h0vO4ypAvrdS3_3xXpaI5Cnk4ouTsG6V17_YGJik9Iq_9pwDgPNUKEsKvwAaiSNFG6zxj8cDaTsAo9p4nEA8cd-AnhovqM0bvPsa1bwP7dnUzkODi4cisrup-y2zfxy7DJezQsx7nnAbQx3qfoNdUqy6BJVFuYO9hgzx_4TLwoaMJgjE_LWaUjoXusc-l7D_nuVxVgQE7ojS9upIJPZOPs_GEgf2lUF6qW0oiYR_orXw8lIj9PSfAEMQOi6Kx5eGxBs2nU9xIa6vpjR5k0wVYF80PEkedL_Y3CSzamo8UVVuoJhBqdpCmONMPUk2dyPhKDsvycsn69IiFbOCmxrGiZcEotJAD7_Z-qJnF8TvWiE6T5hEXlibzjeb-dSRb-cSMz6z9Go73rdEGVAy7klhT9SL_kkOXs-4PV4V "Deployment diagram")

 - #### **Diagram zaporedja**
 ![Diagram zaporedja](https://teaching.lavbic.net/plantuml/svg/dPBTRjf048Nlzob6z8PAZL0iZAeeGYBfZo9LZGMbLxqPsmCic1rtl3Ofxz2toeDrR4Cn3RreBuo0_SuvSsQziYd1Wjd7_6HCiR4kHy4jn9XibiAbInFEMC0BkaAFoFaEbT82oyn_eIS_oUpIRVKO4lqWwL2OU9OxbfJalZ6BCtL_0VnERA7TodhgGYAyw-W1EeS5VI_99VJ9BlHnr4rx5NwuU_l-_W8TeNYRs1oT_tV1nN5DKmLwyy9ZjYPd8S_APGycCvXVm-rjSpmU6vEVdA0tQ24iO1eg5DUkA3-KEyFgI7AfJYCLISi7oYVil73s9_wOUxkrUwm7ojdRLZ3yks0odJt297femT7v94qrMw4dRMAqpDLOfxs1TrnnPg7CMJ1c-1ZDJk0qD5ge1eCR7Q7Wb6EhH5-VrnqiCDgZneQAYQsfY7q_AKNcMlRDDrVxLWMj8bqKLrtjq6YbMZkg8rBq6_jLI5z4x9zZf-yZe-Mk3dc30UmnTMjxL6iOwryvfXdfpJjQbYQbhhhxQsYE-Uhri1Ty_bcwPjrduHSaXxLe_cSiCgf7M448MvGDoPegdMEFSDp12uUWTGZ_po5eBaODvjS70zXHNB2-O1uuhgZmxI8Er-4hU_8rlm00)


- #### **Diagram aktivnosti**
  ![Diagram aktivnosti](https://teaching.lavbic.net/plantuml/svg/NP8xRiCm341tdOB8b5mX7dg0ea2NBaKN6c9i-aCPakp1HO_WG_GWxUJSgtJY-5DD0YK-yb4A4NqqvlpME8-fS0dEMeGUyqWTbRg1fcglloG59URy_eWN1A7nL51CJAC8Zkm43jSVxgg299G8rgKFK8a7-3IWw_nQjHa32xoWO4P-mIC41oxjwFez3YGCxf7S9hTKli3nsJhWFYLFJoU8EGaS9-0SWu3rwNPtBgI4SH227YnLhhvpg0e4nqtvh8KFqNOhDmwygEz1whlsfgtDjsF7CrGiN-w6ouoqZ8wenb98-Tnhe1Ui4R2Ct0dd6fqLNGSrMN2DHvqV2YLcNzk6w57VOE9ecajv7B0God0pG9tgT3P35fCjwtQeaalXUigQA2vwEyjiViC_xnLFGlNoG9EUG7GBvMl_LNRjhvQSh_w9CI6wvWy0)


- #### **Razredni diagram**
  ![Razredni diagram](https://teaching.lavbic.net/plantuml/svg/RP1DReCm48Ntd694DxI4gDcogvAqMQS7G8EPEbOisxLDMXHnzuB3dqGtbkRDc-zvXabq3jwxz_fc33oLoAwv5FpYIrdJFG98iQeA8_LFyfp3JOkgrwJcGYq5IrmuJtRIsYWo7GivmG4zbkXee9-fWdlK3R6GFNRtMYbYNbleKm4ozX24Lg5EXxfFs2zRxPfr8cbe1ANVDTdc-4iicP5BnWQ2e_2DeHm-lHMARm0jTpaS1FFpccstrYFfJCZyVB4FIwH2Nggq5rzDmYweE5K5Mi8HkhZDTF5u5sTPlDjkN-9_Jf53xSWjtA-zSJKmxBjo1tOOcJuS_G40)


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

![Ganttov diagram](https://teaching.lavbic.net/plantuml/png/dPRXRk964CU_-ob6rm_DvKFQa4HDfLDr71YEYc1a7DJhwOGMF9Z5zYxQNRY6wXuX3z4NwQVSUtNM6336HwvHK33htVdDpFvdTjzgmvI9c306NhNjbrn1o5caMFhASTveyv3WRquseRaPXhyT0CDJJBZ0x0T0bnuRCf4AVfZMx5yssfB2R4PftGCDVR4hcOxpLU_O98wKN8emNuktqvjfMBPuqtftwpRovVHXIidFn-23QIbFK1kvS_0bg4aYDORVCb0PPyAZcTa5-yLvyrEUG4V7N2oOJT-uPCae9ZIzGc6S6GyHfbAQiVpBIPY8bYn2q8dZB9ISuyH0jbyQp0pXybSp0pc55exLaga7gFrSktOqCqiLiWTDUS8y1aSJhJJaV3m_lxe0Rb2n2P-pytCugzr2AFZhJy0qVEm4hd_r2HAcYNSDdn5Z3NRLC4xcowT7Mhc2E4Mhc1KiakNNVr7C4TOmz1h01Vo92Ge-GMlvkc2uLVVlN7-mDvsvPYtxRBsISz3q3oC6B8cauYPb81KfaA-jexX3PIvVrWgM6_U3mBiRrRjjRslTlj-Pbq-FGe8XPN1AEfdIN1ia-x4qCC54cYDd1ny6WNit2jn1K7AOYN2x6ymSid_KW2AqoCuwn8Ij68GoNgQqnPiGghcrOsxJQsonjKfiqRyzja_QoKCKJ2SOsgVjLcUioyi2hD-jzqOzzuzWr1owkyoTubc_Yb6kC1mpK6YKr0kC3LyX2HlD4RP0zTt0zpBii7OQUkXVphNWw-S4V5qMSDdqHkNxK7hiwL6HfBFSBQJX851Xn9KsYbDIKrWkf69ZmMEPMcIHsEuFHeFtTR_JQu_kUxxRtj9lAyCwPeSicOiv1xKfXESAu88So6lgtW_Uk_wewGvtgVpb_mX6QXdASLRJ2vbYEXQIgeIUDKjnBVYCTAeDHAGbgoaWBsTo9M6XE7M3SJ97k-3YQ8-zUdFKz_htNSfAyE7qDXU3A6pozvJjnOcw7Nb3rwztkwVhj-nfGTt2O9HfJCS7RfG53fhIWVEl_r1oKbRsgDCBtBPV3pfUxplQoRVT2VOEKCxDKUJtlKwmYVlgfOXctgnoJ2p3e_xKy9gkxG9xI7L_AdfJa9l29MLgKsHAsck5ZZSWW3E5KpOnf7mHlRueWtstLMy4NbPZBs9x-r9Ya1shiSagwUocs19zxtUtGThn2vXgsHvwz5nNF6Y7LvNjy4N0x6Ic_DcKzlEeB2Ah3y7XwP7fNRWvSkWrTwJz2NzmYd8D4xgcq6w5zaptwUPmU2PMJJZeHbKJZjh2CvXz2LTQEvH4rPJITbPDoP9HUj6rzxcsGXJEMqfoTWt-3m00 "Ganttov diagram")

*Ganttov diagram*

![PERT](https://teaching.lavbic.net/plantuml/png/bLDBRjim4Dtp58DcaLM-_jH83GEEemG6d3gGd1Gj0XYqDL9fqQHBKMxh8aV88NgHhf9xbQJaW7QIVZQIPaQSzzxCOvuniQ2Apc52frcgP27YdkHIWLPKvAQ4GXEEYGOjGR7qiuQOAPng9WKX-PHoXCFz5Y7jN7_ds26vfXhF64rjqny4W2eblxelW04JMBQVS8DdSdVaZhGFghCaVw8JsJRkrEaMiHri9OqajXMfObHLjd5-sWfwfflN9CQ45boFy9lkSfQAkH43K_D0HNQztnOCZWztISaTthIdjkN9AI-mKzi7PdwdKpQZxGDNwBm1caD_58Grs4aIR6Bp7JV2t86j7XSAKNHkCZuh7kvDeoLaSzHo2KjOyEBn5uePmWfkXZrW0ZuXHy6cU2k2w0JgBVC-Fu76yQqOLF70nOx0UJUy3C9eFO-IWiFRuj2JYl9EI5TBEOFSF32bG7ag5TDp2bAbLB2LLOXFf6X9mK9R2ircIS5HSR6ZqBkEHiFBSNTmCToauI1V74Ke7-w518svPiPX1Z9dkKR38vDsDrpgIhx5jDXl3qjiny753Zlw68s2o_4eY4QmCwaboQJs-WYwNmhQwQzYv7H98PPPOQrGIduDt-8w_ACIt_5miOz_PZPdJ41hpSe45keb8zN_PAJwFnhfIc7ACOPYOGOy4UpnPuQRSYhkHnNtoZfEWuiTv7KKX2Nplmrk4pQJiLpFQmkelWLKBmqoF0l6ON3J3pxyxvBCTLWejb3sUsLS6iTqPi1npWHLkP4jA9VfMc-zej6eQDGh6eroLy5b_tqt75zrhuBmXNMHyZBlxNNMjyhBU2RtifxzY7yDjck-JRsQ6Jxn76GhpWUaT8EDrqloKjuulUo6EkAF_7drQVFFIhy1 "PERT")



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

