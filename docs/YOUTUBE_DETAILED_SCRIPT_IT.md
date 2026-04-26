# Scaletta video YouTube - Blender Codex MCP

Titolo consigliato:
`Ho collegato Codex a Blender con MCP: AI, modelli 3D e automazione reale`

Titoli alternativi:

- `Codex controlla Blender: come ho creato un MCP per generare modelli 3D`
- `AI + Blender + MCP: ridurre tempi e costi nella produzione di modelli 3D`
- `Da PDF a modello 3D con Codex e Blender: il mio workflow MCP`

Descrizione breve YouTube:

`In questo video mostro come ho collegato Codex a Blender usando un MCP server e un addon locale. L'obiettivo era rispondere a un'esigenza reale: creare e modificare modelli 3D in modo piu rapido, riducendo tempi e costi di produzione. Vediamo cos'e MCP, come funziona il bridge con Blender, come Codex vede la scena tramite screenshot e come si puo arrivare fino all'export GLB per il web.`

Link da mettere in descrizione:

- Repo GitHub: `https://github.com/webita/blender-codex-mcp`
- Articolo guida IT: `https://github.com/webita/blender-codex-mcp/blob/main/docs/ARTICLE_IT.md`
- FAQ IT: `https://github.com/webita/blender-codex-mcp/blob/main/docs/FAQ_IT.md`
- Webita AI: `https://webita.eu/it/webita-ai`

## Struttura consigliata

Durata ideale:

- video breve ma completo: 12-16 minuti
- video piu tutorial: 18-25 minuti

Ritmo:

- inizio veloce e concreto
- spiegazione MCP breve
- contesto cliente
- architettura
- configurazione
- demo con b-roll
- export/web
- chiusura con repo e invito a provarlo

## 1. Hook iniziale - 0:00 / 0:45

Obiettivo: catturare subito l'attenzione mostrando il risultato, non la teoria.

Parlato suggerito:

> In questo video vi faccio vedere una cosa abbastanza potente: ho collegato Codex direttamente a Blender, in modo che possa leggere la scena, modificarla, fare screenshot della viewport e aiutarmi a creare modelli 3D partendo anche da un'immagine o da un disegno tecnico.

> Non e solo un esperimento per smanettoni. Nasce da un'esigenza reale: un cliente aveva bisogno di creare modelli 3D in modo piu massivo, piu veloce e con meno passaggi manuali. Quindi la domanda era: possiamo usare l'AI non solo per scrivere codice, ma per lavorare dentro Blender in maniera controllata?

> La risposta e si, usando un MCP.

B-roll consigliato:

- mostra Blender aperto
- mostra Codex che risponde
- mostra screenshot del modello 3D creato
- mostra la repo GitHub
- taglio rapido del modello `.glb` embed in pagina web, se vuoi

Frase forte:

> L'idea non e sostituire il modellatore 3D, ma abbassare drasticamente i tempi delle operazioni ripetitive e rendere piu veloce arrivare a una prima versione lavorabile.

## 2. Contesto: perche ho creato questo progetto - 0:45 / 2:30

Obiettivo: spiegare il motivo reale e renderlo credibile.

Parlato suggerito:

> Questo progetto nasce da un caso molto pratico. Dovevamo lavorare su strutture tecniche e modelli 3D da usare poi anche sul web, ad esempio in configuratori o pagine prodotto.

> Il problema e che produrre modelli 3D uno per uno richiede tempo: bisogna interpretare il disegno, ricostruire la struttura, correggere inclinazioni, pannelli, materiali, camera, luci, esportare, testare sul sito.

> Se devi farlo una volta, va bene. Se devi farlo molte volte, diventa un collo di bottiglia.

> Quindi ho iniziato a ragionare in questo modo: Codex e bravissimo a scrivere codice e ragionare sui passaggi tecnici. Blender ha una API Python molto potente. Ma mancava il ponte tra i due: Codex doveva poter vedere cosa succedeva in Blender, non solo generare script alla cieca.

Punti da dire:

- esigenza cliente reale
- modelli 3D piu massivi
- riduzione dei tempi di produzione
- riduzione di costi operativi
- workflow piu iterativo
- AI come assistente tecnico, non come bacchetta magica

B-roll:

- PDF/disegno tecnico
- Blender con scena vuota
- scena che si popola
- correzioni successive
- esportazione GLB

## 3. Che cos'e MCP, spiegato semplice - 2:30 / 4:00

Obiettivo: spiegare MCP senza diventare troppo teorico.

Parlato suggerito:

> MCP sta per Model Context Protocol. Possiamo immaginarlo come uno standard che permette a un assistente AI di collegarsi a strumenti esterni.

> Normalmente un'AI come Codex puo ragionare, scrivere codice, leggere file, modificare un progetto. Ma se voglio farle controllare Blender, serve un'interfaccia. Serve un modo sicuro e strutturato per dire: questi sono gli strumenti disponibili, questi sono i comandi che puoi eseguire, queste sono le informazioni che puoi leggere.

> L'MCP fa proprio questo: espone degli strumenti. Nel nostro caso, strumenti come leggere la scena, ottenere informazioni sugli oggetti, eseguire codice Python dentro Blender, fare screenshot della viewport ed esportare un GLB.

Esempio semplice:

> Quindi invece di dire a Codex "scrivimi uno script Blender e speriamo funzioni", posso dire "guarda la scena, dimmi cosa c'e, fai una modifica, mostrami uno screenshot e poi correggiamo".

Frase chiave:

> Il valore dell'MCP non e solo eseguire comandi. E creare un ciclo di feedback tra Codex e il software che vogliamo controllare.

B-roll:

- piccolo schema a schermo:

```text
Codex -> MCP Server -> Blender Addon -> Blender Scene
                      <- Screenshot / Scene Info <-
```

## 4. Come funziona Blender Codex MCP - 4:00 / 5:45

Obiettivo: spiegare l'architettura in modo pratico.

Parlato suggerito:

> La logica del progetto e questa: dentro Blender installiamo un addon. Questo addon apre un bridge locale, di default sulla porta 9876.

> Dall'altra parte, Codex avvia un server MCP dalla repo. Quando io chiedo a Codex di fare qualcosa su Blender, Codex chiama uno strumento MCP. Il server MCP prende quella richiesta e la inoltra a Blender.

> Blender esegue il comando e restituisce il risultato. Se serve, Codex puo anche chiedere uno screenshot della viewport, cosi possiamo verificare visivamente quello che ha fatto.

Punti tecnici da mostrare:

- addon Blender
- porta `localhost:9876`
- server MCP in repo
- config `~/.codex/config.toml`
- strumenti disponibili

Strumenti da nominare:

- `get_scene_info`
- `get_object_info`
- `get_viewport_screenshot`
- `execute_blender_code`
- `sync_camera_to_viewport`
- `export_glb`

Parlato suggerito:

> La parte importante e lo screenshot. Perche nei lavori 3D non basta dire "ho creato un cubo" o "ho ruotato un pannello". Devi vedere se e ruotato bene, se la camera e giusta, se i supporti escono fuori, se il modello e centrato. Questo e quello che rende il workflow molto piu concreto.

## 5. Le difficolta iniziali - 5:45 / 7:15

Obiettivo: rendere il video umano e credibile, spiegando che non e nato perfetto.

Parlato suggerito:

> Ovviamente non e stato tutto immediato. Sono partito da una base MCP gia esistente, pensata in modo piu generico, e l'ho adattata a un workflow verticale per Codex e Blender.

> Una delle prime difficolta e stata capire bene come far comunicare Codex con Blender in modo stabile. Non bastava avere Blender aperto: bisognava avere un addon che restasse in ascolto, un server MCP che esponesse tool coerenti, e soprattutto un modo per verificare visivamente il risultato.

> Poi ci sono state le classiche difficolta da modello 3D: orientamento dei pannelli, camera sbagliata, elementi che uscivano fuori, struttura da centrare, luci e materiali da sistemare. Ed e proprio li che il workflow ha iniziato ad avere senso: Codex faceva una modifica, guardavamo lo screenshot, correggevamo, e piano piano arrivavamo al risultato.

Punti da raccontare:

- base MCP esistente adattata
- trasformazione verticale per Codex
- ponte locale con Blender
- screenshot come feedback visivo
- iterazioni reali su modello tecnico
- correzioni su camera, pannelli, materiali, supporti

Frase chiave:

> Il valore non e stato "farlo perfetto al primo colpo", ma creare un sistema che permette di correggere velocemente.

## 6. Installazione: repo e addon Blender - 7:15 / 9:30

Obiettivo: spiegare i passaggi pratici.

Parlato suggerito:

> Vediamo velocemente come si installa. La repo e pubblica su GitHub e si chiama `blender-codex-mcp`.

Mostra:

```bash
git clone https://github.com/webita/blender-codex-mcp.git
cd blender-codex-mcp
```

Parlato:

> Dentro la repo trovate il file `addon.py`. Questo va installato in Blender.

Passaggi Blender:

1. aprire Blender
2. andare su `Edit > Preferences`
3. sezione `Add-ons`
4. `Install...`
5. scegliere `addon.py`
6. abilitarlo
7. nella viewport premere `N`
8. aprire tab `BlenderCodexMCP`
9. cliccare `Connect to MCP server`

Parlato:

> A questo punto Blender e pronto. Sta ascoltando localmente sulla porta 9876.

B-roll:

- installazione addon
- pannello laterale Blender
- bottone `Connect to MCP server`

## 7. Configurazione Codex - 9:30 / 11:00

Obiettivo: mostrare la parte che spesso blocca gli utenti.

Parlato suggerito:

> Ora dobbiamo dire a Codex come avviare il server MCP. Questo si fa nel file di configurazione di Codex, di solito `~/.codex/config.toml`.

Mostra snippet:

```toml
[mcp_servers.blender]
command = "uv"
args = [
  "--directory",
  "/absolute/path/to/blender-codex-mcp",
  "run",
  "blender-codex-mcp"
]

[mcp_servers.blender.env]
BLENDER_HOST = "localhost"
BLENDER_PORT = "9876"
DISABLE_TELEMETRY = "true"
```

Parlato:

> La cosa importante e sostituire questo percorso con il percorso reale della repo sul vostro computer. Poi riavviate Codex, aprite Blender, attivate l'addon e siete pronti.

Nota da dire:

> Al momento non c'e un marketplace pubblico di plugin Codex di terze parti. Quindi l'installazione oggi e tramite GitHub e configurazione MCP manuale. Nella repo ho lasciato anche uno scaffold plugin, ma lo considero una base futura, non il percorso principale per l'utente.

## 8. Demo: Codex controlla Blender - 11:00 / 15:00

Obiettivo: mostrare il risultato, alternando b-roll e spiegazione.

Prompt 1:

```text
Inspect the open Blender scene and tell me what objects are present.
```

Parlato:

> Qui Codex non sta inventando. Sta interrogando Blender e leggendo davvero gli oggetti presenti nella scena.

Prompt 2:

```text
Take a viewport screenshot so we can verify the camera and model framing.
```

Parlato:

> Questo e fondamentale: Codex puo chiedere uno screenshot della viewport. Quindi possiamo vedere se il modello e nella posizione giusta, se la camera e corretta e se le modifiche hanno senso.

Prompt 3:

```text
Create a clean product-view camera and add soft studio lighting.
```

Parlato:

> Qui iniziamo a usare Codex come assistente 3D: non solo modifica oggetti, ma prepara anche camera, luci e scena per una visualizzazione migliore.

Prompt 4:

```text
Center the visible model, place it on the ground plane, and prepare it for GLB export.
```

Parlato:

> Questo e il tipo di automazione che riduce davvero tempo: centrare il modello, pulire la scena, preparare materiali e export sono operazioni ripetitive che spesso si fanno a mano.

B-roll:

- Codex che riceve prompt
- Blender cambia
- screenshot viewport
- modello tecnico creato/corretto
- confronto prima/dopo se disponibile

## 9. Demo dal caso reale: immagine/PDF verso modello 3D - 15:00 / 18:00

Obiettivo: collegare la tecnologia al caso concreto del cliente.

Parlato suggerito:

> Nel caso reale, siamo partiti da un disegno tecnico e abbiamo chiesto a Codex di ricostruire una struttura 3D in Blender. Non e stato un singolo prompt magico. E stato un processo.

> Prima la struttura base, poi i pannelli, poi le inclinazioni, poi la camera, poi materiali, luci, export. Alcune cose all'inizio erano sbagliate: pannelli orientati male, tubolari troppo visibili, camera non coerente. Pero il punto e che grazie al bridge potevamo correggere in modo iterativo.

> Questo per me e il modo piu realistico di usare l'AI nel 3D: non sostituisce il giudizio umano, ma accelera la produzione e permette di arrivare piu velocemente a una base utilizzabile.

Frase chiave:

> L'AI propone e automatizza; l'umano guida, controlla e decide.

B-roll:

- PDF/disegno tecnico
- prime versioni sbagliate
- correzioni successive
- modello finale
- export/preview web

## 10. Export GLB e utilizzo sul sito - 18:00 / 19:30

Obiettivo: chiudere il cerchio business: da Blender al web.

Parlato suggerito:

> Una volta preparato il modello, possiamo esportarlo in `.glb`, che e un formato molto comodo per il web.

> Per esempio lo possiamo caricare su WordPress e visualizzarlo con un viewer WebGL come `model-viewer`, anche dentro Elementor usando un widget HTML.

> Questo significa che il workflow non si ferma a Blender: possiamo arrivare a una pagina prodotto, a un configuratore, o a una scheda tecnica interattiva.

Mostra se possibile:

- file `.glb`
- pagina WordPress/Elementor
- modello 3D embed

Frase chiave:

> Il valore commerciale e qui: passare piu velocemente da disegno tecnico a modello 3D pubblicabile.

## 11. Collegamento ai servizi Webita AI - 19:30 / 20:30

Obiettivo: CTA naturale, collegata al problema.

Parlato suggerito:

> Questo progetto rientra in una cosa piu ampia che sto portando avanti con Webita AI: usare l'intelligenza artificiale non solo per generare testi o immagini, ma per automatizzare processi reali.

> In questo caso il processo e 3D e Blender. In altri casi puo essere un CRM, un sito web, un gestionale, un sistema di ticket, una dashboard o un e-commerce.

> Il punto e sempre lo stesso: capire dove ci sono passaggi ripetitivi, collegare gli strumenti giusti e creare un workflow che faccia risparmiare tempo.

CTA:

> Se avete un processo aziendale che vorreste automatizzare con AI, trovate il link a Webita AI in descrizione.

## 12. Chiusura - 20:30 / 21:30

Obiettivo: ricapitolare e invitare a provare il repo.

Parlato suggerito:

> Ricapitolando: abbiamo collegato Codex a Blender usando MCP, installato un addon locale, configurato Codex, fatto leggere la scena, modificato il modello, usato screenshot per verificare il risultato ed esportato verso il web.

> La repo e pubblica su GitHub. Dentro trovate il codice, la guida di installazione, le FAQ, l'articolo e anche una guida per embed WordPress.

> Se il progetto vi interessa, provatelo, aprite una issue, lasciate una stella alla repo e fatemi sapere quali workflow vorreste automatizzare dentro Blender.

Ultima frase:

> Secondo me il futuro non e solo chiedere all'AI di creare qualcosa, ma collegarla agli strumenti giusti per farla lavorare dentro i processi reali.

## Sequenza B-roll consigliata

1. GitHub repo aperta
2. README con Quick Install
3. Blender vuoto
4. installazione addon
5. tab BlenderCodexMCP
6. Codex config
7. prompt in Codex
8. scena Blender che cambia
9. viewport screenshot
10. modello tecnico ricostruito
11. errori/correzioni se vuoi raccontarli
12. export `.glb`
13. embed WordPress
14. Webita AI page

## Prompt da usare nel video

```text
Inspect the open Blender scene and tell me what objects are present.
```

```text
Take a viewport screenshot so we can verify the camera and model framing.
```

```text
Create a clean product-view camera and add soft studio lighting.
```

```text
Center the visible model, place it on the ground plane, and prepare it for GLB export.
```

```text
Export the selected model as a GLB file for web embedding.
```

```text
Use this reference image as guidance and recreate a simplified technical 3D version in Blender.
```

## Capitoli YouTube consigliati

```text
00:00 Intro: Codex controlla Blender
00:45 Perche nasce questo progetto
02:30 Cos'e MCP
04:00 Come funziona Blender Codex MCP
05:45 Difficolta iniziali e adattamento per Codex
07:15 Installazione addon Blender
09:30 Configurazione Codex MCP
11:00 Demo: ispezione scena e screenshot
15:00 Da immagine/PDF a modello 3D
18:00 Export GLB e WordPress
19:30 Webita AI e automazioni reali
20:30 Repo GitHub e conclusione
```

## Descrizione YouTube pronta

```text
In questo video mostro come ho collegato Codex a Blender usando un MCP server e un addon locale.

L'obiettivo nasce da una necessita reale: creare modelli 3D tecnici in modo piu rapido, riducendo tempi e costi di produzione. Con Blender Codex MCP, Codex puo ispezionare la scena, eseguire Blender Python, catturare screenshot della viewport, correggere camera/materiali/luci ed esportare modelli GLB per il web.

Repo GitHub:
https://github.com/webita/blender-codex-mcp

Articolo guida:
https://github.com/webita/blender-codex-mcp/blob/main/docs/ARTICLE_IT.md

FAQ:
https://github.com/webita/blender-codex-mcp/blob/main/docs/FAQ_IT.md

Webita AI:
https://webita.eu/it/webita-ai

Nota: al momento non esiste un marketplace pubblico ufficiale per plugin Codex di terze parti. Il progetto si installa da GitHub come MCP server, con addon Blender e configurazione Codex manuale.
```

## Pinned comment pronto

```text
Repo pubblica: https://github.com/webita/blender-codex-mcp

Installazione oggi: GitHub + addon Blender + configurazione MCP in Codex.
Lo scaffold plugin Codex incluso nella repo e sperimentale/futuro, non un marketplace one-click.
```

