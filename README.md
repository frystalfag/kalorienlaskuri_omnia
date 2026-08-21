# kalorienlaskuri_omnia
Ruokapäiväkirja

Tekijät: Maksym, Matvei

Mikä tämä on?

Tää on yksinkertainen komentorivillä toimiva ruokapäiväkirja. Ohjelmalla voi
lisätä syömiään ruokia ylös ja katsoa kuinka paljon kaloreita on tullut
syötyä. Tiedot ei häviä vaikka ohjelman sulkee, koska ne tallennetaan
tiedostoon.

Mitä ohjelma osaa

- lisätä ruoan (nimi + kalorit)
- näyttää kaikki lisätyt ruoat
- etsiä ruokaa nimen perusteella
- muokata jo lisättyä ruokaa
- poistaa ruoan (kysyy varmistuksen ettei tuu vahingossa poistettua)
- laskea kaikkien ruokien kalorit yhteen

Miten käynnistetään

Pitää olla Python 3 asennettuna. Sitten vaan terminaaliin:

python main.py

Ja sen jälkeen valitaan numerolla mitä halutaan tehdä. 0 lopettaa ohjelman.

Data

Ruoat tallennetaan data.json-tiedostoon samaan kansioon missä main.py on.
Jokainen ruoka on siellä muodossa name ja calories. Jos tiedostoa ei löydy
(esim. ensimmäisellä käynnistyskerralla) tai se on jotenkin rikki, ohjelma
ei kaadu vaan aloittaa tyhjällä listalla.
