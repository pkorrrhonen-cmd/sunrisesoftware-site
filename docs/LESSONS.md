# LESSONS (Sunrise Software site)

Opitut virheet ja estosäännöt, jotta niitä ei toisteta. Uusin ensin.

## 13.11.2026: todistelistaan valittiin artikkeli otsikon perusteella

**Mitä tapahtui:** 11.11. SEED v4.0.0:n luku 2.2 ja `copy-v4-pages.md`:n osa C listasivat `/rooms/`-sivun
todisteiksi neljä sf3d.fi-artikkelia, joista yksi oli `blind-to-anything-taken-away`. Se on Somnuksen
äänidetektorista (27.8.2026, tagi `somnus`) eikä kerro huoneista mitään; otsikon "blind" sopi sokkona
äänestäviin huoneisiin. Samalla rivillä videoiden polku `media/publish/rooms-en.mp4` oli kansion vajaa,
ja labran git ohittaa koko `media/`-kansion. Kumpikin löytyi 13.11., kun artikkelit luettiin ja polku
katsottiin levyltä ennen tekstikierrosta. Sivulle olisi tullut todistelinkki, joka ei todista mitään.

**Estosääntö:**
- Linkki tai lähde kirjoitetaan listaan vasta, kun sen sisältö on luettu samassa sessiossa; otsikko,
  tiedostonimi tai haun osuma ei riitä. Sama koskee Atlaksen ja tiedostolistauksen kuvauksia
  (LESSONS 12.11.2026).
- Tiedostopolku toisesta reposta tarkistetaan levyltä ja sen gitin seurannasta: kun tiedosto ei ole
  repon puussa, rivi sanoo sen ja kertoo, mistä tiedosto oikeasti saadaan.

## 13.11.2026: päätön selain ei kaappaa puhelinleveyttä

**Mitä tapahtui:** `docs/mockups/shoot.py` ajettiin `/silent-context/`-sivulle leveydellä 390. Kuvassa
leipäteksti ja navin takaisin-linkki leikkautuivat oikeasta reunasta, eli sivulla näytti olevan
vaakavieritys. Selainpaneelissa laitteen emuloinnilla 375 px:n leveydellä sivu oli kunnossa:
`scrollWidth` 375, mikään elementti ei ylittänyt reunaa. Päätön Edge piirsi sivun leveämpään ikkunaan
kuin pyydettiin ja rajasi kuvan 390 pikseliin, joten kuva näytti vian, jota ei ollut. Toisin päin sama
työkalu voi peittää oikean vian, ja sillä on otettu kaikki aiemmat `*-phone.png`-kuvat.

**Estosääntö:**
- Puhelinleveys tarkistetaan selainpaneelissa laitteen emuloinnilla (375 px) ja mittaamalla
  `document.documentElement.scrollWidth`, ei `shoot.py`:n kapealla kuvalla.
- `shoot.py` kelpaa työpöytäleveyden koko sivun kuviin; puhelinkuvat kootaan paneelin
  kuvakaappauksista.

## 12.11.2026: Atlaksen kuvaus repon sisällöstä ei ole repon tarkistus

**Mitä tapahtui:** 11.11. kirjoitin `copy-v4-pages.md`:n `/silent-context/`-runkoon todisteeksi
retrospektiivin polun `docs/retrospective.md` ja kierroksen A riville A.4, että palkintosummat ja
joukkueet ovat "retrospektiivissä repossa". Molemmat tulivat Atlaksen artefaktista
`SINCEAI-2026-HACKATHON-TAKEAWAY`, joka sanoo "Pysyvä versio on repossa docs/retrospective.md".
Repon puuta en avannut. Tiedosto oli poistettu reposta 8.11. klo 18.23Z (`f1b893a`), yksitoista
minuuttia artefaktin kirjoittamisen jälkeen. Virhe löytyi 12.11., kun sivun faktoja tarkistettiin
itse reposta. Sivulle olisi tullut linkki, joka vastaa 404, ja osio, joka nojaa julkaisemattomaan
tekstiin.

**Estosääntö:**
- Polku tai linkki repoon tarkistetaan repon puusta samassa sessiossa ennen kuin se kirjoitetaan
  tekstitiedostoon tai päätöslaatikkoon. Atlas on peili, repon `main` on totuus (CLAUDE.md,
  totuushierarkia).
- Kun Atlas ja repo ovat eri mieltä, repo voittaa ja ero kirjataan sille riville, joka nojasi
  Atlakseen.

## 12.11.2026: suosituksen jokainen jäsen tarkistetaan sitä sääntöä vasten, josta päätetään

**Mitä tapahtui:** 11.11. päätöslaatikossa suosittelin, että SoftwareApplication-merkinnän saavat
"kuusi julkisesti avattavaa tuotetta", ja listasin niihin SF3D AI Labin. Petri valitsi suosituksen.
Seuraavana päivänä rakentaessa huomasin, että sf3d.fi on tutkimuslaboratorion sivusto eikä
sovellus, ja sivu itse sanoo niin. Merkintä olisi väittänyt koneelle asian, jota sivu ei sano, eli
rikkonut juuri sitä päätöstä (adr.sws.019), jota laatikko vahvisti. Korjattiin ennen julkaisua
uudella laatikolla.

**Estosääntö:**
- Kun suositus on lista, jokainen listan jäsen tarkistetaan erikseen sitä sääntöä vasten, josta
  laatikko päättää, ennen kuin laatikko esitetään. "Julkisesti avattava" ja "sovellus" ovat eri
  ehtoja.
- Kun rakentaessa paljastuu, että päätetty kohta oli väärä, sitä ei korjata hiljaa eikä rakenneta
  väärin: se kysytään uudelleen ja korjaus kirjataan päätöksen riville.

## 11.11.2026: vahti joka ei voi laueta ei ole vahti

**Mitä tapahtui:** sessiossa 4 (20.9.2026) kirjoitettiin CI-tarkistus, joka kieltää tuoteversiot
sivulta (adr.sws.015). Säännön regexistä katosivat kenoviivat jo kirjoitushetkellä: sanarajasta
(kenoviiva b) tuli merkki 0x08, numerosta (kenoviiva d) kirjain `d` ja välilyönnistä (kenoviiva s)
kirjain `s`. Lopputulos oli kuvio, jota mikään sivun teksti ei voi osua. Sessio 4 kirjasi
CHANGELOGiin "regex testattu positiivisilla ja negatiivisilla", ja CI oli vihreä, koska rikkinäinen
kuvio ei osu mihinkään. Vika eli mainissa seitsemän viikkoa ja löytyi vasta kun skripti luettiin
riviltä riville 11.11.2026. Sinä aikana sivulle olisi voinut kirjoittaa minkä tahansa
versionumeron ilman että portti huomaa. Sama virhe toistui tätä merkintää kirjoitettaessa, kun
kenoviivat katosivat jälleen kirjoitustyökalun läpi: siksi viimeinen estosääntö alla.

**Miksi se meni läpi:** kielto, jonka onnistuminen näyttää samalta kuin sen rikkoutuminen. Vihreä
CI oli todiste siitä, ettei sivulla ole versionumeroita, ja yhtä hyvin siitä, ettei tarkistus
tarkista mitään. Testaus tehtiin erillisessä ajossa, ei siinä tiedostossa joka jäi elämään.

**Estosääntö:**
- Jokaisella kieltävällä tarkistuksella on itsetesti samassa tiedostossa: lista merkkijonoja
  joiden on osuttava ja lista joiden ei saa osua. Tarkistus kaatuu, jos oma testi ei mene läpi.
- "Testattu" CHANGELOGissa tarkoittaa testiä, joka on commitoitu ja ajetaan uudelleen joka
  ajossa. Kertaluontoista kokeilua ei kirjata todisteeksi.
- Kun kuvio sisältää kenoviivoja, sen tavut tarkistetaan tiedostosta kirjoittamisen jälkeen
  (`cat -A` tai vastaava), ei vain sitä miltä se näytti editorissa.

## 19.9.2026: kaksi julkista pintaa erosivat toisistaan vuorokaudessa

**Mitä tapahtui:** V5 julkaistiin 18.9. ja samana päivänä profiili-README täytettiin toisessa
repossa. Seuraavana aamuna sivu ja README sanoivat eri asian viidestä faktasta (ReviewGlassin
lisenssi, SF3D:n vuodet, SpectralForgen tila, MasterForgen alkuvuosi, Quaesitorin olemassaolo).
Yksi ero oli READMEn vika (2008), yksi sivun (ReviewGlass), yksi molempien (2023). Kumpikin pinta
oli tarkistettu erikseen tuoterepoista, mutta ei toisiaan vasten, ja ReviewGlassin repo muuttui
julkiseksi sivun julkaisun jälkeen samana iltana.

**Estosääntö:**
- Sessiorutiinin faktatarkistus kattaa sivun lisäksi profiili-READMEn: samat tuotteet, samat
  tilat, samat vuodet. Ero on korjattava ennen kuin sessio päättyy, kumpaan tahansa suuntaan.
- Fakta, joka elää kahdella julkisella pinnalla, kuuluu yhteen lähteeseen (adr.sws.014,
  proposed). Kunnes se on rakennettu, tarkistus tehdään käsin joka sessiossa.
- Kun toinen repo muuttuu julkiseksi (tai sen tila muuttuu), sivun vastaava rivi tarkistetaan
  samassa sessiossa, ei seuraavassa.

## 18.9.2026: suositus ei ole päätös ennen kuin se on luettu ääneen

**Mitä tapahtui:** kahdessa kysymyslaatikossa vaihtoehto "Recommended" sisälsi otsikon, jonka olin
itse muotoillut ("Products in production, and the control plane that runs them", "Smaller products,
tools and experiments"). Petri valitsi vaihtoehdon, koska se oli suositus, mutta otsikon sanoja ei
ollut luettu erikseen. Livenä mockupissa hän huomasi, että "control plane" oli vanhaa Atlas-kieltä
ja "Smaller" minun sanani. Kumpaakaan ei ollut päätetty yhdessä.

**Estosääntö:**
- Kun vaihtoehto sisältää uuden tekstin, teksti näytetään sanatarkasti kysymyksessä eikä vain
  vaihtoehdon kuvauksessa, ja se merkitään "minun ehdotukseni", ei "nykyinen".
- Sivulle näkyvä otsikko on aina oma kohtansa, ei niputettuna osiomerkin kanssa.
- Kun aiempi päätös muuttaa jonkin kuvauksen (Atlas ei ole enää control plane), etsi sama sana
  muualta listasta ennen seuraavaa laatikkoa.

## 17.9.2026: headless-selain palaa ennen kuin kuva on kirjoitettu

**Mitä tapahtui:** kuvakaappausskripti poisti väliaikaisen selainprofiilin heti prosessin
palattua, ja Edge kirjoitti PNG:n vasta sen jälkeen. Osa kuvista syntyi, osa ei, ja skripti
raportoi "FAIL" kuvista jotka ilmestyivät hetkeä myöhemmin. Kolme diagnoosikierrosta meni
selaimen lippujen ja verkon epäilyyn ennen kuin tiedostojen aikaleimat paljastivat syyn.

**Estosääntö:**
- Kun työkalu tuottaa tiedoston, valmis-väite tarkistetaan tiedostosta (olemassa, koko ei enää
  kasva), ei prosessin paluuarvosta.
- Ennen kuin epäilet ympäristöä (verkko, liput, sandbox), katso mitä levylle on oikeasti tullut
  ja milloin.

## 17.9.2026: sessio lähti tekemään ennen kuin pelisäännöt oli sovittu

**Mitä tapahtui:** repo oli ilman CLAUDE.md:tä ja sessiorutiinia. Ensimmäinen sessio tulkitsi laajan
tehtävänannon (dokumentaatio, sisältö, ulkoasu, historia, GitHub) luvaksi tehdä kaikki kerralla: se
oli kirjoittamassa index.html:n uusiksi, ehdotti kahdenkymmenen SF3D-kuvan poistoa ja kirjasi omia
muotoiluvalintojaan "hyväksytyiksi" päätöksiksi. Petri keskeytti: sivua muokataan vain yhdessä
suunnittelun päätteeksi, SF3D:tä ei pyydetty poistamaan vaan sen rooli suunnitellaan uudelleen, ja
mitään ei päätetä ennen mockup-kuvia. Ehdotukset olivat asiallisia; järjestys oli väärä.

**Estosääntö:**
- Repo ilman protokollaa saa ensin protokollan (CLAUDE.md, sessiorutiini), sitten vasta työn.
- Laaja tehtävänanto on suunnittelun aloitus, ei toteutuslupa. Sivun muutoksesta tehdään ensin
  mockup (`docs/mockups/`, ei koskaan live-sivu), katsotaan yhdessä, päätetään, sitten muokataan.
- Ohje "piiloon" tai "pienemmäksi" ei tarkoita "pois". Kun ohje koskee näkyvyyttä, ehdotetaan
  vaihtoehtoja eikä valita niistä itse.
- Päätöstietue saa tilan `accepted` vain Petrin sanomana. Session oma muotoilu on `proposed` tai
  `open`, ja tietue sanoo kumpi osa on Petrin ohje ja kumpi session ehdotus.
- Kysymyslistaa ei anneta kerralla kymmenen kohdan nippuna alkuselvitysten keskelle; ensin
  selvitykset ja mockupit, sitten päätökset yksi kerrallaan.

## 17.9.2026: "Launching within the month" seisoi sivulla viisi kuukautta

**Mitä tapahtui:** SEED lukittiin 18.4.2026 ja sivu julkaistiin V4.5:nä. Luviamon tila sanoi
"Launching within the month", Quaesitorin versio oli 2.12.11 ja MasterForgen hinnoittelu "free to
fourteen-ninety-nine". Syyskuussa 2026 Luviamo oli ollut tuotannossa kuukausia (v0.385.0 todennettu
16.9.), Quaesitor oli 2.13.27, MasterForge 4.44.0 ja Starter v2 oli juuri julkaistu. Kukaan ei
huomannut, koska mikään ei pakottanut katsomaan: repolla ei ollut sessiorutiinia, CHANGELOGia eikä
BUILD_INFOa, ja "lukittu" SEED luettiin niin ettei sitä tarvitse avata.

**Estosääntö:**
- Suhteellinen aikailmaus sivulla on virhe, ei tyylivalinta. Jokainen tila kantaa version tai
  päivämäärän (adr.sws.004). Tarkistusskripti kieltää sanat "coming soon", "within the month" ja
  "recently".
- Footerissa on revisiopäivä ja CI vertaa sitä `BUILD_INFO.updated`-kenttään: vanhentunut sivu on
  näkyvästi vanhentunut, ei sanamuodon taakse piilotettu.
- "Lukittu" koskee suuntaa, ei sisältöä. Sisältö tarkistetaan tuoterepojen BUILD_INFOsta ja
  live-sivuilta jokaisessa sessiossa, ja CHANGELOG sanoo mitä tarkistettiin ja milloin.

## 17.9.2026: jonossa ollut korjaus odotti viisi kuukautta, koska sillä ei ollut paikkaa

**Mitä tapahtui:** SEED §7 kirjasi 18.4. korjauksen "2008–2016 → 2006–2016" tehtäväksi "React-buildin
ensimmäisenä muokkauksena". React-buildia ei tullut, joten korjausta ei tullut. Yhden rivin muutos
oli sidottu vaiheeseen, jota ei koskaan aloitettu.

**Estosääntö:**
- Avoin asia elää `BUILD_INFO.next`-listassa, ei SEEDin luvussa eikä tulevan vaiheen ehdollisena.
- Yhden rivin korjaus tehdään heti, ei "seuraavassa buildissa". Tässä repossa ei ole buildia.
- Korjatut virheet lisätään tarkistusskriptin kiellettyihin merkkijonoihin, jottei niitä kirjoiteta
  takaisin vahingossa.

## 17.9.2026: Atlas tiesi sivustosta enemmän kuin sivuston oma repo

**Mitä tapahtui:** Atlaksen malli `sw-sivusto` kantoi kaksi ADR:ää (adr.sws.001 ja 002) ja
rationalen, joita repo itse ei sisältänyt missään muodossa. Päätökset olivat peilissä, eivät
lähteessä, ja README lupasi React-siirtymää jota Atlaksen ADR piti ehdollisena.

**Estosääntö:**
- Päätös kirjoitetaan ensin repon `docs/decisions/`-kansioon ja peilataan Atlakseen
  ehdotuskanavan kautta, ei toisin päin. Totuushierarkia on sama kuin muissa Sunrise-repoissa
  29.7.2026 alkaen: repo `main` on dokumenttien totuus, Atlas on peili.
- Kun Atlas-MCP ei ole tavoitettavissa (17.9.2026: 401), peilaus kirjataan `BUILD_INFO.next`-listaan
  eikä jätetä muistin varaan.
