
## Ideje funkcionalnosti
- on the fly organizacija pluženja - navigira plugmajstre
  - kje je najbolj treba plužit
  - wolt način - recimo da bi se kmetje s plugi lahko dodal v sistem - osnovna verzija je da vsi štartajo sočasno. Nadgradnja pa je, da lahko ob različnih časih začnejo.
- da folk k gre v službo da destinacijo in jih navigira po najbolj spluženi poti. Pa dobiš info od kje do kje se folk voz in je najbolj treba plužt 
- občani report - tukej je dost snega in je treba splužt
- crisis report - če se nekdo zatakne na cesti, ali pa neki ostareli ki ne morejo skidat pa nekam morajo - in bi imel neko ekipo ki to rešuje.
- pluženje domačih dvorišč in parkirišč - da se prijavijo in oddajo ponudbo - recimo za ko so ceste že dokaj splužene
- folk s frezami da gre lahko folku pomagat za dvorišča od folka pa firm pa občin

## Ideja dodajanja funkcionalnosti
- najprej samo sledenje plugom in vremenskim razmeram (map zapadlih padavin glede na vremenske postaje - lahko da le na polovici mesta pada. In ko gre plug tam mimo pač gre na nulo. Lahko je tudi samo iz ene postaje pa se povsod z istim rateom zvišuje, pa pač plug daje na 0 takrat ko gre mimo.)
- ! preverit moramo, da lahko od kakšnega ARSOta dobimo sploh podatke o zapadenem snegu na večih vremenskih postajah po Celju
- do kakšne višine snega se folk itak še lahko voži, kdaj pa postane nemogoče - kakšen je graf voznosti v odvisnosti od debeline snega.
- naredit da prvi sneg ki pade ni tako pomemben - ker ko ga 2cm pade pa je bilo posoljeno pa cesta je bila prej še somewhat topla, se bo ta sneg itak takoj stopil
- sekundarno načrtovanje pluženja

https://console.cloud.google.com/google/maps-apis/build

## vprašanja za občino:
- kaj so Zelenice? Organizacija, ki pluži te ceste na zemljevidu?
- na kakšni višini se sploh začne plužit (baje 1 inch pravi internet)
- - vremenske postaje če imajo kaj svojega
- kje so začetne postaje plugov in koliko jih je na voljo in koliko jih ponavadi res obratuje


## Aplikacija:
spletna stran vizualizacija stanja cest
live tracking plugov?
Možnost prijave:
- plug se prijave (ko se pluh prijavi je online, lahko začne s pluženjem?)
- podjetje, individum - se prijavi da se prijavi za pluženje parkišišč, dvorišč
- upravljalec -> vidi dodatne podatke, ki jih regular user ne (lokacije baz, št plugov)

## Viri
1. Najbolj uporaben Lavbičev vir je tale: https://github.com/gandalfsaxe/ecmi2017
Lepo dokumentiran projekt, lahko nam služi kot zgled. 
Pokriva katere Google Maps extenšne so uporabili, tudi neko demo kodo za risanje po zameljevidu in animiranje (aka. live tracking/prewiev pluženja. Za enkrat še nimam ideje kako bi drugače simulirali "live tracking") https://developers.google.com/maps/documentation/javascript/examples/overlay-symbol-animate

2. Python modul za reševanje vehicle routing problem (VRP)
https://pyvrp.org/index.html
Tu bomo uporabli:
- heterogeneous fleet (različna vozila, niso vsi plugi enaki)
- muliple depots (več plužnih baz)
- mogoče costs, s pomočjo katere bi lažje definirali prioritete


3. Vreme (za enkrat) se osredotočimo na eni vremensko postajo v sredini Celja
https://meteo.arso.gov.si/uploads/probase/www/observ/surface/text/sl/observation_CELJE_latest.xml
Najbolj nas zanima zadnjih nekaj vrstic
```
<snow_var_desc>Skupna višina snežne odeje</snow_var_desc>
<snow_var_unit>cm</snow_var_unit>
<snow/>
<rrHh_var_desc>Interval merjenja padavin</rrHh_var_desc>
<rrHh_var_unit>h</rrHh_var_unit>
<rrHh>24</rrHh>
<snowNew_var_desc>Novozapadli sneg</snowNew_var_desc>
<snowNew_var_unit>cm</snowNew_var_unit>
<snowNew_val/>
```
Mogoče nek programčič ki bo avtomatsko modificiral te vrednosti, za voljo testiranja projekta, 
potem imamo več .xml testov. Lahko jih pa tudi samo ročno spišemo.
