# CHANGELOG (Sunrise Software site)

Sessiokohtainen muutosloki, uusin ensin. Tila on `BUILD_INFO.json`:ssa, avoimet asiat sen
`next`-listassa, päätökset `decisions/`-kansiossa. Tämä tiedosto kertoo mitä tehtiin ja miksi.

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
