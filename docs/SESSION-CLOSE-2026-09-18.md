# Ketjun lopetusdokumentaatio: sivuston uudistus 17.–18.9.2026

**Tekijä:** Petri Korhonen, kirjannut Claude Code · **Ketju:** Claude Code -sessiot 1 ja 2 haarassa
`claude/sw-website-modernization-8676dd` · **Tulos:** V5 livenä https://sunrisesoftware.app/ 18.9.2026

## Mitä saatiin aikaan

| | Ennen (17.9. aamu) | Jälkeen (18.9. ilta) |
|---|---|---|
| Sivu | V4.5, huhtikuu 2026: tumma teema, Fraunces, viisi kuukautta vanhentuneet tuotetilat, Quaesitor ja kellotusarkisto suurimpana, ei metaa eikä GitHub-linkkiä | V5: auringonnousu-ilme, Familjen Grotesk + Public Sans, liikejärjestelmä, päivätyt tilat, neljä päätuotetta kahdessa ryhmässä, seitsemän laatikkoa oikeilla kuvilla, SF3D kryokammiona, head ja OG, GitHub neljästi |
| Dokumentaatio | README ja yksi SEED | CLAUDE.md, CHANGELOG, BUILD_INFO, LESSONS, 13 päätöstietuetta, SEED v3.0.0, copy-v3, apps-v3, look-brief, decision-method, mockup-kierrokset |
| CI | ei mitään | check-site.mjs ja workflow: kuvaviittaukset, head, kielletyt merkkijonot koko tiedostosta, footerin revisiopäivä, GitHub-linkit |
| Repo | yksityinen | julkinen ilman OSS-lisenssiä; työnantajan sovellusten nimet, kumppanien nimet ja muiden projektien sisäiset tilat siivottu kaikista tiedostoista |
| Atlas | status v1 heinäkuulta | status v5, työtapa-artefakti `SUNRISE-TYOTAPA-PAATOSLAATIKOT` |

## Miten se tehtiin: kierrokset

1. **Kartoitus ja protokolla (17.9. päivä):** nykytila kaikista tuoterepoista ja live-sivuilta, Atlas luettu connectorin kautta, dokumentaatio talon standardiin. Ensimmäinen yritys lähti liian lujaa; Petri asetti pelisäännöt (sivu vain yhdessä, mockupit ennen päätöksiä, "pienemmäksi" ei tarkoita "pois").
2. **Look 1 (17.9. ilta):** kolme auringonnousupalettia samalla näkymällä. A hieman C:hen (adr.sws.010).
3. **Flow 1 (17.9. ilta):** elementit, liike ja flow koko sivulla. "Juuri oikea suunta" (adr.sws.011).
4. **Flow 2 (18.9. aamu):** Petrin vastaukset sovellettuna; kolme korjausta; muotokuva irrotettu taustasta.
5. **Type 1 (18.9.):** kuusi kirjasinparia. Familjen Grotesk + Public Sans (adr.sws.012).
6. **Tekstit (18.9. iltapäivä):** 90+ kohtaa päätöslaatikoilla, neljä kerrallaan; Flow 3 välitarkistuksena; kaksi otsikkoa ja kryoteksti uusiksi.
7. **Sovellusnäkymät (18.9. ilta):** 30+ kohtaa samalla menetelmällä; Somnus-laatasta kolme luonnosta; Flow 4 hyväksytty (adr.sws.013).
8. **Sivu (18.9. ilta):** SEED v3.0.0, index.html Flow 4:stä asseteineen, check-site vihreä, julkisen repon siivous, rebase, PR #1, Pages-esikatselu, squash-merge, deploy noin 40 s, todennettu livestä.

## Päätökset (docs/decisions/)

001 staattinen HTML · 002 editoriaalinen rakenne · 003 SF3D:n rooli (suljettu v3:lla: kryokammio) · 004 päivätyt tilat · 005 Atlas valittuna työnä (toteutui työtilalautana) · 006 työnantajan sovellukset pidätetty · 007 GitHub-linkki · 008 React-siirtymä pois roadmapilta · 009 dokumentaatiostandardi · 010 auringonnousu-ilme · 011 Flow 1 suunta · 012 fontit · 013 Flow 4 on sivu.

## Opit (docs/LESSONS.md)

- Suhteellinen aikailmaus sivulla on virhe; jokainen tila kantaa päivän ja CI vertaa footeria.
- Jonossa ollut korjaus ilman paikkaa odottaa ikuisesti; avoin asia elää BUILD_INFO.next-listassa.
- Repo ilman protokollaa saa ensin protokollan; laaja tehtävänanto on suunnittelun aloitus, ei toteutuslupa.
- Suositus ei ole päätös ennen kuin se on luettu ääneen (oletusvaihtoehdon vaikutus).
- Headless-selain palaa ennen kuin kuva on kirjoitettu; valmis-väite tarkistetaan tiedostosta.
- Julkisessa repossa kiellettyjen merkkijonojen tarkistus kattaa koko tiedoston, myös script-lohkot.

## Työtapalöydös

Päätösten pilkkominen neljän laatikon eriin tehosti päätöksentekoa mitattavasti: sivukysymykset
vähenivät ja päätös muotoutui vaihtoehtoja vertaillessa. Ilmiön selittävät Hickin laki,
valintaylikuorma, työmuistin nelosraja, päätösväsymys ja yksi-kysymys-kerrallaan -läpivienti;
ainoan virheen selittää oletusvaihtoehdon vaikutus. Nimi: **päätöslaatikot**. Koko analyysi
lähteineen: `docs/design/decision-method.md`, Atlaksessa `SUNRISE-TYOTAPA-PAATOSLAATIKOT`.

## Avoinna seuraavaan ketjuun (BUILD_INFO.next)

- Petrin luenta livesivusta puhelimella ja työpöydällä; korjaukset uuteen haaraan mainista.
- ADR-ehdotukset 003–013 Atlaksen malliin yhtenä kierroksena (projektitason MCP-merkinnän token uusittava tai otsake pois; connector toimii).
- GitHub-profiilin täyttö (sivu linkittää sen neljästi; profiili oli tyhjä 17.9.).
- Cloudflare Web Analytics; Lighthouse livestä; myöhemmin laajempi EQ-tallenne ja Somnuksen ja Atlaksen oikeat kuvat, jos ne vapautuvat.

## Kiitos

Petri 18.9.: "todella kova sessio ... tehtiin erittäin hyvällä iteraatiolla tekstien ja rakenteiden
muotoilua." Menetelmä on nyt kirjattu, jotta se toistuu.
