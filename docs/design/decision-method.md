# Päätösten pilkkominen laatikoiksi: työtapalöydös 17.–18.9.2026

**Tekijä:** Petri Korhonen, kirjannut Claude Code · **Lähde:** Sunrise Software -sivuston uudistus,
sessiot 1 ja 2 (`docs/CHANGELOG.md`) · **Atlas-artefakti:** `SUNRISE-TYOTAPA-PAATOSLAATIKOT`

## 1. Mitä tehtiin

Kahdessa päivässä sivusto suunniteltiin ja rakennettiin uusiksi: ilme, liike, fontti, noin 90
tekstikohtaa ja noin 30 kuvakohtaa. Ensimmäinen yritys epäonnistui: sessio luki laajan
tehtävänannon lupana tehdä kaikki kerralla ja oli kirjoittamassa sivua ennen kuin mitään oli
sovittu. Petri keskeytti ja asetti kolme sääntöä: sivua ei muokata ennen kuin muutokset on
katsottu mockupeista, mitään ei päätetä ennen kuvia, ja päätöslistat käydään läpi
kysymyslaatikoilla noin neljä asiaa kerrallaan.

Sen jälkeen työ eteni ilman yhtään taaksepäin otettua askelta lukuun ottamatta yhtä tapausta
(luku 4). Menetelmä oli:

1. **Kerää ensin koko lista.** Jokainen päätettävä asia yhdeksi numeroiduksi riviksi tiedostoon
   (`copy-v3.md`, `apps-v3.md`), jolla on tila: draft, OK, edit, drop, later.
2. **Näytä neljä kerrallaan.** Yksi kysymyslaatikko per rivi: missä se näkyy, mitä lukee nyt,
   kaksi tai kolme vaihtoehtoa joista yksi suositeltuna, ja vapaa kenttä omalle tekstille tai
   pyynnölle "kolme uutta versiota tähän suuntaan".
3. **Kirjaa heti.** Jokainen vastaus listaan ennen seuraavaa laatikkoa; tiedosto on aina totuus.
4. **Kun laatikko synnyttää suunnan, tee uusi kierros** samasta kohdasta sen suuntaan (otsikko
   meni kolme kierrosta: suunta → kolme versiota → yksi valittu).
5. **Iso rakennepäätös keskeyttää listan.** Kun yksi vastaus muutti rakennetta (Quaesitor pois,
   Somnus tilalle, kaksi ryhmää), lista päivitettiin ennen kuin jatkettiin.
6. **Välitarkistus livenä.** Kun lista oli valmis, tekstit vietiin mockupiin ja katsottiin
   oikeassa ilmeessä; kaksi otsikkoa paljastui päättämättömiksi vasta siellä.

## 2. Miksi se tehosi: viisi tunnettua ilmiötä

Menetelmällä ei ole yhtä vakiintunutta nimeä; se yhdistää päätösanalyysin hajota-ja-kokoa
-periaatteen ja lomakesuunnittelun asteittaisen paljastamisen. Sen teho selittyy tunnetuilla
tuloksilla:

**Valinta-aika kasvaa logaritmisesti vaihtoehtojen määrän mukana** (Hickin laki, 1952:
RT = a + b·log₂(n+1)). Kolme vaihtoehtoa on noin kaksi bittiä; kymmenen kohdan lista, jossa
jokaisella on useita vaihtoehtoja, on kertaluokkaa raskaampi kuin sama sisältö neljän ryhmissä.
Pieni laatikko pitää jokaisen päätöksen halvassa päässä käyrää.

**Liian monta vaihtoehtoa lykkää päätöstä** (valintaylikuorma, Iyengar ja Lepper 2000: 24
hillon pöydästä osti 3 %, kuuden pöydästä 30 %). Lista, jossa on kymmenen avointa kohtaa
kerralla, on 24 hillon pöytä: se houkuttelee katsomaan mutta ei päättämään. Neljän ryhmä on
kuuden pöytä.

**Työmuistin raja on noin neljä kokonaisuutta** (Cowan 2001). Neljä laatikkoa on täsmälleen se
määrä, jonka voi pitää mielessä yhtä aikaa vertaillen. Viides olisi jo pudonnut.

**Peräkkäiset päätökset kuluttavat, ja tauot palauttavat** (päätösväsymys; Danziger ym. 2011
havaitsivat tuomarien myönteisten päätösten putoavan sessiossa ja palaavan tauon jälkeen; itse
mekanismi on kiistanalainen, mutta ilmiö toistuu). Neljän erä on luonnollinen tauko: vastaus,
kirjaus, uusi erä. Kaksi päivää päätöksiä ilman väsymistä oli mahdollista, koska yksikään erä ei
ollut pitkä.

**Yksi kysymys kerrallaan nostaa läpiviennin** (lomaketutkimus: keskustelumuotoiset lomakkeet
noin kaksinkertaistavat valmiiksi täytettyjen osuuden verrattuna koko lomakkeen näyttämiseen
kerralla). Sama koski tätä: koko 90 kohdan lista olisi jäänyt puoliksi luetuksi; laatikoina se
tuli läpi iltapäivässä.

Lisäksi kaksi rakenteellista syytä, jotka eivät ole psykologiaa: **sivukysymykset vähenevät**,
koska laatikko rajaa keskustelun yhteen asiaan eikä keskustelu haaraudu, ja **päätös muotoutuu
vaihtoehtoja vertaillessa**, koska konkreettinen vaihtoehto on helpompi hylätä kuin tyhjästä
keksiä (Petrin havainto: "itse päätös muotoutuu").

## 3. Nimi

Lähin vakiintunut käsite on Raiffan (1968) **hajota ja kokoa** (decomposition–recomposition):
monimutkainen päätös jaetaan osiin, jotka ratkaistaan erikseen ja kootaan. Käytännön muoto on
lomakesuunnittelun **asteittainen paljastaminen** (progressive disclosure, yksi kysymys
kerrallaan). Delphi-menetelmästä tulee kierrosten ajatus: sama kysymys uudestaan tarkentuneena.

Perheen omaksi nimeksi: **päätöslaatikot** (decision boxes). Se kuvaa muodon: numeroitu lista,
neljän laatikon erät, suositus ja vapaa kenttä, kirjaus heti.

## 4. Ainoa virhe, ja mitä se opetti

Kahdessa laatikossa suositeltu vaihtoehto sisälsi uuden otsikon, jonka Claude oli itse
muotoillut. Petri valitsi suosituksen, ja vasta mockupissa huomasi, että sanat olivat vanhaa
kieltä tai ei-yhdessä-päätettyjä. Tämä on **oletusvaihtoehdon vaikutus** (Johnson ja Goldstein
2003: oletus valitaan, koska se luetaan suositukseksi ja se säästää vaivaa; elinluovutuksessa
oletuksen kääntö nosti suostumuksen 42 %:sta 82 %:iin). Sama voima, joka tekee suosituksesta
tehokkaan, tekee siitä vaarallisen, kun suositus kantaa piilotettua sisältöä.

Sääntö siitä eteenpäin: **kun vaihtoehto sisältää uutta tekstiä, teksti näytetään sanatarkasti
kysymyksessä ja merkitään ehdotukseksi, ei "nykyiseksi"**; sivulle näkyvä otsikko on aina oma
laatikkonsa. Ja välitarkistus livenä kuuluu menetelmään, koska se löytää juuri nämä.

## 5. Ohje muihin repoihin

1. Kun edessä on lista päätettäviä asioita (tekstit, kuvat, rakenne, backlogin priorisointi),
   kirjoita ensin tiedosto: numero, missä, mitä nyt, tila.
2. Kysy neljä kerrallaan. Jokaisessa: nykyinen teksti sanatarkasti, 2–3 vaihtoehtoa joista yksi
   suositeltuna, vapaa kenttä. Suosituksen uusi sanamuoto näkyvissä ja merkittynä ehdotukseksi.
3. Kirjaa vastaus tiedostoon ennen seuraavaa erää. Tiedosto on totuus, keskustelu ei.
4. Kun vastaus antaa suunnan, tee tarkentava kierros samasta kohdasta ennen kuin siirryt.
5. Kun vastaus muuttaa rakennetta, päivitä lista ja kerro mitä muuttui.
6. Kun lista on valmis, näytä tulos oikeassa ympäristössä (mockup, esikatselu) ennen kuin sitä
   pidetään päätettynä.
7. Pidä isot linjat (suunta, ilme, rakenne) ennen pieniä (sanamuodot); pienet eivät ratkea
   ennen kuin isot ovat kiinni.

## Lähteet

- Hick, W. E. (1952). On the rate of gain of information. Yhteenveto: [Hick's law, Wikipedia](https://en.wikipedia.org/wiki/Hick%27s_law); katsaus Proctor ja Schneider 2018, [Quarterly Journal of Experimental Psychology](https://web.ics.purdue.edu/~dws/pubs/ProctorSchneider_2018_QJEP.pdf).
- Iyengar, S. ja Lepper, M. (2000). When choice is demotivating. Yhteenveto: [Choice paradox, Coglode](https://www.coglode.com/research/choice-paradox); kritiikki ja toistot: [A better test of choice overload](https://arxiv.org/pdf/2212.03931).
- Cowan, N. (2001). The magical number 4 in short-term memory. [Behavioral and Brain Sciences](https://philpapers.org/rec/COWTMN); jatkokeskustelu [Journal of Cognition 2024](https://journalofcognition.org/articles/10.5334/joc.387).
- Danziger, S., Levav, J. ja Avnaim-Pesso, L. (2011). Extraneous factors in judicial decisions. Yhteenveto ja kritiikki: [Pretrial release judgments and decision fatigue, Cambridge](https://www.cambridge.org/core/journals/judgment-and-decision-making/article/pretrial-release-judgments-and-decision-fatigue/85614F4520F57B10C20F7A3BB786ADF8); nollatulos terveydenhuollon datasta: [Communications Psychology 2025](https://www.nature.com/articles/s44271-025-00207-8).
- Johnson, E. J. ja Goldstein, D. (2003). Do defaults save lives? Science. Yhteenveto: [Default effect](https://yukaichou.com/gamification-analysis/default-effect-johnson-goldstein-organ-donation-opt-in-opt-out/); [Choice without awareness, JPPM 2013](https://www.dangoldstein.com/papers/Smith_Goldstein_Johnson_Choice_Without_Awareness_Defaults_JPPM_2013.pdf).
- Raiffa, H. (1968). Decision Analysis. Hajota ja kokoa -periaatteen sovellus: [Decision-analytic approaches to operational decision making](https://arxiv.org/pdf/1302.3565).
- Delphi-menetelmä: [Wikipedia](https://en.wikipedia.org/wiki/Delphi_method).
- Yksi kysymys kerrallaan lomakkeissa: [Conversational form design](https://roundpushpin.com/knowledge/conversational-form-design); [The science behind conversational form completion rates](https://gnosari.com/blog/conversational-completion-rates).
