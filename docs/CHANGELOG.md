# CHANGELOG (Sunrise Software site)

Sessiokohtainen muutosloki, uusin ensin. Tila on `BUILD_INFO.json`:ssa, avoimet asiat sen
`next`-listassa, päätökset `decisions/`-kansiossa. Tämä tiedosto kertoo mitä tehtiin ja miksi.

## Sessio 10, jatko 2 (13.11.2026): `/hometeam/`-sivu (kierros AD, PR F)

**Tehty yhdessä Petrin kanssa** Petrin sanasta "Rakennetaan nyt". Rakennusaikaiset valinnat kysyttiin
yhdellä laatikkokierroksella (AD, neljä kysymystä, kuvana `docs/mockups/hometeam/round-AD-page.jpg`), ja
kaikki neljä hyväksyttiin rakennettuina. Työ on haarassa `claude/hometeam-page`.

**Kaappaukset nimet vaihdettuina.** HomeTeamin `mockups/` ja kuvakansio kopioitiin tämän repon
ulkopuolelle, ja kopiota muokattiin (Y.3, AD.2): lapsen tervehdys ja lasten laatat saivat avatar-eläintensä
nimet (Kettu, Pingviini, Pupu), sukunimirivi poistettiin, `Hei, Petri!` jäi, ja pistetaulun valitun
vaihtoehdon (N2) alapalkista poistettiin rakentamaton "Ruoka". Viisi näkymää kaapattiin 2x-tarkkuudella
Playwrightilla (`docs/mockups/hometeam-capture.py`). Ensimmäisessä kaappauksessa mockupin oma varjo näkyi
kulmissa puoliläpinäkyvänä, joten varjo kytkettiin pois kaappauksen ajaksi. Kuvat tehtiin skriptillä
`docs/mockups/hometeam-images.py`: viisi WebP-kuvaa PNG-varakuvineen, 2x-lähteet `source-assets/`-kansioon
ja etusivun laatikon 16:9-kuva. Jakokuva on `docs/mockups/og-hometeam.html`:stä.

**Sivu.** `hometeam/index.html` on rakennettu `/reviewglass/`-sivun kehykselle. Rakennusskripti luki
tekstit HT.1–HT.16 osasta E ja pysähtyi, jos jokin rivi ei ollut päätetty. Kaksi virhettä korjattiin
ennen kierrosta: skripti luki ensin otsikoksi sarakkeen nimen `<title>`, ja kiitosrivi peri leipätekstin
koon. **Etusivu:** HomeTeam-laatikossa on nyt lapsen Tänään-näkymä piirroksen tilalla, linkki
`How my family uses it →` ja kuvateksti `hometeam · a child's today, a design mockup`. Piirroksen koodi
poistettiin, ja sitemap nimeää viisi osoitetta.

**Tarkistettu paikallisesti:** 1024 ja 1440 px: ei vaakavieritystä eikä konsolivirheitä, fontit ja kaikki
viisi kuvaa latautuvat, JSON-LD jäsentyy. 375 px laite-emuloinnilla: `scrollWidth` 375, mikään `main`-
elementissä ei ylitä reunaa, kuvapari 160 px:n levyisinä rinnakkain, rivi allekkain. Etusivun laatikko
375 px:n leveydellä linkkeineen ja kuvineen. `check-site` vihreä viidellä sivulla (37 paikallista
tiedostoa). Yhdessäkään commitoitavassa tekstitiedostossa ei ole sukunimeä eikä lasten nimiä, ja kuvat
katsottiin näkymä kerrallaan. BUILD_INFO 5.8.0.

## Sessio 10, jatko (13.11.2026): `/hometeam/`-sivun tekstit päätetty (kierrokset AA–AC, ei sivumuutosta)

**Tehty yhdessä Petrin kanssa** kolmella laatikkokierroksella (AA–AC, 12 kysymystä). Kaikki
suositukset hyväksyttiin sellaisinaan, joten `/hometeam/`-sivun kohdat HT.1–HT.16 ovat nyt päätetty
(`copy-v4-pages.md` osa E):

- **AA** leipäteksti: `What it does` (Today, Wallet ja talous, pelikerros), `Why it exists`
  (ensimmäisen version kaksi opetusta ja perheen äänestys), `Where it stands` (käytössä 29.9.2026 alkaen,
  vain sallitut osoitteet, yksityinen repo, data EU:ssa, sovellus suomeksi); kolmen kuvan kuvatekstit.
- **AB** `<title>` `HomeTeam: the application my family runs the week on · Petri Korhonen`, kuvaus,
  aihemerkki `HomeTeam · my own family`, todistelohkon rivi `No public link: ...`.
- **AC** jakokuva muiden sivujen rakenteella, JSON-LD:ssä vain `WebPage` (C.3 pysyy), etusivun linkki
  `How my family uses it →` ja kuvan kuvateksti, kiitosrivi fonteille (OFL) ja Fluent Emoji -kuville
  (MIT; lisenssi luettu `microsoft/fluentui-emoji`-reposta).

Jokainen väite on luettu samana päivänä HomeTeamin reposta ja koodista (osan E kaksi listaa). Sivuja ei
muutettu. BUILD_INFO 5.7.0. **Seuraavaksi PR F:** `/hometeam/`-sivu rakennetaan yhdessä Petrin kanssa.

## Sessio 10 (13.11.2026): `/hometeam/`-ketju alkoi, kuvitus ja ensimmäiset tekstit päätetty (kierrokset Y–Z), etusivun HomeTeam-laatikon virhe korjattu

**Alkutarkistus palvelukatkojen päivänä:** session 9 työ meni perille. Avoimia PR:iä ei ole; `main` on
`e5bc2d2` ja CI vihreä jokaisessa session 9 commitissa. Cloudflare Pages raportoi onnistuneen buildin
commiteille `975dda7`, `f8ac691` ja `e5bc2d2`. Livestä: `/silent-context/`, `/rooms/`, `/reviewglass/` ja
sitemap tavu tavulta samat kuin main, `og-reviewglass.jpg` ja `og-rooms.jpg` 200, `data-revised="2026-11-13"`,
`/hometeam/` 404. Etusivu eroaa mainista vain Cloudflaren sähköpostisuojauksen kahdessa mailto-linkissä ja
sen skriptissä (jo `BUILD_INFO.next`:ssä). Atlaksen `sw-sivusto.STATUS` v22 löytyi. Työpuissa ei ole
keskeneräistä: vanhan työpuun kaksi commitia ovat PR #8:n pää, joka on squash-mergattu.

**Kierros Y yhdessä Petrin kanssa** Petrin sanasta "hometeam repossa on paljon mockuppeja, joten käytetään
niitä kuvituksessa sivulla". Luettu HomeTeamin reposta (`origin/main` `1c98b23`, muuttunut viimeksi
10.10.2026, joten osan A3 faktat 11.11. pitävät): `mockups/README.md` ja sen 21 mockupin taulukko.
Kymmenen mockupia kuvattiin 1440 px:n leveydellä, ja valituista vaihtoehdoista leikattiin yhdeksän
ehdokasnäkymän arkki. Arkki jäi scratchpadiin, koska kolmessa näkymässä on oikeita nimiä (perheen sukunimi
ja kolmen lapsen etunimet), ja tämä repo on julkinen. Päätökset (`copy-v4-pages.md`, kierros Y):

- **Y.1** pääkuvana lapsen ja aikuisen Tänään rinnakkain, leipätekstin jälkeen Wallet, pistetaulu ja
  aarresaari; pysäytyskuvat 2x, WebP + PNG.
- **Y.2** näkymät suomeksi sellaisinaan, jokaisen alla englanninkielinen kuvateksti, ja sivulla rivi siitä,
  että sovellus on suomeksi.
- **Y.3** `Hei, Petri!` saa jäädä; sukunimi ja lasten nimet vaihdetaan mockupien omiin nimimerkkeihin
  kaappauskopiossa repon ulkopuolella. Mikään nimellinen kuva tai lähdetiedosto ei tule repoon.
- **Y.4** etusivun HomeTeam-laatikon piirros (B.3, 11.11.) vaihtuu lapsen Tänään-näkymään PR F:ssä.

**Päätös:** adr.sws.020 (hyväksytty) sallii HomeTeamille mockup-näkymät ja kirjaa nimisäännön. CLAUDE.md:n
piirrettyjen instrumenttien sääntö ei enää nimeä HomeTeamia, ja siihen kirjattiin Petrin linja muille
tuotteille. SEED v4.1.0 (luvut 2.2, 7 ja 8), apps-v3 (HomeTeamin rivi ja B.6b) ja päätösindeksi päivitetty.
**Seuraavaksi** tekstikierros Z: kuvatekstit, suomen kieli -rivi, miten sivu sanoo näkymien olevan
suunnitelmia eikä tuotannon kaappauksia, ja fonttien (OFL) ja Fluent Emoji -kuvien (MIT) maininta. BUILD_INFO 5.6.0.

**Kierros Z ja virhe livesivulla.** Ennen tekstikierrosta `/hometeam/`-sivun faktat luettiin HomeTeamin
koodista eikä vain kuvauksista (`routes.tsx`, `moduleOptions.ts`, `i18n.ts`, `apps/api/src/family/index.ts`,
BACKLOG, `product.md`, `v1-reference.md`; `app.hometeam.fi` ja `hometeam.fi` 200). Löytyi virhe:
etusivun HomeTeam-laatikko (3.43, livenä 12.11. alkaen) lupaa ateriat ja kauppalistan, joita ei ole
rakennettu (`/ruoka` on paikkamerkki, kauppalistalla ei ole sivua, KOORD-2 ja -3 kohdassa "Myöhemmin").
11.11. tarkistus luki README:n kuvauksen, joka on suunnitelma; LESSONS 13.11.2026. `/hometeam/`-sivun
tekstiehdotukset HT.1–HT.16 kirjoitettiin osaan E (`HT.n`, koska `H.n` ovat `/silent-context/`-sivun
kierroksen H päätöksiä), ja faktat kahtena listana: rakennettu ja tuotannossa, ei rakennettu.
Kierros Z (neljä kysymystä, kaikki suositukset hyväksytty):

- **Z.1** laatikon leipäteksti korjataan heti omalla PR:llä: `A shared Today view for the day's tasks and
  the family calendar, and an economy ...` (muu teksti ennallaan). Etusivun muu osa odottaa PR F:ää.
- **Z.2** h1 `The application my family runs the week on. My children voted on how it looks.`
- **Z.3** ingressi ehdotuksen mukaan (HT.6).
- **Z.4** pääkuvan kuvateksti `Design mockups, not captures: a child's Today and a parent's, in Finnish
  as the application is. A capture would show my family's own week.`
- **Z.5** (kysytty, kun PR #14:n esikatselua katsottiin) laatikon piirros lupasi samaa: alarivi
  `TASKS · CALENDAR · MEALS · SHOPPING · HOMECOIN` ja tehtävät `Tacos for dinner` ja `Milk, bread, apples`.
  Korjattu samaan PR:ään: alarivi `TASKS · CALENDAR · WALLET · HOMECOIN`, tehtävät `Take out the rubbish` ja
  `Make the bed`.

**Sivumuutos:** `index.html`:n HomeTeam-laatikon leipäteksti (Z.1) ja piirroksen alarivi ja kaksi tehtävää (Z.5). Alatunnisteen päivä on jo 2026-11-13,
joten se ja sitemap pysyvät. Profiilin README (push 24.9.2026) mainitsee HomeTeamin vain perhekartassa
eikä lupaa aterioita, joten F2 pysyy ennallaan. BUILD_INFO 5.6.1. **Seuraavaksi** kierrokset AA alkaen:
HT.1–HT.4 ja HT.9–HT.16.

**Deploy:** PR #14 squash-mergattu Petrin sanasta 13.11.2026 17:43Z (`bac9f62`). Cloudflaren tuotantobuild
(`0df20e7a`) valmistui 17:43:53Z, ja livesivu tarjosi korjatun laatikon 17:44Z. Livestä todennettu:
laatikon teksti ja piirroksen alarivi ja tehtävät uudet, aterioita ja kauppalistaa ei mainita missään
(ainoa osuma on piirroksen koodikommentti, joka kertoo korjauksesta), `data-revised="2026-11-13"`.
Etusivu eroaa mainista vain Cloudflaren sähköpostisuojauksen kahdessa mailto-linkissä ja sen skriptissä.
`/silent-context/`, `/rooms/`, `/reviewglass/` ja sitemap tavu tavulta samat kuin main. Atlaksen
`sw-sivusto.STATUS` v24.

## Sessio 9, päätös (13.11.2026): ketju paketoitu, seuraavaksi `/hometeam/`

**Petrin linja ketjun lopuksi:** "Oikeat mockupit sovelluksesta täytyy saada sivuille, mutta review glass
kohdalla se täytyy rakentaa muuten kuin kuvankaappauksella koska itse suurennuslasi katoaa kun otetaan
kuvankaappaus." Tarkistettu ReviewGlassin reposta: lasi, sen halo ja etsin sulkevat itsensä pois
kaappauksesta (`WDA_EXCLUDEFROMCAPTURE`, jotta lasi ei kuvaa itseään), ja kaappaukseen näkyvät vain dokki
ja sen laatikko (adr.rg.025). Linja muuttaa CLAUDE.md:n piirrettyjen instrumenttien sääntöä ja apps-v3:n
kohtaa B.5, joten tapa päätetään Petrin kanssa tuote kerrallaan ja kirjataan päätöstiedostoon. Siihen asti
`/reviewglass/` pitää piirroksen (RG.8, X.1). Kirjattu `BUILD_INFO.next`:iin, SEEDin lukuun 8 ja
`copy-v4-pages.md`:n osan D loppuun.

**Session 9 tulos:** `/rooms/` (PR #10 ja #11) ja `/reviewglass/` (PR #12 ja #13) ovat livenä ja livestä
todennettuja; nimi ReviewGlass kirjattiin pysyväksi myös ReviewGlassin repoon ja Atlakseen. **Seuraava
ketju** aloittaa `/hometeam/`-sivun tekstikierroksesta (`copy-v4-pages.md` osa E), ja oikea mockup on
mukana alusta asti. BUILD_INFO 5.5.1; sivuihin ei koskettu, joten alatunnisteen päivä ja sitemap pysyvät.
Atlaksen `sw-sivusto.STATUS` v22.

## Sessio 9, jatko 3 (13.11.2026): `/reviewglass/`-sivu (kierros X, PR E)

**Tehty yhdessä Petrin kanssa** Petrin sanasta "Rakennetaan /reviewglass/-sivu". Rakennusaikaiset valinnat
kysyttiin yhdellä laatikkokierroksella (X, kolme kysymystä, kuvana
`docs/mockups/reviewglass/round-X-page.jpg`), ja kaikki kolme hyväksyttiin rakennettuina. Työ on haarassa
`claude/reviewglass-page`.

**Deploy, ensimmäinen yritys:** PR #13 squash-mergattu 13.11.2026 15:28Z Petrin sanasta (`1ad52ba`) CI:n ollessa
vihreä. Cloudflaren tuotantobuild käynnistyi 15:28:55Z mutta jäi tilaan "Building", koska Cloudflaren
Workers API -häiriö alkoi 15:31Z (tilasivu: korjaus asennettu 15:42Z). Kello 16.09Z deploymentin oma osoite
`d3236b51.sunrisesoftware-site.pages.dev` antoi 404:n kaikille poluille, ja Pagesin API vastasi 503 "no
healthy upstream". Live jäi edelliseen revisioon ehjänä: etusivu ei linkittänyt uuteen sivuun, eikä
sitemap nimennyt sitä. Tämä kirjaus mainiin käynnistää uuden tuotantobuildin samalle sisällölle.

**Deploy:** kirjauscommitin `975dda7` build (`3ae502fd`) jäi ensin jonoon jumiutuneen buildin taakse ja vei
sivun tuotantoon 16:30Z; `d3236b51` ei valmistunut koskaan. Livestä todennettu 16:30Z alkaen: `/reviewglass/`
200 ja tavu tavulta sama kuin main, kanoninen osoite, `og:image`, `data-revised="2026-11-13"`, JSON-LD
WebPage ja SoftwareSourceCode; `images/og-reviewglass.jpg` `image/jpeg` ja sama; sitemap neljällä
osoitteella ja sama; `/rooms/` ja `/silent-context/` samat; tuntematon osoite 404. Etusivulla linkki
`How the glass works →`, fakta `Screen pixels never leave the machine` (vanha poissa) ja `#reviewglass`
rakenteisessa datassa; etusivu eroaa mainista vain Cloudflaren sähköpostisuojauksen kahdessa
mailto-linkissä ja sen skriptissä, jotka ovat jo `BUILD_INFO.next`:ssä. Lasin liikettä ei nähty
selaimessa, koska selainpaneeli oli piilossa; se jää Petrin silmälle. Atlaksen `sw-sivusto.STATUS` v21.

**Sivu.** `reviewglass/index.html` rakennettu kohdista RG.1–RG.14 sanasta sanaan `/rooms/`-sivun
kehyksellä. Rakennusskripti luki tekstit `copy-v4-pages.md`:n osasta D ja pysähtyi, jos jokin rivi ei
ollut päätetty. Päämediana on etusivun §03-piirros 16:9-kehyksessä sarakkeen levyisenä, piirrettynä
sivun omalla kopiolla etusivun canvas-koodista (X.1). Ensin näkyy etusivun pysäytyskuva, ja lasi liikkuu
vain kehyksen ollessa näkyvissä; liikettä vähentäessä ja `?static=1`:llä näkyy pelkkä pysäytyskuva.
Jakokuva `images/og-reviewglass.jpg` on tehty `/rooms/`-kuvan tapaan, ja h1 on kolmella käsin katkaistulla
rivillä, joista viimeinen `--sun-deep`-värissä (X.3). **Etusivu:** ReviewGlass-laatikon toinen fakta on nyt
`Screen pixels never leave the machine` (RG.15), koska vanha `Nothing leaves the machine` ei pidä paikkaansa
Explainin etäversion ollessa päällä. Laatikkoon tuli linkki `How the glass works →` ennen repolinkkiä:
työpöydällä rinnakkain ja puhelimella allekkain (RG.14, X.2). Rakenteiseen dataan tuli
`SoftwareSourceCode` `#reviewglass` (RG.13), ja sitemap nimeää neljä osoitetta. Etusivun muut tekstit
eivät muuttuneet.

**Tarkistettu rakennuspäivänä:** ReviewGlassin repo `origin/main` `2654ab4` (kierroksen jälkeen vain
oma nimikirjaukseni): README ja BUILD_INFO (sessio 11), GitHubin API (julkinen, Apache-2.0, ei julkaisuja
eikä tageja, kielet). RG.9–RG.11 pitävät sellaisinaan. **Profiilin README** (`pkorrrhonen-cmd`, 24.9.2026)
sanoo ReviewGlassista "and later a live diff", vaikka live diff on rakennettu ja sivu sanoo niin. README
on Petrin, joten ero kirjattiin `BUILD_INFO.next`:iin.

**Tarkistettu paikallisesti:** 1440 px: ei vaakavieritystä, ei konsolivirheitä, fontit latautuvat,
JSON-LD jäsentyy (WebPage, SoftwareSourceCode), piirros täyttää 820x461-kehyksen. 375 px laite-emuloinnilla:
`scrollWidth` 375, mikään ei ylitä reunaa, navissa vain aurinkomerkki; etusivun laatikon linkit allekkain.
`node scripts/check-site.mjs` vihreä: neljä sivua, 30 paikallista tiedostoa.

**Korjattu kesken:** otin vertailukuvan puhelinsarakkeen ensin `shoot.py`:llä 375 px:n leveydellä, vaikka
LESSONS 13.11. kieltää sen. Kuvassa teksti leikkautui oikeasta reunasta. Huomasin sen ennen kuin kuva
näytettiin Petrille, otin sarakkeen uudelleen selainpaneelista, ja nyt `shoot.py` kieltäytyy alle 500 px:n
leveydestä. SEED v4.1.0:n 2.2, 3.6, 4, 5.2, 7 ja 8 päivitetty; copy-v3:n 3.24 ja 3.24b osoittavat
korvaaviin kohtiin. BUILD_INFO 5.5.0.

## Sessio 9, jatko 2 (13.11.2026): `/reviewglass/`-sivun tekstit päätetty (kierrokset S–W, ei sivumuutosta)

**Tehty yhdessä Petrin kanssa** viidellä laatikkokierroksella (S–W, 18 kysymystä), kohdat RG.1–RG.15
`copy-v4-pages.md`:n osassa D. Sivua ei rakennettu. Kierros R jätettiin väliin, koska R.n ovat
`/rooms/`-sivun kohtia, ja kohdat ovat RG.n eivätkä G.n, joka sekoittuisi silent-contextin kierrokseen G.

**Päätetty.** Isot linjat ensin (S): sivu tehdään nyt, koska **Petrin mukaan nimi ReviewGlass on ja pysyy**,
ja ReviewGlassin repon merkintä nimen avoimuudesta (adr.rg.008 *proposed*, NAME-CLEARANCE, README:n
"gated on the name") oli vanha; AvoQ:ta ei mainita (K.4). Petrin pyynnöstä päätös kirjattiin samana
päivänä myös ReviewGlassiin ja Atlakseen: adr.rg.008 hyväksytty mallissa (Atlas #673, `a757696`,
molemmat workerit deployattu) ja ReviewGlassin README, CLAUDE.md, BUILD_INFO ja NAME-CLEARANCE
korjattu (`2654ab4`); spec seuraa versiossa 0.5. Claude Code nimetään ja README:n
riippumattomuuslause sanotaan. Päämedia on §03:n piirros suurennettuna. **Etusivun laatikon fakta
`Nothing leaves the machine` oli epätosi**, kun Explainin etäversio on päällä, ja se korjataan sivun
mukana muotoon `Screen pixels never leave the machine` (RG.15). Otsikko on "A glass for reading what the
AI agent writes, while it is writing." Runko: What it does, What it keeps, and what it does not, Where it
stands. Todisteena repo, etusivulle laatikkoon linkki `How the glass works →`, rakenteinen data
WebPage ja SoftwareSourceCode (myös etusivulle).

**Korjattu kesken kierroksen:** merkitsin statusrivin (RG.7) päätetyksi kierroksella S, vaikka sitä ei
ollut kysytty; palautin sen luonnokseksi ja kysyin kierroksella U ennen kuin mitään rakennettiin.

**Tarkistettu tässä sessiossa:** ReviewGlassin repo `origin/main` (`45609db`): README, BUILD_INFO
(sessio 10, 12.11.), CHANGELOG (172 testiä), ADR:t 001–036 (otsikot ja 006, 007, 024 päätösosat),
NAME-CLEARANCE; GitHubin API (julkinen, Apache-2.0, ei julkaisuja eikä tageja, kielet); Atlas
`reviewglass.STATUS` v38; etusivun piirroksen koodi (mitä aria-label kuvaa). **Ristiriita kirjattu:**
repon README sanoo repon julkiseksi 17.9.2026, tämän sivuston LESSONS 18.9. illalla; sivu ei tarvitse
päivää. `node scripts/check-site.mjs` vihreä. SEED v4.1.0:n 2.2, 4 ja 8 päivitetty. BUILD_INFO 5.4.2.

## Sessio 9, jatko (13.11.2026): `/rooms/`-sivu ja sen mediat (kierrokset P ja Q, PR D)

**Tehty yhdessä Petrin kanssa** kahdella laatikkokierroksella (P, neljä kysymystä, vertailukuvana
`docs/mockups/rooms/round-P-media.jpg`; Q, kaksi kysymystä, kuvana `docs/mockups/rooms/round-Q-page.jpg`).
Työ on haarassa `claude/rooms-pr-d`.

**Sivu.** `rooms/index.html` rakennettu kohdista R.1–R.14 sanasta sanaan `silent-context`-sivun kehyksellä;
muuttuivat vain statusrivin pallo (infrastruktuurin meri, kuten Atlas-laatassa), videolohko ja yksi lyhyt
skripti. R.12:n luvut luettiin Atlaksesta uudelleen rakennuspäivänä noin klo 12.30, eivätkä ne olleet
muuttuneet (335 ja 90, ensimmäinen testi 20/20 ilman kumoutuneita, tiukempi 0/20, Jev 272/309).
Etusivun Atlas-laattaan tuli nappi `How the decision rooms work →` hiljaisen tekstin eteen, ja sitemap
nimeää kolme osoitetta. **Päätetty rakentaessa (kierros Q), molemmat kuten rakennettu:** työpöydällä
16:9-video sarakkeen levyisenä ja kuvateksti sarakkeen reunassa, puhelimella (alle 600 px) 9:16-leikkaus
posteineen 420 px:n kehyksessä ja kuvateksti keskellä, leikkauksen valitsee skripti kerran latautuessa
ja ilman JavaScriptiä toistuu 16:9 (Q.1); Atlas-laatan napit vierekkäin linkki ensin, puhelimella
allekkain (Q.2). Pystyleikkaus ja sen posteri ovat videon `data-src`- ja `data-poster`-määritteissä, joten
`check-site.mjs` tarkistaa niiden olemassaolon. SEED v4.1.0:n luvut 2.2, 3.6, 7 ja 8 päivitetty.
BUILD_INFO 5.4.0.

**Tarkistettu paikallisesti:** 1440 px: ei vaakavieritystä, ei konsolivirheitä, kolme fonttia latautuu,
JSON-LD jäsentyy (WebPage, VideoObject), 16:9-video toistuu 1920x1080:na ja ensimmäinen tekstitysrivi
näkyy, `.vtt` tulee `text/vtt`:nä. 375 px laite-emuloinnilla: `scrollWidth` 375, mikään ei ylitä reunaa,
9:16-leikkaus ja sen posteri valittu, navissa vain aurinkomerkki; etusivun Atlas-napit allekkain.
Kelausta ei voitu kokeilla paikallisesti, koska Pythonin palvelin ei vastaa osapyyntöihin; se
tarkistetaan esikatselussa. `node scripts/check-site.mjs` vihreä: kolme sivua, 29 paikallista tiedostoa.

**Mediat (kierros P).** Videot kopioitiin sellaisinaan (P.1): `media/rooms-en.mp4` (1920x1080, 6 448 529
tavua) ja `media/rooms-en-916.mp4` (1080x1920, 5 855 181 tavua). Ne olivat jo verkkovalmiita (moov ennen
mdatia) ja samaa kokoluokkaa kuin silent-contextin uudelleenkoodattu video, eikä pienempi kuva olisi
pitänyt huoneen pientä mono-tekstiä luettavana. Posteriksi molempiin leikkauksiin BLIND-kortti 23
sekunnin kohdalta (P.2): huoneen tehtävä ja vaihtoehdot ja rivi "Not in the task: the owner's choice, a
recommendation.", eli ingressin asia yhdellä silmäyksellä; ei huoneen tulosta (sf3d.fi:n posteri,
tiheä 820 px:n kehyksessä) eikä loppukorttia (tyhjä 16:9:ssä ja näyttää yhden tuomarin). Jakokuva
`images/og-rooms.jpg` luonnoksen mukaan (P.3): h1 58 px:nä neljällä käsin katkaistulla rivillä, toinen
lause `--sun-deep`-värissä, lähde `docs/mockups/og-rooms.html`. Tekstitys `media/rooms-en.vtt` on labran
tiedosto sellaisenaan ja päällä oletuksena (P.4), koska videossa ei ole tekstiä kuvassa.

**Deploy:** PR #11 squash-mergattu 13.11.2026 12:26Z (`3192d6b`) Petrin sanasta CI:n ollessa vihreä
(Site checks ja Cloudflare Pages). Ennen mergea preview `claude-rooms-pr-d.sunrisesoftware-site.pages.dev`
tarkistettu: sivut, sitemap, posterit, jakokuva ja `.vtt` tavu tavulta samat kuin paikallisesti
tarkistetut, `.vtt` `text/vtt`:nä, pystyleikkaus toistuu tekstityksen kanssa puhelinleveydellä, ei
konsolivirheitä, tuntematon osoite 404. Livestä todennettu 12:27Z alkaen: `/rooms/` 200 ja tavu tavulta
sama kuin main, kanoninen osoite, `og:image`, `data-revised="2026-11-13"`, JSON-LD WebPage ja VideoObject;
molemmat videot 206 osapyyntöön (`content-range bytes 0-1023/6448529` ja `/5855181`, `video/mp4`,
immutable) ja tavu tavulta samat; `.vtt` `text/vtt`; posterit ja jakokuva `image/jpeg` ja samat; etusivun
Atlas-laatassa nappi `/rooms/`-sivulle; sitemap kolmella osoitteella; `/nonexistent-xyz/` 404. Kelaus
kokeiltu livessä selaimessa: 54,8 sekunnin kohdalla näkyy oikea tekstitysrivi. Päivä ei siirtynyt, joten
`uploadDate` 2026-11-13 pitää. Atlaksen `sw-sivusto.STATUS` v19.

**Medioista tarkistettu:** molemmat videot SHA-256:lla samoiksi kuin labran tiedostot ja `sf3d-media.pages.dev`:n
julkaisemat; atomijärjestys (faststart) tiedostosta; posterit ja jakokuva silmällä tehdyistä tiedostoista;
`.vtt` 27 riviä, UTF-8 ilman BOMia, LF. `node scripts/check-site.mjs` vihreä. SEED v4.1.0:n 5.2 ja 8
päivitetty. BUILD_INFO 5.3.2.

## Sessio 9 (13.11.2026): `/rooms/`-sivun tekstit päätetty (kierrokset K–O, ei sivumuutosta)

**Tehty yhdessä Petrin kanssa** viidellä laatikkokierroksella (K–O, 19 kysymystä), kohdat R.1–R.15
`copy-v4-pages.md`:n osassa C. Sivua ei rakennettu: se tehdään yhdessä, kun mediat ovat valmiit.

**Päätetty.** Otsikko on "Before I settle how my software is built, I ask a panel of AI models for a
second opinion." Ensimmäinen luonnos ("Before AI builds something hard to undo, ...") hylättiin (K.1):
sivu ei saa näyttää siltä, että rakentaminen on tekoälyn, vaikka koodin kirjoittaakin malli, koska työ
tehdään rakenteen varassa, ja tekstin on oltava helppotajuinen. Petrin suunta oli paneeli, jossa kaksi
eri malliperheen agenttia ja kaksi tuomarimallia antavat toisen mielipiteen; "settle" eikä "decide",
koska huone tarkistaa jo tehdyn valinnan sokkona ja erimielisyydessä päätän uudelleen. Ingressi kertoo
paneelin ensin ja sanoo lopuksi, että Atlaksessa paneelia kutsutaan huoneeksi. Statusrivi
`In use · 2026 →` kuten etusivun Atlas-laatassa. Runko: How a room is built (alan nimet selkeän lauseen
perässä, Clef sanottuna koekäytössä olevaksi), The room in the video (huone R-G, työpenkki nimeämättä),
The challenger (paholaisen asianajaja ja dialektinen inkvisitio lähteineen ja Nemethin varoitus), What
the record shows, and what it cannot (luvut, ensimmäisen ennakkorekisteröidyn testin raja, tiukempi
testi, tuomarin lempeys; luvut luetaan uudelleen rakennuspäivänä). Video näytetään sellaisenaan, ääni
sanotaan generoiduksi ilman työkalun nimeä, ja tekstitys on labran `rooms-en.vtt` sellaisenaan.
Todisteina kaksi huoneartikkelia. Etusivulle Atlas-laattaan nappi `How the decision rooms work →`.
Rakenteinen data WebPage ja VideoObject, `uploadDate` kuten J.4.

**Päätetty samalla, sivun ulkopuolelta (K.3):** Atlas ja Somnus tarvitsevat kumpikin oman alasivun.
Etusivulla ne ovat tuotteina, mutta piirretyt instrumentit ja kertomukset eivät tee niitä
ymmärrettäviksi; niiden tekstit ja tuotteet arvioidaan erikseen, kun sen aika on (`BUILD_INFO.next`).
Siksi `/rooms/` ei linkitä `why-i-built-atlas`-artikkelia.

**Löydetty tarkistaessa:**
1. **SEEDin 2.2 todistelista oli väärä.** `blind-to-anything-taken-away` (27.8.2026) on Somnuksen
   äänidetektorista, ei huoneista; se tuli listaan 11.11. otsikkonsa takia. Korjattu SEED v4.1.0:n lukuihin 2.2 ja 4
   tässä PR:ssä, ja LESSONSiin estosääntö.
2. **Videoiden polku oli kansion vajaa.** Renderit ovat `sf3d-ai-lab/media/publish/rooms/`-kansiossa, ja
   labran git ohittaa `media/`-kansion, joten ne ovat paikallisia renderöintejä (myös
   `sf3d-media.pages.dev/rooms/`, 200). SEED 5.2 ja 8 sekä `BUILD_INFO.next` korjattu tässä PR:ssä.
3. **"Noin joka viides" on vanhentunut.** 24.10. huone oli eri mieltä 30:ssä 147:stä; 13.11. 90:ssä
   335:stä, noin joka neljännessä. Ensimmäinen ennakkoon lukittu testi (H1) ei enää odota: se luki 20
   toteumaansa, eikä yksikään kumoutunut kummassakaan ryhmässä, joten se ei erottanut varmaa huonetta
   epävarmasta. Tiukempi H1 v4 (lukittu 27.10.) oli 0/20.

**Tarkistettu tässä sessiossa:** neljä artikkelia labran `origin/main`ista ja livestä (kaikki 200);
Atlas `ATLAS-HUONEET-KAR-ARV-20261031` v1 kokonaan (sanasto, 28 lähdettä; sanaa Delphi ei ole);
`atlas_decision_calibration` (limit 500) 13.11. noin klo 11.15; Atlaksen päätökset adr.atlas.043
(huoneen rakenne 22.9.), 072 (protokolla päälle 15.10.) ja 116 (haastaja 30.10.); `atlas.STATUS` v283;
huone R-G:n faktat artikkelista, labran `video/rooms/sources.md`:stä ja työpenkin reposta (ensimmäinen
gate-commit `c392dfb` 18.10. lukitsi julkaisuehdokkaan ja sääntötiedoston tiivisteen); molemmat videot
ffprobella (`rooms-en.mp4` 1920x1080, 118,08 s, 6 448 529 tavua; `rooms-en-916.mp4` 1080x1920,
5 855 181 tavua; ei tekstitystä kuvassa) ja kuvakoosteena; `rooms-en.vtt` (27 riviä). Profiili-README
ennallaan 24.9. jälkeen eikä mainitse huoneita; sivua ei muutettu, joten uutta eroa ei synny.
`node scripts/check-site.mjs` vihreä. BUILD_INFO 5.3.1.

## Sessio 8 (13.11.2026): `/silent-context/`, sivuston ensimmäinen alasivu, ja sen mediat (PR C)

**Tehty yhdessä Petrin kanssa** kahdella laatikkokierroksella (I ja J, `copy-v4-pages.md`).

**Mediat (kierros I).** Since AI -pystyvideo koodattiin uudelleen ffmpegillä: `media/silent-context-916.mp4`,
720x1280, H.264 High 3.1, CRF 25, BT.709, AAC 128 kb/s, faststart, 5,55 MB (lähde 1080x1920, 15,7 MB).
Videon pieni mono-teksti tarkistettiin luettavaksi tässä koossa. Posteri on avausruutu 1,5 sekunnin
kohdalta (oma kuva Turun salista videon otsikon alla), ei loppukortti eikä karttakohtaus. Jakokuva
`images/og-silent-context.jpg` (1200x630) on aiheleima ja otsikko aamutaivaalla `og-cover.jpg`:n
rakenteella, nyt sivuston omilla fonteilla (etusivun kuva tehtiin 18.9. Bahnschrift-sijaisfontilla);
lähde `docs/mockups/og-silent-context.html`. Pystyvideolle 9:16-kehys kaikilla leveyksillä, ja etusivun
merkintä 1 saa vain pillerin, ei pikkukuvaa.

**Sivu.** `silent-context/index.html` rakennettu kohdista SC.1–SC.14 sanasta sanaan: kehys etusivulta
(paletti, taivas, navi, paljastukset, lukuvalo, ranta), otsikkolohko, video posterineen, neljä runko-osiota,
todisteet (koodi ja demo) ja rakenteinen data (WebPage, SoftwareSourceCode, VideoObject). Todisteiden
osoitteista jätettiin pois nuolet, joita päätetyssä tekstissä SC.13 ei ole. Etusivulle merkinnän 1 pilleri
`Read the whole thing ↗` ja sama `SoftwareSourceCode`-entiteetti. Alaviitteet, sitemap (nyt kaksi
osoitetta) ja `BUILD_INFO.updated` 2026-11-13. BUILD_INFO 5.3.0.

**Päätetty rakentaessa (kierros J), kaikki kuten rakennettu:** rannalla vain vesi, takaisin-pilleri ja
alaviite (ei yhteystietolohkoa); sarake vasemmassa reunassa sanamerkin linjassa, ja puhelimella alle
420 px navissa pelkkä aurinkomerkki, koska sanamerkki ja takaisin-linkki eivät mahdu samalle riville;
statusrivin pallo aurinko, koska rivi on tulos eikä tuoteasteikon sana; VideoObjectin nimi videon oma
otsikko "What I built at Since AI" ja `uploadDate` 2026-11-13.

**SEED v4.1.0:** luku 3.6 kapeni viidessä kohdassa (pystyvideon kehys, §04:n posteri vain 16:9-videolle,
tuloksen aurinkopallo, alasivun navi puhelimella, alasivun ranta), 5.2 ja 5.8 päivitetty. v4.0.0
arkistoon. CLAUDE.md ja README osoittavat uuteen versioon; README:n tilaosio oli jäänyt 11.11. tilaan
("V6 is specified and not built") ja korjattiin.

**`check-site.mjs` tarkistaa nyt jokaisen sivun, jonka sitemap nimeää:** paikalliset tiedostot sivun
omasta hakemistosta tai juuresta, head, kanoninen osoite sivun omaan osoitteeseen, JSON-LD jäsentyy,
ajatusviivat, versionumerot, kielletyt merkkijonot, alaviitteen päivä sivun omaa `lastmod`ia vasten.
Gate kaatuu, jos levyllä on alasivu jota sitemap ei nimeä, jos etusivu ei linkitä alasivua tai jos
alasivulta puuttuu takaisin-painike. Kokeiltu rikottuun kopioon: viisi istutettua vikaa, viisi
kiinni. `--links` kysyy GETillä, kun palvelin kieltää HEADin (demo vastaa HEADiin 405).

**Tarkistettu tässä sessiossa:** `pkorrrhonen-cmd/silent-context` GitHubin API:sta (julkinen, MIT,
Python, tagi `submission` osoittaa `f36d5b1`:hen, README:n testiluvut 160, 13/13, 1/16 ja toistot
0, 0, 0, 1, 1), demo (GET 200, `/health` ok), lähdevideo ja koodattu video ffprobella, video
toistuu selaimessa 720x1280, `node scripts/check-site.mjs --links` (11 ulkoista linkkiä 200).
Profiili-README (`github.com/pkorrrhonen-cmd`) tarkistettu sivua vasten: ennallaan 24.9. jälkeen, eikä
mainitse Silent contextia eikä Since AI:ta, joten ero F6 on nyt README:n puolella (`copy-v4-pages.md` osa F).
Paikallisesti 1440 px ja 375 px: ei vaakavieritystä (scrollWidth 375), ei konsolivirheitä, fontit
latautuvat, JSON-LD kolme entiteettiä alasivulla.

**Deploy:** PR #9 squash-mergattu 13.11.2026 09:06Z (`0baab20`) Petrin sanasta CI:n ollessa vihreä
(Site checks ja Cloudflare Pages). Ennen mergea preview `30102275.sunrisesoftware-site.pages.dev`
tarkistettu: sen `/silent-context/`, etusivu ja video ovat tavu tavulta samat kuin paikallisesti
tarkistetut tiedostot. Preview-osoite vastaa videon osapyyntöön koko tiedostolla (200), samoin kuin
nykyiselle MasterForge-klipille, joten se on `pages.dev`:n ominaisuus. Livestä todennettu 09:06:48Z
alkaen: `/silent-context/` 200 ja tavu tavulta sama kuin tarkistettu tiedosto, kanoninen osoite, `og:image`
ja `data-revised="2026-11-13"`, JSON-LD kolme entiteettiä (WebPage, SoftwareSourceCode, VideoObject);
video 206 osapyyntöön (`content-range bytes 0-1023/5550573`, `video/mp4`, immutable) ja tavu tavulta sama;
posteri ja jakokuva 200 `image/jpeg`; etusivun pilleri vie `/silent-context/`-sivulle ja sen graafissa on
10 entiteettiä SoftwareSourceCode mukaan lukien; sitemap kahdella osoitteella ja `lastmod` 2026-11-13;
tuntematon osoite `/nonexistent-xyz/` 404. Päivä ei siirtynyt, joten `uploadDate` 2026-11-13 pitää.

## Sessio 7 (12.11.2026): PR B, ensimmäinen V6-muutos etusivulle

**Tehty yhdessä Petrin kanssa** tekstien pohjalta, jotka päätettiin 11.11. (`docs/design/copy-v4-pages.md`):
uusi osio **§04 Recent** "What I have been building, with dates." kahdella päivätyllä merkinnällä
(Since AI 2026, 8 Nov; As Prescribed, 18 Oct), Approach ja Correspondence numeroitu §05:ksi ja §06:ksi,
naviin **Recent** Productsin ja Approachin väliin, **HomeTeamin laatikko** ReviewGlassin jälkeen
(tila "in use · my own family", ei linkkiä, piirretty Today-näkymä: viisi geneeristä tehtävää
kuittautuu ja jokainen lähettää kolikon lompakkoon), headiin kuvakelinkit ja manifesti,
`max-image-preview:large`, `og:image:alt` ja `twitter:image:alt`, ja rakenteinen data adr.sws.019:n
mukaan (WebSite, Organization sameAs-listalla ja logolla, viisi SoftwareApplicationia, SF3D AI Lab
WebSitena, Person). Vanha käyttämätön HomeTeam-luonnos (putki ja kolikot) korvattiin. Alaviite,
`BUILD_INFO.updated` ja sitemapin lastmod 2026-11-12. BUILD_INFO 5.2.0.

**Päätetty rakentaessa (kierros D):** SF3D AI Lab tyypitetään WebSiteksi eikä sovellukseksi, koska se
on tutkimuslaboratorion sivusto; eilinen suositukseni oli väärä (LESSONS 12.11.2026). Kolme lisäystä
hyväksytty: `twitter:image:alt`, `Organization.logo` ja `publisher` sovelluksille.

**Ei vielä:** merkinnän 1 linkki `/silent-context/`-sivulle ja merkintöjen posterit tulevat sivun
omassa PR:ssä, koska sivua ei ole ja linkki vastaisi 404.

**Tarkistettu:** `node scripts/check-site.mjs` vihreä. Korjattu versiovahti löysi ensimmäisellä
oikealla ajollaan "SEED v4.0.0" -merkkijonon omasta CSS-kommentistani, ja se poistettiin. Rakenteinen
data jäsentyy (9 entiteettiä). Paikallisesti työpöytä- ja puhelinleveydellä: §04, navi, HomeTeamin
laatikko ja piirros, ei vaakavieritystä (375 px), ei konsolivirheitä, laatikoiden järjestys ja osioiden
numerot päätetyt.

**Deploy:** PR #7 squash-mergattu 12.11.2026 13:47Z (`14d267d`) Petrin sanasta CI:n ollessa vihreä
(Site checks ja Cloudflare Pages). Ennen mergea preview `c4e2b76a.sunrisesoftware-site.pages.dev`
tarkistettu: sen `index.html` on tavu tavulta sama kuin paikallisesti tarkistettu tiedosto, osiot §01:stä §06:een,
kuvakkeet ja manifesti oikeilla tyypeillä, tuntematon osoite 404, JSON-LD 9 entiteettiä. Livestä
todennettu noin minuutin kuluttua: `data-revised="2026-11-12"`, osiot §01:stä §06:een ja niiden joukossa §04 Recent, navissa
Products, Recent, Approach, Contact, HomeTeamin laatikko ja piirros, `og:image:alt`, `twitter:image:alt`
ja `max-image-preview:large`, kuvakelinkit headissa, `/favicon.ico` `image/vnd.microsoft.icon`, PNG-kuvakkeet
`image/png`, `/site.webmanifest` `application/manifest+json`, `/nonexistent-xyz.html` 404, sitemapin
`lastmod` 2026-11-12, JSON-LD jäsentyy 9 entiteetiksi (WebSite, Organization, viisi SoftwareApplicationia,
SF3D AI Lab WebSitena, Person).

**Havainto, ei muutos:** tuotantoverkkotunnuksen sivu eroaa repon tiedostosta vain Cloudflaren
sähköpostiosoitteiden suojauksen verran: vyöhyke korvaa kaksi `mailto`-linkkiä `/cdn-cgi/l/email-protection`
-osoitteella ja lisää purkuskriptin. Preview-osoitteessa (`pages.dev`) suojausta ei ole. Sama näkyy jo
arkistoidussa `docs/archive/concept-v3.html`:ssä, joten asetus on ollut päällä aiemminkin. Ilman
JavaScriptiä yhteystieto näkyy muodossa "[email protected]"; päätetäänkö asetuksesta, on Petrin asia
(BUILD_INFO.next).

**Iltapäivällä: `/silent-context/`-sivun tekstit päätetty** neljällä kierroksella (E–H, 15 kysymystä,
kohdat SC.1–SC.14 `copy-v4-pages.md`:ssä). Otsikko on "An agent that knows where its advice came
from." ja statusrivi "Built 6 to 8 Nov 2026 · third of fifteen". Osiot ovat ingressi, What Elisa
asked, What Silent context does, What I measured, and what I did not, sekä Why third, in my own
reading omin sanoin ilman joukkueiden nimiä. Video näytetään sellaisenaan, vaikka sen kohtauksessa 3
näkyy tulostaulu nimineen ja summineen; sivun teksti ei nimeä kumpaakaan. Todisteissa ovat koodi ja
hostattu demo. Jakokuvassa on aiheleima ja otsikko. Rakenteinen data: WebPage, SoftwareSourceCode
(myös etusivulle) ja VideoObject; adr.sws.019 täydennetty sallimaan alasivun oma video. SEED v4.0.0
luvut 2.2, 5.3 ja 8 päivitetty: `/silent-context/` rakennetaan ensimmäisenä alasivuna, kun sen
mediat ovat valmiit.

**Tarkistettu tekstejä varten 12.11.:** `pkorrrhonen-cmd/silent-context` (README, CHANGELOG,
hosting.md, tagit ja commitit), poistettu retrospektiivi repon historiasta (`da250e8`), Atlas
`SINCEAI-2026-HACKATHON-TAKEAWAY` v1, videotiedosto ffprobella ja kuvakoosteena, HTTP-pyynnöt
demoon (200 ja `/health` ok) ja tapahtuman sivulle (`sinceai.ai` 200). **Löydetty:** retrospektiivi
poistettiin reposta 8.11. illalla, joten 11.11. kirjattu todistepolku ja rivin A.4 viittaus olivat
vääriä; korjattu ja kirjattu LESSONSiin. Sivua ei muutettu. BUILD_INFO 5.2.1.

## Sessio 6 (11.11.2026): tilannetarkastus, sivuston omat tiedostot ja SEED v4.0.0 (ei sivumuutosta)

**Lähtökohta:** Petri palasi Since AI 2026 -tapahtumasta (Turku 6.-8.11.), jossa Silent context
oli kolmas viidestätoista Elisan haasteessa. Pyyntö: saada tulos näkyville, tarkistaa koko
projektin tila Atlasta vasten, ja laittaa SEO, GEO ja pienkuvake kuntoon.

**Tarkistettu tässä sessiossa** (ei muistista): Atlaksen statukset kaikista 25 järjestelmästä
11.11., `atlas_get_workspace sw-sivusto`, livesivun otsakkeet ja resurssit HTTP-pyynnöillä,
`node scripts/check-site.mjs --links` (kymmenen ulkoista linkkiä 200), sinceai2026-repo ja sen
video (1080x1920, 77,8 s, 15,7 MB), `github.com/pkorrrhonen-cmd/silent-context` julkinen,
sf3d.fi:n julkaistut huoneartikkelit ja `sf3d-ai-lab/media/publish/` renderöidyt videot.

**Löydetty, kolme merkittävää:**
1. **Jokainen tuntematon osoite vastasi 200:lla ja koko etusivulla** (94 886 tavua). `/favicon.ico`,
   `/apple-touch-icon.png` ja `/site.webmanifest` palauttivat HTML:ää. Soft 404 hakukoneelle, eikä
   sivustolla ollut kuvaketta missään selaimen välilehden ulkopuolella, koska ainoa favicon oli
   inline-SVG data-URI, jota ei voi hakea osoitteesta.
2. **adr.sws.015:n versiovahti ei ollut koskaan lauennut.** `check-site.mjs`:n regexistä olivat
   kadonneet kenoviivat jo sessiossa 4, eli kuvio ei voinut osua mihinkään. Seitsemän viikkoa
   mainissa. LESSONS 11.11.2026.
3. **Sivu oli seitsemän viikkoa jäljessä tuotetyöstä:** kaksi hackathontulosta, HomeTeam
   tuotannossa 10.10. alkaen, AvoQ ja SCC2 eivät näy sivulla, eikä uutisosiota ollut olemassa.

**Päätetty Petrin kanssa kolmessa laatikkokierroksessa** (`docs/design/review-2026-11.md`,
jokainen rivi tilalla): **sivusto lakkaa olemasta yksi sivu** (adr.sws.018). Etusivulle lyhyet
jutut ja uusi päivätty osio §04 Recent, esiteltävät asiat omille sivuilleen `/rooms/`,
`/reviewglass/`, `/silent-context/` ja `/hometeam/`, joista palataan painikkeella etusivulle.
Huonejärjestelmä kerrotaan tieteen nimillä (multi-agent debate, devil's advocate, dialectical
inquiry, LLM-as-a-judge, pre-registration, maximin), lähteenä Atlaksen
`ATLAS-HUONEET-KAR-ARV-20261031`; sanaa "Delphi" ei käytetä ilman lähdettä. Video kopioidaan
tänne ja pitkä evidenssi jää sf3d.fi:hin. Rakenteinen data nimeää tuotteet (adr.sws.019, muuttaa
18.9. päätöstä). HomeTeam saa oman laatikon §03:een. Tekniset korjaukset omaan PR:ään ensin.

**Tehty (PR A, index.html ei muutu):** `404.html`; `scripts/icons.py` ja sen tuotokset
(`favicon.ico` 16/32/48, `icon-192`, `icon-512`, `icon-maskable-512`, `apple-touch-icon`,
`site.webmanifest`) samasta aurinkomerkistä kuin inline-favicon; `_headers`-säännöt niille;
`sitemap.xml` lastmod 2026-09-20; versiovahti korjattu ja sille itsetesti samaan tiedostoon
(neljä osuvaa, neljä ei-osuvaa merkkijonoa); kaksi uutta CI-tarkistusta (sitemapin lastmod ja
kanoninen osoite, sivuston omien tiedostojen olemassaolo). `docs/SEED-v4.0.0.md` kirjoitettu,
`adr.sws.017`, `018` ja `019` kirjattu, ja `adr.sws.016` lisätty päätösindeksiin josta se puuttui.

**Tekstit (sama sessio, PR B:n osalta valmis):** ennen tekstejä luettiin hometeam-repo
(tuotannossa app.hometeam.fi 29.9. alkaen, mutta kirjautuminen vain sallituilla osoitteilla, joten
asteikon sana on In use eikä Live), todettiin SpectralForgen `BetaGatePage.tsx` yhä repossa
(closed beta pitää) ja verrattiin profiili-README sivuun: kuusi eroa, ei yhtään sivumuutosta,
listattu `copy-v4-pages.md`:n osaan F. Niistä yksi on vanha avoin asia, README nimeää työnantajan
ja kaksi sen sovellusta.

`docs/design/copy-v4-pages.md` kirjoitettu ja **PR B:n tekstit päätetty kolmessa laatikkokierroksessa
(23 kohtaa)**: §04 Recent -otsikko "What I have been building, with dates.", kaksi päivättyä
merkintää (Since AI 8.11., As Prescribed 18.10.), ei palkintorahaa eikä voittajien nimiä
etusivulle, HomeTeamin laatikko ReviewGlassin jälkeen tilalla "in use · my own family", ilman
linkkiä ja piirretyllä instrumentilla, navin kohta "Recent", og:image:alt otsikkona, ja kuusi
tuotetta joille tulee SoftwareApplication-merkintä (adr.sws.019 täydennetty).

**Ei tehty, seuraaviin sessioihin:** PR B etusivulle (tekstit valmiina), alasivujen tekstit omina
kierroksinaan, mediat (Since AI -videon uudelleenkoodaus 720x1280, huonevideon kopiointi, OG-kuva
per alasivu) ja yksi PR per alasivu. Järjestys on SEED v4.0.0 luvussa 8.

**Deploy:** PR #6 squash-mergattu 11.11.2026 19:43Z (`2aef4d2`) CI:n ollessa vihreä (Site checks ja
Cloudflare Pages). Ennen mergea preview `803057f6.sunrisesoftware-site.pages.dev` tarkistettu: 404-sivu
puhelin- ja työpöytäleveydellä, tuntematon osoite 404. Cloudflare Pages julkaisi noin 30 sekunnissa;
livestä todennettu: `/favicon.ico` 200 `image/vnd.microsoft.icon`, `/icon-192.png` ja
`/apple-touch-icon.png` 200 `image/png`, `/site.webmanifest` 200 `application/manifest+json`,
`/nonexistent-xyz.html` **404**, etusivu 200 ja `data-revised="2026-09-20"` ennallaan, sitemapin
`lastmod` 2026-09-20. Työ jatkuu 12.11.2026 PR B:stä.

## Sessio 5 (27.9.2026): SCC2:n asennuskuvakkeet /scc/-polkuun (ei sivumuutosta)

**Tehty:** SCC2-sovelluksen neljä asennuskuvaketta (192, 512, maskattava 512 ja 180 px
apple-touch-icon) kansioon `scc/` ja niille `_headers`-sääntö (välimuisti vuorokausi,
`Access-Control-Allow-Origin: *`). Syy: SCC2 on Cloudflare Accessin takana, ja Chrome hakee
asennuskuvakkeet ilman evästeitä, joten ne eivät voi olla sovelluksen omassa osoitteessa
(adr.sws.016, Petrin valinta 27.9.2026). Kuvakkeet tehdään scc2-repossa (`scripts/kuvakkeet.mjs`,
kuvake: kolikko ja numero 1 mustepohjalla, kaksoisviiva).

**Tarkistettu:** `index.html` ei muutu, joten alaviitteen päiväys ja `BUILD_INFO.updated` pysyvät;
`node scripts/check-site.mjs` vihreä.

## Sessio 4 (20.9.2026): tuoteversiot pois sivulta (adr.sws.015)

**Petrin havainto:** sivulla luki Luviamo v0.385, tuotannossa oli jo 0.388. Käsin kirjoitettu
versionumero vanhenee päivässä eikä mikään sivulla päivitä sitä, joten kaikki tuoteversiot
poistetaan. Pyyntö: etsi, listaa, poista yhtenä koontina.

**Löydetty ja listattu 8 kohtaa** (head, JSON-LD ja alt-tekstit puhtaat): heron metasolu
"Latest release · MasterForge 4.44 · 16 Sep 2026", tilarivit MasterForge v4.44, Luviamo v0.385,
Atlas v0.9, Virustutka v0.24, SpectralForge v2.0, ja Atlas-laudan piirretyt kortit "MasterForge ·
Starter v2" ja "Virustutka · v0.24". Yksi laatikkokierros (3 kysymystä): koonti hyväksytty,
metasolu vaihtuu "Email · pete@sunrisesoftware.app" (pysyvä fakta; Since 2024 olisi ollut kolmas
Est.-maininta), laudan kortit "MasterForge · free tier rebuilt" ja "Virustutka · autumn season".

**Tehty:** 8 korvausta index.html:ään, footer 20 Sep 2026. Tilarivit nyt "Live · paying customers
· 2024 →", "Live · 2026 →", "In use · 2026 →", "live", "closed beta"; päiväys jää, versio ei.
`check-site` kieltää `v1.2`-muotoiset merkkijonot ja "<tuote> 1.2" koko tiedostosta (kattaa myös
canvas-korttien datan); regex testattu positiivisilla ja negatiivisilla (CSS-luvut, "1335.90 pts",
`version="1.0"` eivät osu). Päätöstietue adr.sws.015 accepted, adr.sws.004 merkitty muutetuksi
("versio tai päiväys" → päiväys), sääntö SEEDiin (0, 4), CLAUDE.md:hen, copy-v3 (0.9, 2.4, 2.20,
2.27, 3.3, 3.36) ja apps-v3 (A.6 kortit). BUILD_INFO 5.0.2.

**Deploy:** PR #4 squash-mergattu, Cloudflare Pages deployasi; livestä todennettu data-revised 2026-09-20 ja ettei tarjoillussa HTML:ssä ole yhtään v1.2-muotoista tai "<tuote> 1.2" -merkkijonoa. Atlas sw-sivusto.STATUS v8 kirjoitettu OAuth-connectorilla.

## Sessio 3 (19.9.2026): palautekierros V5-livesivuun, 14 kohtaa päätöslaatikoilla

**Lähtökohta:** chat luki livesivun ja GitHub-profiilin tekstinä ja jätti Atlakseen palautteen
`SW-SIVUSTO-MSG-PALAUTE-V5` (art_cbd6dba3d59a4f8b): 5 vahvuutta, 14 korjauskohtaa kolmessa
luokassa (A ristiriidat sivun ja profiili-READMEn välillä, B tekniset, C tekstit) ja yksi
rakenteellinen huomio (jaetut faktat yhdestä lähteestä). Luettu OAuth-connectorin kautta.

**Tarkistettu ennen päätöksiä (ei muistista):** ReviewGlassin repo julkinen 18.9. 16:51Z,
Apache-2.0, BUILD_INFO sessio 4 pre-alpha; SpectralForgen live-appi näyttää käyttäjälle ilman
oikeutta "Closed Beta"-portin (`src/pages/BetaGatePage.tsx`), package.json 2.0.0; Luviamon video
5 118 732 tavua luviamo.appissa; Ultra Gravelin repo 0.1.0, livesivulla ei versionumeroa;
GitHub-profiili täytetty (nimi, bio, 2 julkista repoa, README bannerilla ja taulukolla); SF3D:n
vuodet: sivun 2006–2016 on korjattu arvo (LESSONS 17.9., check-site kieltää 2008), README sanoi
2008. Palautteen väitteistä yksi (A2) osoitti siis READMEen, ei sivuun.

**Päätetty Petrin kanssa kolmessa laatikkokierroksessa** (`docs/design/feedback-v5.md`, jokainen
rivi tilalla): ReviewGlass "Built for my own daily use. Open source, Apache-2.0." + repolinkki
laatikkoon; SpectralForge "closed beta · v2.0"; yksi tila-asteikko Live / In use / Closed beta /
Pre-alpha / Venture, versio heti tilan perään (Luviamo "Live · v0.385 · 2026 →", Atlas "In use ·
v0.9 · 2026 →"); MasterForge "paying customers · 2024 →" (Petri: vuosien pitää täsmätä yhtiöön,
2023 ei voi jäädä); kryokammion lukema "Lowest probe reading"; §01 kohta 03 sai toisen lauseen
"Patient data, audit trails and the security review are part of the product, not a layer added
afterwards."; Luviamon tagline nimeää työkaluluokat ("ideation, copy, visuals, scheduling,
publishing and measurement in one place"); 7 GHz -väite ankkuroitu ("And in 2026 no desktop
processor on sale…"); creed pysyy molempine lauseineen; Quaesitor pysyy poissa (päätetty 18.9.).
Tekniset: `#peek img` ja `#lightboxImg` saivat läpinäkyvän 1×1-paikkamerkin src:ksi; Luviamon
video kopioitu `media/luviamo-intro.mp4`; molemmat klipit `preload="none"`.

**Sivu muokattu yhdessä suunnittelun päätteeksi:** 14 korvausta `index.html`:ään, footer 19 Sep
2026, `check-site` vihreä (skripti kattaa nyt myös `media/`-viittaukset ja `poster`-attribuutit:
19 paikallista tiedostoa). Katsottu paikallisesti selaimessa: ReviewGlass-laatikko linkkeineen,
molemmat videot toistuvat näkyviin tullessaan `preload="none"`:lla, kryokammio puhelinleveydellä.

**Profiili-README** (`pkorrrhonen-cmd/pkorrrhonen-cmd`, eri repo, Petrin luvalla): SF3D 2006 to
2016 ja MasterForge paying customers since 2024, commit 8e190e8, pushattu. Työnantajan sovellusten
nimet READMEssä jäävät Petrin päätettäväksi (kohta 4).

**Rakenteellinen huomio kirjattu** `adr.sws.014`:ksi (proposed): sivun ja READMEn jakamat faktat
(tila, versio, alkuvuosi, lisenssi, url) yhdestä lähteestä, check-site vertaa sivua siihen ja
READMEn tuotetaulukko generoidaan siitä. Toteutus myöhemmin.

**Dokumentit:** copy-v3 rivit 1.9, 2.4, 2.20, 2.22, 2.27, 3.23, 3.24 (+3.24b linkki), 3.36, 4.8,
4.10; apps-v3 Luviamon lähde; SEED 3.4 (probe reading), 4 (tila-asteikko sääntöihin), 5.2
(video paikallinen), 7 (V5 live, palautekierros), 8 (next). `BUILD_INFO` 5.0.1, `updated`
19.9.2026, `sources_checked_2026_09_19`, `next` uusiksi (profiili-rivi sulkeutui).

**Deploy:** PR #2 squash-mergattu mainiin (9d85c02) Petrin pyynnöstä, Cloudflare Pages deployasi noin puolessa minuutissa; livestä todennettu data-revised 2026-09-19, muuttuneet tekstit ja molemmat klipit (206 range-pyyntöön). Petri: MasterForge 2024 on ok. Bearer-poisto A ajetaan päivän päätteeksi.

**Mobiilikorjaus (Petri puhelimelta: MasterForgen EQ oli vanha piirros kultaisilla palkeilla):** video oli `opacity:0` kunnes `canplay`, ja puhelin joka ei käynnistä `play()`-kutsua ilman elettä ei koskaan antanut sitä, joten alla oleva canvas-luonnos jäi näkyviin. Nyt video posterinsa (oikea EQ-ruutu) kanssa näkyy heti, `ready` tulee `playing`-tapahtumasta, ja toisto yritetään uudelleen ensimmäisellä kosketuksella, osoittimella tai vierityksellä sekä välilehden palatessa. Todennettu paneelin mobiiliemulaatiossa: posteri näkyy ilman toistoa, vieritys käynnistää klipin. PR #3.

**Atlas-yhteyden 401 selvitetty** (Petrin pyyntö): projektitason `.mcp.json` (24 repoa, pvm
9.8.2026) määrittelee `atlas`-palvelimen staattisella bearerilla `${ATLAS_MCP_TOKEN}`; muuttuja on
Windowsin käyttäjätason ympäristömuuttuja, jonka arvo ei enää vastaa MCP-workerin `MCP_TOKEN`-
secretiä; `~/.claude/settings.json` kytkee sen päälle (`enabledMcpjsonServers`). OAuth-connector
on toiminut koko ajan. Ehdotettu poisto (kaikki kolme paikkaa), ei ajettu ilman Petrin sanaa.

## Sessio 2 (18.9.2026 aamu): Petrin vastaukset Flow 1:een, Flow 2 rakennettu

**Petrin vastaukset:** sivu on pitkä ja harva, tiivistetään hieman; kuvan yläreuna häivytetään
paremmin; hover-esikatselu hyvä mutta kaksinkertaisena, eikä se saa seurata kursoria plus-painikkeen
lähellä; plus reagoi lähestymiseen kasvamalla; toiminnot houkuttelevia ja responsiivisia. Liike
riittää mutta animoidummin: sumuverho väistyy ja aurinko nousee valaisemaan kohtaa jota katsotaan;
navin aurinko "nerokas", pidetään. Meri hieman vaaleampi: seisot rannalla aamuauringossa.
Ylikellotus otsikkotasolla selvänä, kuvat ja lisätieto painikkeen takana kryokammiona, joka tuo
kylmän kontrastin lämpimään sivuun; otsikko kertoo heti että nesteheliumilla on kellottanut vain
kourallinen ihmisiä. Tuotteet interaktiivisemmiksi ja eläviksi: Luviamon esittelyvideo, MasterForgen
palkit liikkuvat, Virustutkan kartta värjäytyy, Ultra Gravelin reitti piirtyy, Somnuksessa kaavat
leijuvat. "Yksi vilkaisu ja ymmärrys syntyy lukematta mitään."

**Tehty:** `docs/mockups/flow-2.html` toteuttaa jokaisen kohdan (taulukko briefissä, luku "Round 3").
Uutta: lukuvalo (sky-kerroksen lämmin ellipsi hakeutuu luettavan osion otsikkoon), pysäköity
esikatselu (540 px, rivin oikeassa reunassa plussan vieressä), kasvava plus (0.62 → 1.4 lähestyessä),
rantagradientti ja auringon polku vedessä, kryokammio (kylmä paneeli, sumu-canvas, lukemat, nauha),
elävät tuotelaatat canvas-piirroksina (11 kpl) ja Luviamon oikea esittelyvideo (poster kopioitu
Luviamo-reposta, video striimataan luviamo.appista). Atlas-kaavion kontrasti korjattu. Mitattu
paneelissa: esikatselu asettuu rivin kohdalle, plus skaalautuu 1.36:een kursorin lähellä. Kaksi
korjattua vikaa: esikatselun sijainti laskettiin väärästä juuresta, ja `all:unset`-nappi katkaisi
CSS-muuttujan periytymisen (skaala nyt inline-transformina).

**Petrin luenta Flow 2:sta (aamupäivä):** miltei kaikki kohdallaan. Kolme korjausta: heroon enemmän
vaaleaa, punertava hehku peitti muotokuvan; kryokammion Close-nappi oli tekstin päällä; footerissa
kimallusviivat osuivat otsikoihin ja linkkeihin. Tekstisisältö ja piirretyt kuvat jätetään nyt
huomiotta, vain toiminnallisuus katsotaan; iso tekstiremontti tulee fonttivaiheen jälkeen.

**Korjattu ja mitattu paneelista:** orbit siirretty muotokuvan vasemmalle puolelle ja vaimennettu,
aamugradientti vaaleammaksi, lukuvalo pois herosta kokonaan, kursorivalo sammuu muotokuvan
sarakkeessa, muotokuvan yläreuna yhtyy paperiin; Close omalle riville kammion yläreunaan (ei
enää päällekkäin labelin tai otsikon kanssa); kimallukset vain vedessä tekstin yläpuolella
(100 px väli mitattuna), linkkien riviväli väljemmäksi.

**Muotokuva (Petri: "ihminen näkyy kokonaan"):** häivytysmaski ja multiply-sekoitus peittivät kasvot
ja katkaisivat pään. Ratkaisu: hahmo irrotettu studiotaustasta (`docs/mockups/media/petri-cutout.webp`,
175 kB; väriedellisyys + suurin yhtenäinen alue + pehmennetty reuna + alareunan häivytys, ei
erillistä mallia, skripti CHANGELOGin rivillä toistettavissa numpy/scipy/Pillow'lla). Herossa ei
enää maskia, peittoa eikä sekoitusta; takana pehmeä lämmin hehku, vartalo häipyy paperiin alhaalla,
parallax kevennetty ettei pää poistu kehyksestä.

**Hero kuitattu, fonttikierros aloitettu:** `docs/mockups/type-1.html` näyttää kuusi kirjasinparia
Flow 2:n heron ja yhden osion päällä samassa valossa; ylälaidan nauha vaihtaa parin ja labelien
tyylin (mono tai leipäfontti). Parit ja perustelut briefissä ("Type round"): 1 Newsreader + Albert
Sans (rauhallinen editoriaalinen serif), 2 Instrument Serif + Sans (kapea, persoonallinen),
3 Bricolage Grotesque + Figtree (groteski jolla on luonne), 4 Familjen Grotesk + Public Sans
(pohjoismainen, hiljainen), 5 Gloock + Golos (yksi rohkea ele otsikoissa), 6 Young Serif + Onest
(lämmin, käsintehdyn oloinen). Kaikki Google Fontsista, saatavuus tarkistettu. Kuvat pareittain ja
kaksi vertailuarkkia (herot, osiot).

**Fontti päätetty (adr.sws.012):** Petri valitsi parin 4, Familjen Grotesk + Public Sans: "ainoa
varteenotettava vaihtoehto, helppo lukea ja neutraali, sopii tähän hyvin". Viety Flow 2:een koko
sivun läpi: Familjen Grotesk 400 otsikoissa, tuotenimissä, säännöissä, §01:n lauseissa, ideologia-
lauseessa ja sähköpostissa; Public Sans 300–600 leivässä ja UI:ssa; JetBrains Mono labeleissa
toistaiseksi (mono vai sans päätetään erikseen, kytkin type-1.html:ssä). Kursiivia ei käytetä,
korostus värillä. Kaappaukset päivitetty.

**Tekstikeräys (Petrin pyyntö):** kaikki Flow 2:n tekstit kerätty yhdeksi numeroiduksi rakenteeksi
`docs/design/copy-v3.md`: 7 osaa (kehys, §01, §02, §03, SF3D ja kryokammio, §04, §05 ja footer,
sivun mukana kulkevat metat), jokainen tekstinpätkä omalla numerollaan ja tilalla (draft / OK / edit /
drop / later). Sovellusosiot merkitty `[apps]`, koska niiden joukko ja kuvaukset käydään erikseen
sovellusnäkymäremontissa; kal.app ja HomeTeam merkitty `drop` Petrin ohjeen mukaan (ei käytössä),
VitalTrack, sisäiset työkalut ja SpectralForge `later`. Otsikolle ja ideologialauseelle kolme
vaihtoehtoa. Muokkaus numero kerrallaan; kun kaikki on OK, tekstit ovat valmiit.

**Tekstilista käyty läpi kysymyslaatikoilla, 4 kohtaa kerrallaan (Petrin toive), 18.9. iltapäivä.**
Kaikki 7 osaa päätetty; 0 draft-riviä jäljellä, 7 `later`-riviä kuuluvat sovelluskierrokseen
(laattojen kuvatekstit, Atlas-kaavion labelit, Open-pilleri, alt-tekstit, rakenteinen data).
Keskeiset päätökset: otsikko "Understand the human first. Then build the better product for
them." (suunta: ohjelmistoja ihmisille, 20 vuotta ihmisten kanssa, ei koodausta kellarissa); lede
"The world is open. Wherever better software is needed, from audio to public health, I build it.";
Founder metarivillä; navi Products · Approach · Contact; §01 intro ilman "stably"-sanaa (ärsyttävä
suomalaiselle), ala 01 viestinnän ymmärryksellä, ala 04 ilman agentteja. **Rakennepäätös §02:** kaksi
ryhmää, Commercial products (MasterForge, Luviamo) ja Tools and research instruments (Somnus, Atlas);
**Quaesitor putoaa pois** (ei enää kehitetä, Somnus on tutkimusydin); Somnukseen AMD-maininta
tarkasti "AMD R9700 sample program · white paper in progress"; Atlas kuvataan projektinhallintana,
yhteistyönä, kirjastona ja lisämuistina, työn tukirakenteena. Spec-rivit ilman tekniikkanimiä
kaikissa tuotteissa. **§03 joukko:** Virustutka, Ultra Gravel, TilastoSilta, SF3D AI Lab, ReviewGlass,
Salpa Defence, SpectralForge (tuotanto, ei beta); pois Kalastus, HomeTeam, Quaesitor Security,
VitalTrack, sisäiset työkalut. SF3D: otsikko väitteenä, Petrin oma johdanto, nappi ilman
lämpötilaa. §04: "How the work gets done.", säännöt kokonaan uusiksi (ihminen ensin, järjestelmästä
paras irti, sameness is not a business model), ideologialause pidetään, menetelmäkohdat pidetään.
§05: "Let's talk." ja Petrin ydinajatus avoimuudesta. Footer ilman "Independent". Labelit mono.

**Välitarkistus (Petrin pyyntö): Flow 3** = Flow 2 päätetyillä teksteillä ja rakenteella
(`docs/mockups/flow-3.html`, kuvat työpöytä ja puhelin). 50 tekstivaihtoa, Quaesitor-laatta ja
viisi laatikkoa poistettu, Somnus-laatta ja SpectralForge-rivi lisätty, ryhmäotsikot §02:een.
Tarkistettu: yhtään pudotettua nimeä tai kiellettyä sanaa ei jäänyt runkoon. Laatat ja kuvat ovat
yhä paikanpitäjiä sovelluskierrokseen.

**Petrin luenta Flow 3:sta (ilta):** hyvällä mallilla; kaksi otsikkoa olivat jääneet minun
sanoikseni ilman yhteistä päätöstä (§02 "control plane" vanhasta Atlas-kuvauksesta, §03 "Smaller").
Käyty läpi: §02 "Products people pay for, and the instruments behind them.", §03 "More products,
tools and instruments." (instruments kattaa SpectralForgen kutsuttavana palveluna, Salpan ja labin).
Kryokammion teksti kirjoitettiin kokonaan uusiksi Petrin suunnasta: rajojen rikkominen, ennätykset
ja kilpailu, teknologian kehitys jonka teollisuus rakensi meidän takiamme (virransyötöt, markkinan
tuotteet), valmistajien edustaminen tapahtumissa, ja 7 GHz jota yksikään vakiona myytävä
pöytäkoneprosessori ei vieläkään saavuta. Helium −269 °C tekstissä, mitattu lukema −234 °C
lukemissa. Flow 3 päivitetty ja kuvat uusittu.

**Sovellusnäkymäremontti (ilta, kysymyslaatikoilla):** lista `docs/design/apps-v3.md`, kaikki kohdat
päätetty. §02-laatat: MasterForge = oikea Pro Master -EQ-tallenne loopilla (mainosvideotyön klippi,
12,5 s, 3,4 MB, kopioitu `docs/mockups/media/`); Luviamo = esittelyvideo, klikkaus toistaa äänellä;
Somnus = räkkipaneeli (kolmesta luonnoksesta `somnus-plate.html` valittu 3: GPU-mittarit ja elävä
työlista kuudella tehtävällä: audio separation, research funnel, Atlas compute, Salpa processor,
local inference, research engine "what Quaesitor did, now local"), Petrin linjaus: Somnus on
työjuhta ja suppilo vain yksi tehtävä; Atlas = työtilalauta (Projects, Waiting on, Decided,
kumppani, puhelin, kirjasto). Pilleri "Visit ↗". **Laatikoissa vain oikeaa tuotetta:** Virustutka
ja SpectralForge kaappaus molemmissa, Ultra Gravel reittikaappaus (Petri otti 18.9.: 67 km silmukka Tampereen ympäri, 816 m nousua, 79 % soraa; rajattu 16:9 laatikkoon ja esikatseluun), TilastoSilta ja
SF3D AI Lab kaappaukset, Salpa brändikäsikirjan logo (kopioitu `media/`) ja hoverilla "ACCESS
DENIED", ReviewGlass mockup tekstiruudusta (lasi ja lukukehikko sumennettujen palstojen päällä).
Kryonauha kahdeksan kuvaa, LN₂ ja Taiwan ensin. Rakenteinen data vain Organization ja Person.
OG-kuva: otsikko auringonnousupaperilla. Flow 4 katsotaan koko sivuna kerralla.

**Opit:** näytön ulkopuolinen canvas ei saa kokoa `getBoundingClientRect`istä taustavälilehdellä
ja rAF ei etene; korjattu piirtämällä ensimmäinen kehys heti ja ajastinvarmistuksella (somnus-plate,
flow-2, flow-3). Ultra Gravelin kartta-UI ei ohjaudu ulkoa (ei globaalia karttakahvaa, ei
reitti-URLia), joten aito reittikuva otetaan käsin.

**Flow 4 rakennettu** (`docs/mockups/flow-4.html`, 17 vaihtoa Flow 3:een): MasterForgen EQ-tallenne
loopilla (varaluonnos alla, häivytys kun klippi on valmis, toisto vain näkyvissä; kuvasuhde 3,9:1
rajautuu 16:10-kehyksessä keskikaistaan, joka näyttää käyrän ja spektrin), Luviamon video klikkaus
äänelle, Somnus-räkkipaneeli, Atlas-työtilalauta (kolme saraketta korteilla, kumppanin puhelin,
kirjastohylly), Visit-pillerit; laatikot: Virustutkan kartta, Petrin Ultra Gravel -reitti,
TilastoSilta ja sf3d.fi kaappaukset, ReviewGlass-mockup (sumennetut palstat, lukukehikko, lasi),
Salpan logo kuusenvihreällä ja ACCESS DENIED -leima hoverilla, SpectralForgen kuvakaappaus;
kryonauha uudessa järjestyksessä. Tarkistettu paneelista: klippi toistuu (1720×444), kaikki
canvasit piirtyvät, yksi muuttujavirhe (ReviewGlass) korjattu. Kuvat työpöytä ja puhelin.

**Flow 4 hyväksytty (Petri: "huima parannus edelliseen versioon, olemme valmiita"; huomio: EQ-säädön
kapea kaista klipissä on sivuseikka, laajempi tallenne voi korvata sen myöhemmin).** adr.sws.013.
**SEED v3.0.0 kirjoitettu** Flow 4:stä: pääversio (suunnan vaihto), sivuarkkitehtuuri V5, paletti A'
tokeneineen, typografia, sky ja valo (liikejärjestelmä), komponentit (hero, laatta, ryhmälabel,
laatikko, kryokammio, approach, ranta, lightbox, nauhat), elävät laatat ja piirretyt instrumentit,
sisältöindeksi copy-v3.md:hen, assetit sivulle, head ja SEO, suorituskyky, saavutettavuus, CI,
iteraatioloki ja seuraavat askeleet. SEED v2.0.0 ja v2.1.0-luonnos arkistoitu. CLAUDE.md ja README
päivitetty viittaamaan v3.0.0:aan; CLAUDE.md:n sivusäännöt päivitetty (SF3D kryokammiona, laatat
oikeaa tuotetta, spec-rivit ilman tekniikkanimiä, kysymyslaatikkomenetelmä).

**Sivu rakennettu (Petri: "tehdään vielä tuo").** `index.html` kirjoitettu Flow 4:stä (47 vaihtoa):
sivun assetit (muotokuva 880 ja 440 px WebP + PNG, laatikkokaappaukset WebP + JPG, EQ-klippi
`media/masterforge-eq.mp4` ja poster, Luviamon poster, Salpa-SVG, OG-kuva 1200×630 Bahnschrift-
sijaisfontilla, inline-SVG-favicon nousevalla auringolla); head (description, canonical,
theme-color, Open Graph, Twitter card, JSON-LD Organization + Person); oikeat linkit kaikkialle
(GitHub neljästi, tuotteet, sf3d.fi, mailto); alt-tekstit joka kuvalle; skip-linkki ja
focus-visible; `data-revised="2026-09-18"` footerissa. Korvatut kuvat poistettu (product-quaesitor,
-masterforge, -luviamo), studiomuotokuvan lähde siirretty `source-assets/`. **check-site vihreä.**
Paneelista: ei konsolivirheitä, 16/16 kuvaa latautuu, molemmat videot valmiina. Paino 5,2 MB, josta
3,4 MB on klippi joka latautuu vasta näkyvissä; HTML 91 kB. Kaappaukset `docs/mockups/v5-*.png`.
BUILD_INFO 5.0.0.

**Commit, PR ja deploy (Petri: "commit ja deploy / merge liveen").** Haara pushattu, PR #1 avattu.
Mainiin oli tullut 17.9. commit (perustajatiedot karsittu julkisiin faktoihin, lisenssi, repo
julkiseksi), joten sama linja tähän: koko repo skannattu ja työnantajan sovellusten nimet,
kumppanien etunimet ja muiden projektien sisäiset tilat poistettu kaikista jäljitetyistä
tiedostoista (yksi oli Atlas-laudan korttitekstissä script-lohkossa, jota CI ei tarkistanut;
kieltolista tarkistaa nyt koko tiedoston), arkistoidut SEEDit ja concept-v3 karsittu, README:n
lisenssikappale. Rebase mainin päälle (README-konflikti ratkaistu haaran versioon). CI vihreä,
Cloudflare Pages -esikatselu katsottu paneelista (ei virheitä, kuvat ja videot latautuvat,
puhelinleveys kunnossa). Squash-merge mainiin 18.9. 16:34 UTC. **V5 livenä** noin 40 s myöhemmin:
todennettu title, og:image, data-revised, assetit (muotokuva, klippi, OG, robots, sitemap) ja
turvaotsakkeet.

**Ketjun paketointi (Petri: "paketoidaan tämä ketju ja tehdään lopetusdokumentaatio").** Petri
huomasi, että päätösten pilkkominen neljän laatikon eriin tehosti päätöksentekoa: sivukysymykset
vähenivät ja päätös muotoutui vaihtoehtoja vertaillessa, ja pyysi tutkimaan ilmiötä ja kirjaamaan
työtavan Atlakseen muiden repojen käyttöön. Tutkittu (verkko): Hickin laki, valintaylikuorma
(Iyengar ja Lepper 2000), työmuistin nelosraja (Cowan 2001), päätösväsymys (Danziger 2011 ja sen
kritiikki), oletusvaihtoehdon vaikutus (Johnson ja Goldstein 2003), Raiffan hajota ja kokoa,
Delphi, yksi kysymys kerrallaan -lomakkeet. Menetelmällä ei ole yhtä vakiintunutta nimeä; perheen
nimeksi **päätöslaatikot**. Kirjoitettu `docs/design/decision-method.md` (mitä tehtiin, viisi
ilmiötä, nimi, ainoa virhe ja sen sääntö, seitsemän kohdan ohje muihin repoihin, lähteet) ja
`docs/SESSION-CLOSE-2026-09-18.md` (ketjun tulos, kierrokset, päätökset, opit, avoimet). Atlakseen
viety artefakti `SUNRISE-TYOTAPA-PAATOSLAATIKOT` (art_8b3182d865124b2e, v1, draft, system
sw-sivusto) OAuth-connectorin kautta; projektitason MCP-merkintä hylkää tokenin edelleen (401).
CLAUDE.md:n päätöslaatikkosääntö viittaa nyt menetelmädokumenttiin.

**Seuraava:** Petrin luenta livesivusta puhelimella ja työpöydällä; korjaukset uuteen haaraan
mainista. Atlas-ehdotukset, GitHub-profiili, Web Analytics, Lighthouse.
Aiemmin kirjattu seuraava askel oli: sovellusnäkymäremontti (elävät laatat, laatikkokuvat, Atlas-kaavio uuden kuvauksen mukaan,
joukon lopputarkistus), sitten SEED v3.0.0.

## Sessio 1, päätös (17.9.2026 myöhään illalla): Flow 1 on oikea suunta

**Petri:** "Erittäin hyvä. Hiotaan tätä huomenna ja vastaan kysymyksiin tarkemmin. Tämä mockup on
juuri oikea suunta." Kirjattu adr.sws.011:ksi. Kierros 2:n mockup `docs/mockups/flow-1.html` on
tästä eteenpäin sivun referenssi; sitä hiotaan yhdessä 18.9. alkaen, sitten fonttikierros, sitten
tekstit ja sisältö, sitten SEED v3.0.0 ja vasta sitten sivu.

**Session lopputila:** sivu, gitin kuvat ja sivun asset-tiedostot koskemattomia. Työpuussa
committoimatta: dokumentaatio, päätökset 001-011, CI-tarkistus, SEED v2.1.0 -luonnos, brief,
mockupit ja kuvat (`docs/mockups/`, mukaan lukien `shots/` live-sivuista) sekä työpuun kopio
muotokuvasta (`images/Petri.jpg`, ei stagettu) ja `.claude/launch.json` (paikallinen palvelin
paneelia varten, ei stagettu). Commit tehdään kun Petri sanoo. Atlas `sw-sivusto.STATUS` v3
kirjoitettu.

**Kuvakaappausten opit** (tallennettu myös `docs/mockups/README.md`): headless Edge palaa ennen
kuin kuva on kirjoitettu, joten skripti odottaa tiedoston valmistumista ennen profiilin poistoa;
paneeli lataa `file://`-sivun data-URL:na ilman kuvia, joten mockupit katsotaan paikallisen
palvelimen kautta (`python -m http.server 8765`); staattinen kaappaus on yksi korkea viewport,
joten `?static=1` poistaa vh-mitoitukset.

## Sessio 1, jatko 2 (17.9.2026 ilta): look-kierros 1 päätetty, kierros 2 (elementit, liike, flow)

**Petrin vastaukset** (adr.sws.010): A hieman C:hen; fontti vaihtuu (Fraunces on koukeroinen serif,
joka on nyt jokaisessa LLM-sivustossa; katsotaan erikseen), mono-labelit samassa; footer saumaton
siirtymä; muotokuva herossa reunat häivytettyinä; liikkuva hehku; ylipäänsä enemmän animaatiota,
hiirellä esiin vedettävät galleriat, parallax. Järjestys: väri, sitten elementit, liike ja flow,
sitten fontit ja tekstit, sisältö ohessa. Sivun pitää välittää: mielikuvitus on raja, rakenna ja
nauti maailmasta.

**Tehty:** paletti A′ ja kierros 2:n konsepti briefiin (sivu on yksi aamu: ensisäde ylhäällä,
selkeä aamupaperi keskellä, avomeri alhaalla). Kuvakaappaukset live-tuotteista laatikoita varten
(`docs/mockups/shots/`, `docs/mockups/shoot.py`). Kierros 2:n mockup `docs/mockups/flow-1.html`:
sky-kerros valon etenemisellä, liikkuva hehku ja kursoria seuraava lämpö, häivytetty muotokuva,
navin aurinko nousee vierityksen mukana, sanoittain nousevat otsikot, tuotelaatat parallaxilla,
elävä Atlas-kaavio, kabinetin laatikot (hover vetää, klikkaus avaa, raahattava nauha), SF3D
filminauhana (sijoitus auki), lähestymistavan säännöt ja ideologialause, sivu liukuu mereen.
Fontti tarkoituksella neutraali paikanpitäjä (DM Sans). `?static=1` kuvia varten.

## Sessio 1, jatko (17.9.2026 ilta): uusi ilmesuunta, look-kierros 1

**Petrin linjaus:** tumma teema on 2026 AI-sivustojen perusasia; Luviamon brändäys on perheen
paras eikä lue kielimallin tekemältä; sivusto suunnitellaan Sunrise-ajatuksella: lämmin paletti,
auringonnousu meren takaa (ensimmäiset säteet silmiin, lämpö kasvoille), Luviamon koivumetsän
tapaan tunnelmana, ei kuvina. Suunnan vaihto on SEED-pääversio (v3), ja se päätetään mockupeista.

**Tehty:** Luviamon ilme luettu lähteistä (SEED §10 ja §11, site-tokenit, app/theme.css, live-sivu):
vaalea pohja, Fraunces ilman kursiivia, DM Sans, yksi kultainen aksentti, valo-orbit ja loivat
gradientit, tumma vihreä vain navissa ja footerissa. Brief `docs/design/look-2026-09.md`: siirto
auringonnousuun (paperi, horisonttigradientti, aurinko-aksentti, meri-harmaansininen toissijaisena,
Fraunces + DM Sans + mono vain arkistolabeleissa) ja kuusi kysymystä. Look-kierros 1:
`docs/mockups/build-look.py` tuottaa kolme varianttia samasta näkymästä (A Ensisäde, B Lämpö
kasvoilla, C Aamu-usva meren yllä) ja kuvat työpöytä 1440 px ja puhelin 390 px headless Edgellä.
Muotokuva (`images/Petri.jpg`, kopio työpuussa, ei gitissä) herossa multiply-sekoituksella. Kuvat
lähetetty Petrille. Oppi: Edge headless tarvitsee oman `--user-data-dir`in, muuten käynnissä oleva
selain ottaa kutsun eikä kuvaa synny.

**Ei tehty:** sivua, SEED v3:a tai päätöksiä. Seuraava: Petrin luenta kuvista ja vastaukset
briefin kysymyksiin, sitten kierros 2 (yksi variantti koko sivun läpi).

## Sessio 1 (17.9.2026): dokumentaatio talon standardiin, sivun uudistus suunnitelmaksi

**Lähtötilanne.** Sivu on V4.5 (18.4.2026) eikä sitä ole muutettu sen jälkeen. Repo sisälsi
READMEn, SEED v2.0.0:n ja arkistokansion; ei CHANGELOGia, BUILD_INFOa, LESSONSia, päätöstietueita,
CLAUDE.md:tä eikä CI:tä. Atlaksen malli `sw-sivusto` kantoi kaksi ADR:ää joita repo ei.

**Petrin linjaukset sessiossa:** (1) dokumentaatio Atlaksen ja Luviamon tasolle; (2) kellotushistoria
vielä enemmän piiloon pieneksi sivuhuomioksi; (3) sivu peilataan nykytilaan, Atlas näkyviin
yhteistyön työkaluna (työtila ja Atlas Connect); (4) työnantajan sovelluksia ei näytetä ennen
erillistä lupaa; (5) ulkoasu tarkastellaan hackathon-vierailijan silmin (Since AI); (6) linkki
julkiseen GitHub-profiiliin samaan pakettiin; (7) **sivun muokkaukset vain yhdessä sovitusti ja
suunnittelun päätteeksi.**

**Tehty (dokumentaatio ja työkalut):**
- `CLAUDE.md`: työtavat, dokumenttien paikat, sivun säännöt (voimassa kun päätös hyväksytty),
  sessiorutiini, Atlas-peilaus, sääntö sivun yhteismuokkauksesta.
- `docs/decisions/`: adr.sws.001 ja 002 tuotu Atlaksesta repoon; 003 (historia sivuhuomioksi,
  ehdotettu muoto), 004 (päivätyt tilat, ehdotus), 005 (Atlas §02.4 ja piirretty kansi, ehdotus),
  006 (työnantajan sovellukset pidätetty, hyväksytty), 007 (GitHub-linkki, hyväksytty; osoite vahvistetaan),
  008 (React-siirtymä pois roadmapilta, ehdotus), 009 (dokumentaatiostandardi, hyväksytty).
- `docs/LESSONS.md`: kolme oppia (suhteellinen aikailmaus, jonossa ollut korjaus ilman paikkaa,
  Atlas tiesi enemmän kuin repo).
- `docs/BUILD_INFO.json`: tila, 17.9. tarkistetut lähteet tuotteittain, `next`-lista.
- `scripts/check-site.mjs` ja `.github/workflows/ci.yml`: riippuvuudeton tarkistus (kuvaviittaukset,
  head-metat, ei ajatusviivoja, kielletyt merkkijonot, footerin revisiopäivä = BUILD_INFO.updated,
  GitHub-linkin esiintymät). **Punainen V4.5:llä tarkoituksella**: portti kantaa uudistuksen säännöt.
- `docs/SEED-v2.1.0.md` (LUONNOS): tarkistettu nykytila, ulkoasukatselmus, ehdotettu sivuarkkitehtuuri
  V4.6, koko ehdotettu copy osioittain, tekniset lisäykset ja luku 7: Petrin päätettävät asiat.
- `README.md` uusittu talon muotoon (Status, Layout, Develop, Deploy, Documents).

**Tarkistettu 17.9.2026** (lähde ja päivä `BUILD_INFO.sources_checked_2026_09_17`): MasterForge
4.44.0 (16.9.), Quaesitor 2.13.27, Luviamo 0.385.0 tuotannossa (16.9.), SpectralForge 2.0.0,
Atlas 0.9.185 (sessio 135, 12.9.), Virustutka live, Ultra Gravel live, TilastoSilta live, sf3d.fi
live, ReviewGlass pre-alpha (17.9.), Salpa-demo tuotannossa (22.8.), Somnus (17.9.), Kalastus
(1.9.), Quaesitor Security sisäinen (20.8.). HEIJASTE ja BrightFeed: ei jälkeä missään repossa.
GitHub `pkorrrhonen-cmd`: 0 julkista repoa.

**Korjaus samana iltana (Petrin palaute):** ketju lähti liian lujaa: sessio alkoi kirjoittaa sivua ja
ehdotti SF3D-kuvien poistoa ennen kuin pelisäännöistä oli sovittu. Linjaukset: (a) sivua ei muokata
ennen kuin muutoksista on katsottu yhdessä mockup-kuvat; (b) SF3D:tä ei poisteta, sen rooli ja
näkyvyys suunnitellaan uudelleen (adr.sws.003 avoin, vaihtoehdot A/B/C SEED 4.4); (c) kysymyslista
(SEED luku 7) käsitellään vasta alkuselvitysten jälkeen; (d) `images/Petri.jpg` (16.8.2026) on tuotu
pääkansioon sivulla käytettäväksi, sijoitus mockupeista. Atlas-yhteys: session alussa raportoitu 401 koski projektitason
MCP-määritystä ("atlas", staattinen bearer-otsake, jonka palvelin hylkää; OAuth-varapolku ei
käynnisty kun otsake on asetettu). Claude.ai:n OAuth-connector "Atlas" oli koko ajan yhdistetty (30
työkalua); sessio luki virheilmoituksen väärin. Atlas luetaan connectorin kautta.

**Atlas luettu 17.9. illalla (connector):** kokonaiskuva v3 (6.9.2026), kaikkien 20 järjestelmän
statukset ja sivuston työtila. Erot paikallisiin tarkistuksiin `BUILD_INFO.atlas_read_2026_09_17`:
Quaesitor tuotannossa 2.13.34 (checkout jäljessä), Virustutka v0.24.0 ja liikennevalo määritelty
uudelleen, TilastoSilta v2 odottaa cutoveria, Luviamon laskutus livenä 15.8. alkaen, MasterForgen
Atlas-status on repoa jäljessä, Somnus-boksi alhaalla komponenttivaihtoa varten. Sivuston oma
status oli v1 26.7.2026 ja kantoi odottavan raiteen: **sivustogeneraatio Atlaksen STATUS-datasta**
(SEED 5.5 vaihtoehtona käsin ylläpidetyille päivätyille tiloille). Työtilassa ei ollut opasta,
aikajanaa, päätöksiä eikä viestejä. Kokonaiskuva nimeää Since AI:n jo Atlaksen puolella.
`sw-sivusto.STATUS` v2 kirjoitettu 17.9. illalla; ADR-ehdotukset Atlakseen yhtenä kierroksena kun
suunnitelma on sovittu.

**Ei tehty, tarkoituksella:** `index.html`, `images/`, OG-kuva, `_headers`, `robots.txt`,
`sitemap.xml`. Ne kuuluvat sivun pakettiin, joka muokataan yhdessä suunnittelun päätteeksi.
`sw-sivusto.STATUS` peilataan connectorin kautta alkuselvitysten päätteeksi (`next`).

## Historia ennen sessiota 1 (SEED v2.0.0:n iteraatiolokista)

- V1 (2024 Q4): SaaS-tyylinen yhden sivun landing, neljä tuotekorttia. Julkaistu, vanhentui.
- SEED v1.0 (25.3.2025): uudistuksen suunnittelu alkoi.
- V2, V3, V3 revised (16.4.2026): editoriaalinen sävy, eri fontit; hylätty tai korvattu.
- V4 (17.4.2026): Observatory × Atelier, Fraunces + Inter, cabinet dark, §-osiot. Suunta vahvistettu.
- V4.1 - V4.4 (17.4.2026): neljä alaa, SF3D-kuvat, proof rail, lightbox.
- **V4.5 (18.4.2026): tuotekannet, SpectralForge featured. LUKITTU.** Initial commit bc3e463.
- Kesäkuu 2026: tuotanto Cloudflare Pagesin Git-integraatioon, domain siirretty (todennettu 13.6.2026).
