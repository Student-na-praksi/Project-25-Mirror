# :yellow_square: Predlog projekta

| Prejšnji dokument |          Trenutni dokument           | Naslednji dokument [:arrow_forward:](02_Osnutek_sistema_1_porocilo_o_stanju.md) |
| :---------------- | :----------------------------------: | ------------------------------------------------------------------------------: |
|                   | :yellow_square: **Predlog projekta** |                   :orange_square: **Osnutek sistema**<br>(1. poročilo o stanju) |

![Terminski načrt](https://teaching.lavbic.net/plantuml/svg/fLVHRjfA47tVhnWr3yb5WiPh8BIAeghjhLJrIgsgFYNAmmGlPB7PjNONzuQhVa8-el-I_bTdZKCmDhRJAtY0OUUScJF7O_F6EZHkZievUF5DcALKDfQWyE7Uk1UCdLjtbuWBbfzuBt5kS0d_CG0dboAHIkHV0FwXZ-zqeWqSpRX_vT4FMhbDbFBkAFJ3PwADYwotE8tdHgzKLEIAoMmqY_OHHn_UJlv-LwIZCVfxbRLqPYaJOPtULlSdFDD4Mn4T0gXjCf7pMxVjz0SxVrcenqXJbQBNxcOFoHbKbduIoh7ZMna9c6djRlI_B44rN-5SW4rOQgHoTeg9WEz2nCaTGQ9RcGZlI11H5CiimPOZ_9GF-wVq3a3Q_I0_gmH7TISfo7U2HJJi1vCywliWfQI2e-XKuEo67MzfMquGyhZjH55bzGJxOlH2J1ta7hQmIU3zu1LZL-TvmkljI2ukoTB2YHZaEiC5gWL2Ie1BuH1EWbS3FlZh_6MUT74DjvYcGbb0jujwVDK4KZ3cP1q1QyhizJwkKvseXSW8Na2M6lpr4nCbO-prVFkzNchqJ2RI-0CKEmd0YKYe7JgqSFK-k8O4BGap0dA5fVB_0BpSLJUYkgw-uZgYXU541XdOU9NIPVT8ATStn4UQhcM63Gtn4W-WYXv7JxBwCeuj21NbZJw7hqkFNRbPlm_108ZOu5IIF_fz6dElzuLiakWvsOKy6xiARUXfbTod3HzfWuss5MBkYVC0k_eSHLWuagXmoxNNu6GGDbhJNzYCh3xN6Ise2jgciikzeLSA2tSLuHL5QYposQgLlxQij4uiSoCSK6MqLMNOGkwjKCNjedntZcelnI381was-k5U9WZQ9wl52aucWs6Z_dvjKk6D8AKEEW7MRSJDX6iPocfSyfPfZvu4RuHzBfmtJzZ5F1_N6Vbq8RDYpDuzm_h9ZhUJdRGsKmjS4lz_anoq3w-tptWmQfoslwS-sOUtswSJu67xy0xs2LlcFQxQXpVOfpESjy-mYtq-QVLmh_mzmQlMi7e2thQHnxlkgU1sMJtFu3XedZWd5dvlRrKyuMUje-PdJzwfmoZLtmtli7Lg2FQCCsoPTC2hpgb1VJPQJT4qIZ6jVNeCWrOPme0AF8XGDaKdDFQ6oip_bVq6 "Terminski načrt")

V 1. iteraciji ekipa predlaga projekt, ki je skladen z izzivom dejanskega naročnika (zunaj ekipe). Ekipa določi zahteve, projektne cilje, načrtuje implementacijo in se seznani z orodji in platformami, ki jih bo uporabljala. Na predavanjih v tem času obdelamo potrebe in zahteve uporabnikov. Podrobna vprašanja v predlogu omogočajo, da ekipe delajo vzporedno s predavanji.

V 5. tednu ekipe predstavijo svoj predlog na zagovoru. Povratna informacija pomaga ekipi določiti cilje projekta, ki morajo biti dovolj zahtevni, a izvedljivi.

Predlog projekta in poročila o stanju se nadgrajujejo v celovito končno poročilo. Vsa poročila imajo v osnovi enake odstavke. V predlogu sta poudarjena odseka [**2 Potrebe naročnika**](#2-potrebe-naročnika) in [**3 Cilji projekta**](#3-cilji-projekta). Gradivo iz teh odsekov se lahko uporabi v kasnejših poročilih.

## :page_with_curl: Opisni naslov, osredotočen na prednosti za naročnika

## :information_desk_person: Ime ekipe: Člani ekipe

## 1 Uvod

### Začetni odstavek

- Kaj je projekt?
  - Kakšna je motivacija za ta projekt?
- Kaj je pri tem izvirnega?
  - Še kakšen vidik za orientacijo bralca?

### 1.1 Izzivi

- Na kratko opišite glavne izzive za ekipo.
  - Kako jih boste naslovili?
  - Je tehnologija ekipi znana ali nova?

## 2 Potrebe naročnika

- Kdo je primarni naročnik (zunaj ekipe)?
  - Kdo so sekundarni deležniki?
- Kaj deležniki želijo? Zakaj?
- Kakšna je njihova želena splošna izkušnja?

### 2.1 Uporabniške zahteve

- Zapišite **SMART** uporabniške zgodbe na podlagi potreb in želja deležnikov.
  - **`S`**`pecific` **`M`**`easurable` **`A`**`chievable` **`R`**`elevant` **`T`**`ime-bounded`
- Uporabite predlogo "Kot **_\<vloga\>_** želim **_\<akcija\>_**, da **_\<posledica\>_**."
  - npr. "Kot **_prijavljen uporabnik_** želim **_urediti podatke v svojem profilu, vključno z imenom in profilno sliko_**, da **bo profil vedno vseboval točne podatke**."
- Za uporabniške zgodbe zapišite teste sprejemljivosti z uporabo predloge "Glede **\<pogoj\>**, ko **\<akcija\>**, potem **\<posledica\>**."
  - npr. "Glede **_na to, da sem prijavljen uporabnik_**, ko **_zahtevam urejanje profila_** in **_posodobim profilno sliko_**, potem **_so informacije o mojem profilu posodobljene in vidne vsem uporabnikom_**."

## 3 Cilji projekta

- Za katero težavo naročnika ste se odločili, da jo boste obravnavali?
- Brez tehničnih podrobnosti opišite koristi sistema za naročnika.
- Kako bodo koristi podprle želeno splošno izkušnjo naročnika?
- Kaj bodo konkretni izdelki vašega projekta?
- Cilji morajo biti merljivi in preverljivi.

### 3.2 Merila uspeha

- Pri komu izven ekipe ste preverili ustreznost ideje?
  - Opišite dejanskega zunanjega naročnika.
- Kako boste vedeli, ali je naročnik dobil želene koristi?
  - Katera merila uspeha so pomembna naročniku?

## 4 Opis sistema

_V okviru predloga projekta zadostuje osnutek tega poglavja._

- Narišite blokovni diagram, ki prikazuje, kako bo predlagani sistem deloval z zunanjimi storitvami, podatkovnimi bazami ipd. Jasno označite tudi meje sistema.
- Uporabite prejšnji diagram za predstavitev sistema.
- Kaj so osrednji elementi predlaganega sistema?

## 5 Predlagan pristop

_V okviru predloga projekta zadostuje osnutek tega poglavja._

- Na kratko opišite, kako bo sistem deloval.
- Katere platforme, orodja in knjižnice boste uporabljali?
  - Kako boste sistem testirali?
  - Kako boste ovrednotili ustrezno strategije testiranja?

## 6 Vodenje projekta

_Začnite zapisovati v **dnevnik sprememb**, kjer sledite vsem spremembam projekta, kot je opisano v tem predlogu projekta. Za vsak vnos v dnevnik sprememb vključite naslednje podatke: datum, opis, motivacija in posledica spremembe._

- Kateri razvojni proces in dobre prakse boste uporabili?
  - Kakšen je minimalni delujoč sistem, ki ga nameravate zgraditi v naslednji iteraciji?
- Kakšen je vaš seznam želja glede funkcij predlaganega sistema?

### 6.1 Usklajevanje ekipe

- Kako boste razporedili in koordinirali delo v okviru ekipe?
  - Kako se boste sestajali kot ekipa? Kako pogosto?
  - Kaj nameravate doseči med sestanki?

### 6.2 Projektni načrt

- Povzetek razdelitve projekta na aktivnosti s seznamom izdelkov, vključno z Ganttovim diagramom in grafom PERT.

![Ganttov diagram](https://teaching.lavbic.net/plantuml/svg/dPBFJy8m5CVl_IjUzA3k8aoNO48C0kB5WmTlXCE3lesoqfBs3LmC_xlTc4IcN4oJTlssd-_xqGqye-CC3JDSl5IBtO9Kc3bSNmZHzrngUXJrXV51Xay1m6fDMXcgDm2luNDajNLmcSRLgDM9DNnG0rS6QL-HwFE66k8YpvmjZ6nOwgL9AjkEoMJOUnurE3fdTx-ZdjnPAqsUxJ6x_yHPQEj9dZFuiqYjiYKVAzsB_ctJFU5pPJPOzMxUScA7neSZCYoMIXAarlBSVWYD9Yim8_1QY8spAremr8_bWPS4tGTUWarXGdDNe2iXxiJtmYCNJcBfGv-egK7u4AqbYMaKlRaj0kQijiPwZYAuxdP06dKp0_GmVUhEGACFuIevy1KpTaNMWfAVJ7naO4UK0nhvdJHoxNdbWOoilDuTyQgTmOdRtT4jWKC5v-p48CprJ_e5 "Ganttov diagram")

**Ganttov diagram** (izvorna koda :bar_chart: [PlantUML](./gradivo/plantuml/Gantt.puml))

![PERT diagram](https://teaching.lavbic.net/plantuml/svg/bL9DJyCm3BtdLrZR3MsmTUeqGLN1O9mu8DXjx90rRYdD4kHcV8Zjl-Eq7LJJE718ujX-x_b5kIoT9BTPQ-ZSpnxce7APaLntX2YBtBnAZc4bao8Zkp7gscfBu4YQaajedD2OEd0MAC-U7QC94vTRm_14QeJ1wKI8g7IV6cF1KWvlQW7u4W2IoBvN4S1TRh2cNsdMuznEx4Hqrc1RupnwcWerFHYiYvCqJ9MlM598JJQydKvcrypM8b6OoersS_nmLphFp9hDGC8RagW7XKwKUFovabGGglYUtYJ8mkLlnfOkEgkgSGTa2LT3wAOfZd5yeTd77WBd43NvNdF6Mu3X0BRWbm-UpDRRRwVs-ZUqoLgAjL9GaTP6UytfII5iq30CQzRg4bHR-4jwO6fEw5x-j3NwXwtXpm11kBSrQAU4M9mieR_eDZIzbTLgsO_vzGG_ODz7GHKTQHa9TkvRc4FmN4TwV4LSeb7ycxy1 "PERT diagram")

**Graf PERT** (izvorna koda :bar_chart: [PlantUML](./gradivo/plantuml/PERT.puml))

### 6.3 Finančni načrt

- Finančni načrt projekta po metodi COCOMO II.

![COCOMO II ocena](./gradivo/img/cocomo-ii-ocena.png)

## 7 Ekipa

### 7.1 Predznanje

- Kakšno je predznanje ekipe?
  - Kakšne predhodne delovne izkušnje pri razvoju programske opreme?
  - Je kateri član ekipe že razvil kaj podobnega?
  - Ali so orodja ekipi znana ali nova?

### 7.2 Vloge

- Kakšne so načrtovane vloge članov ekipe pri projektu?

## 8 Omejitve in tveganja

- Ali obstajajo kakšne družbene, etične, politične ali pravne omejitve?
  - Opredelite možna tveganja in strategije za obvladovanje tveganj.
- Ali boste imeli dostop do podatkov, storitev in virov, ki jih potrebujete?
- Ali potrebujete še kaj drugega?
