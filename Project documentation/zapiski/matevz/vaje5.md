Zajem zahtev:
- funkcionalnosit
- nefunkcionalne zahteve
- specifikacija vmesnikov

Funkcionalnosti:
Natančni moramo biti pri funkcionalnosti.

Specifikacija vmesnikov:
- zaslonske maske - med človekom in računalnikom. Specificiramo kakšna vnosna polja so in kakšni elementi so gor - naročik si že lahko predstavlja. Laghko jih narišemo pa poslikamo. (Brezplačna orodja, lahko tudi prototip maske, eni naredijo že končne maske ki jih potem tudi uporabijo, Visio? je eno orodje)
- drugi vmesniki so med nami in zunanjimi sistemi (API, nek drug sdostop) - opisat je treba kako se dela klic, kaj dobimo nazaj. Teaching.lavbič dober primer. Če mi ustvarimo nek svoj API moramo tudi dokumentirat, ampak za ostale.

Nefunkcionalne zahteve:
- sistem mora biti sposoben obravnavati 5000 uporabnikov naenkrat
- sistem mora biti sposoben teči na redhead enterprise linux z nameščenim strežnikom apache tok pa tok

Nefunkcionalne so bolj kritične kot funkcionalne. Nič ti ne pomaga da je vse funkcionalno možno, pa nič potem ne dela.
Merljive morajo bit.

RUP - rational unified process.

Funkcionalne zahteve:
Diagram primerov uporabe.
Vir za funkc in nefun zahteve so uporabniške zgodbe.
Generalizacija (puščica s trikotno glavo ki je prazna). Med uporabniki. Med primeri uporabe. To pomeni, da ta, ki razširja, uporablja vse funkcionalnosti kot tisti zgoraj.

Asociacija - med akterjem in primerom uporabe. NIKOLI MED DVEMA PRIMEROMA UPORABE.
Pomeni: akter a prične primer uporabe X.
Z neusmerjeno povezavo: med U ini PU: basically isto. Med zunanjim sistemom in PU pa smer puščica je nujna, ker ne vemo, a PU uporabi zunanji sistem ali uporabno.
Zato kar vedno uporabljaj puščice pa je.

Za ta predmet je dogovor, da delamo tako:
Na levo stran akterje, ki so vloge. Na desno zunanje sisteme.
Na sredino primere uporabe.

Ne pozabit narisat mej sistema.

Funkcionalnost ki se mora avtomatsko prožiti na določen čas. Narediš akter, ki mu rečemo timer.: (<system> Timer) Ta bo znotraj sistema, zato ga rišeš znotraj tega kvadrata.

Odvisnosti: Include in extend.
Vedno s črtkano črto.
Kaj pomeni extend v levo? Leva funk je razširjena z desno (desna razširja levo): pri določenem pogoju se bo poleg leve funkcionalnosti izvedla še desna.
Include v desno: Leva vsebuje desno. V okviru leve se vedno izvede tudi desna. Leva vsebuje desno. (Zakaj smo dali ta kos ven iz funkc, če se vedno izvede: ker ga dva use cassea uporabita - nek drug ga extenda recimo.)

Akter je vdno tist, ki je v interakciji s sistemom. Zato je pri nakupu kart na okencu Prodajalec akter, ni kupec. Ne pisat Kupca sploh.

Vsako elipso je potem treba opisat:
IME FUNKCIONALNOSTI MORA BITI ISTO KOT V DIAGRAMU!

Osnovni tok:
Najbolj običajen primer uporabe use casea.

Alternativni tok

To je oboje direkt osnova za diagrame zaporedja.
Ta je pa potem osnova za risanje razrednega diagrama (teh metod, ki jih imaš).
  In se splača te dobro nardit.

Predpogoj za prijavo:
uporabnik ni prijavljen.
Popogoj:
user je prijavljen.
Ali pa: število uporabnikov se poveča za 11,

Posebne zahteve: glede hardwarea načeloma (npr. čitalnik črtne kode)

Vsaki funkcionalnosti še damo prioriteto:
MUST HAVE:
Brez njih sploh ne bo delovalo, al pa bo nezakonito.
SHOULD HAVE: Prispevajo uporabniški izkušnji, ni pa nujno. (Npr. statistična aplikacija: izračun nečesa je must have, vizualizacija je pa should have)
COULD HAVE: Vse funkcionalnosti, ki jih izdelamo samo v primeru, da imamo dovolj časa - če bomo po planu. Te prvo letijo ven, ko ni časa.
WONT HAVE THIS TIME: Te, ki vemo, da jih ne bomo realiziral zdaj, ampak jih imamo na zalogi.


Sprejemni testi:
Vsak primer uporabe ima več sprejemnih testov.
Začetno stanje, vhod, pričakovan rezultat.
Če si pri uporabniških zgodbah naredil več testov, ti bo zdaj lažje.

Pri opisu funkcionalnosti še pogostost uporabe - kolikokrat se bo uporabljala.
Likartova lestvica kot prejšnjič. Lahko pa številsko pa povemo kaj pomeni 1 do 10, kero je največ in kero najmanj.


Razširitvene točke in pomoje vstopne točke.
