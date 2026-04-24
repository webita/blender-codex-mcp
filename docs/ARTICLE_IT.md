# Collegare Codex a Blender con MCP: guida pratica per controllare scene 3D, esportare GLB e pubblicare sul web

SEO title:
`Codex + Blender MCP: guida pratica per controllare Blender con AI`

Meta description:
`Scopri come collegare Codex a Blender con un server MCP locale: installazione addon, configurazione, screenshot viewport, automazioni Python, export GLB e embed web.`

Repository:
[https://github.com/webita/blender-codex-mcp](https://github.com/webita/blender-codex-mcp)

## Introduzione

Lavorare in Blender con un assistente AI diventa molto piu interessante quando l'assistente non si limita a scrivere codice Python, ma puo anche ispezionare la scena, verificare cosa ha creato, catturare screenshot della viewport e iterare sul modello.

Questo e l'obiettivo di **Blender Codex MCP**: collegare Codex a una sessione Blender aperta usando il **Model Context Protocol**, con un addon locale dentro Blender e un server MCP eseguito da Codex.

In pratica:

- Blender esegue un addon locale
- l'addon apre un bridge su `localhost:9876`
- Codex avvia un server MCP
- il server MCP inoltra i comandi a Blender
- Codex puo ispezionare, modificare, fotografare e preparare la scena per l'export

Il progetto e disponibile su GitHub:

[https://github.com/webita/blender-codex-mcp](https://github.com/webita/blender-codex-mcp)

## Perche usare MCP con Blender

Un modello AI puo gia scrivere script Blender Python. Il problema e che, senza feedback, lavora quasi alla cieca.

Con un bridge MCP, invece, il ciclo diventa piu utile:

1. Codex legge la scena.
2. Codex modifica un oggetto o crea nuova geometria.
3. Codex cattura uno screenshot della viewport.
4. L'utente verifica visivamente.
5. Codex corregge camera, materiali, luci o export.

Questo approccio e molto adatto a:

- mockup tecnici
- scene prodotto
- modelli per configuratori web
- preparazione di file `.glb`
- automazioni Blender ripetitive
- workflow in cui serve una revisione visiva progressiva

## Cos'e MCP

MCP, Model Context Protocol, e uno standard aperto per collegare applicazioni AI a sistemi esterni, strumenti, sorgenti dati e workflow.

La documentazione ufficiale lo descrive come uno standard per connettere applicazioni AI a strumenti e sistemi esterni in modo coerente:

[Model Context Protocol documentation](https://modelcontextprotocol.io/)

Nel nostro caso, il sistema esterno e Blender.

## Cosa fa Blender Codex MCP

Blender Codex MCP espone a Codex strumenti come:

- `get_scene_info`: leggere oggetti, materiali e stato della scena
- `get_object_info`: ispezionare un singolo oggetto
- `get_viewport_screenshot`: catturare uno screenshot della viewport
- `execute_blender_code`: eseguire Python dentro Blender
- `blender_health_check`: verificare che Blender sia raggiungibile
- `sync_camera_to_viewport`: copiare la vista corrente nella camera attiva
- `export_glb`: esportare la scena o gli oggetti selezionati in `.glb`

Questo non sostituisce Blender. Lo rende controllabile da Codex.

## Requisiti

Prima di iniziare servono:

- Blender installato
- Codex desktop o un runtime Codex compatibile con MCP
- `uv` installato
- Python 3.10 o superiore
- la repo `blender-codex-mcp`

`uv` e un package/project manager Python molto veloce, usato qui per avviare il server MCP:

[uv documentation](https://docs.astral.sh/uv/)

## Installazione

Clona il repository:

```bash
git clone https://github.com/webita/blender-codex-mcp.git
cd blender-codex-mcp
```

Poi apri Blender e installa l'addon:

1. apri Blender
2. vai in `Edit > Preferences > Add-ons`
3. clicca `Install...`
4. seleziona `addon.py` dalla repo
5. abilita `Interface: Blender Codex MCP`
6. nella viewport premi `N`
7. apri la tab `BlenderCodexMCP`
8. clicca `Connect to MCP server`

Di default Blender ascolta su:

```text
localhost:9876
```

## Configurare Codex

Aggiungi questa configurazione a `~/.codex/config.toml`:

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

Sostituisci `/absolute/path/to/blender-codex-mcp` con il percorso reale della repo.

Dopo la modifica, riavvia Codex.

## Primo test

Con Blender aperto e addon connesso, puoi chiedere a Codex:

```text
Inspect the open Blender scene and take a viewport screenshot.
```

Oppure in italiano:

```text
Controlla la scena Blender aperta e fammi uno screenshot della viewport.
```

Se tutto e configurato correttamente, Codex dovrebbe riuscire a leggere la scena e usare gli strumenti MCP esposti dal server.

## Workflow consigliato

Il modo migliore di lavorare non e chiedere a Codex di rifare tutta la scena in un solo passaggio.

Meglio procedere cosi:

1. ispezione scena
2. modifica piccola e verificabile
3. screenshot viewport
4. correzione di camera, scala, materiali o luci
5. export finale

Esempi di prompt utili:

```text
Inspect the scene and tell me which objects are present.
```

```text
Create a clean product-view camera and add soft studio lighting.
```

```text
Center the selected model and place it on the ground plane.
```

```text
Export the selected model as a GLB file for web embedding.
```

## Export GLB e WordPress

Per pubblicare un modello 3D sul web, il formato piu pratico e spesso `.glb`.

Un flusso semplice e:

1. prepara il modello in Blender
2. centra la geometria
3. applica materiali leggeri
4. imposta camera e luci per preview
5. esporta `.glb`
6. carica il file su WordPress
7. visualizzalo con un viewer WebGL

Una soluzione comoda per WordPress/Elementor e usare `<model-viewer>`:

[model-viewer documentation](https://modelviewer.dev/)

Esempio HTML:

```html
<script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>

<model-viewer
  src="https://example.com/wp-content/uploads/model.glb"
  camera-controls
  auto-rotate
  interaction-prompt="none"
  shadow-intensity="1"
  exposure="1"
  style="width:100%; height:500px; background:#fff;"
></model-viewer>
```

Nel repository trovi anche una guida dedicata:

[WordPress embed guide](https://github.com/webita/blender-codex-mcp/blob/main/docs/WORDPRESS_EMBED.md)

## Plugin Codex: cosa significa davvero

Una domanda naturale e: "Si puo installare come plugin Codex con un click?"

Al momento, non esiste un marketplace pubblico ufficiale per plugin Codex di terze parti. Per questo il percorso principale e:

1. installazione da GitHub
2. addon Blender
3. configurazione MCP in Codex

La repo include anche uno scaffold plugin Codex locale, utile per workflow futuri o sperimentali, ma oggi non va presentato come installazione principale.

In breve:

- MCP server: e il motore reale
- Blender addon: e il bridge dentro Blender
- plugin scaffold: e una base futura/locale per packaging plugin

## Sicurezza

Lo strumento `execute_blender_code` puo eseguire Python dentro Blender.

Questo e potente, ma richiede attenzione:

- salva il file `.blend` prima di modifiche importanti
- lavora a piccoli passi
- verifica spesso con screenshot
- usa repo e script di cui ti fidi

## Riferimenti

- Repository Blender Codex MCP: [https://github.com/webita/blender-codex-mcp](https://github.com/webita/blender-codex-mcp)
- Model Context Protocol: [https://modelcontextprotocol.io/](https://modelcontextprotocol.io/)
- Blender Python API: [https://docs.blender.org/api/](https://docs.blender.org/api/)
- uv documentation: [https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)
- model-viewer: [https://modelviewer.dev/](https://modelviewer.dev/)

## Conclusione

Blender Codex MCP non e un semplice esperimento: e un modo pratico per rendere Blender piu accessibile a workflow AI assistiti.

La parte piu interessante non e solo generare codice Python, ma chiudere il ciclo:

```text
Codex modifica -> Blender mostra -> Codex verifica -> utente corregge -> export web
```

Per chi lavora con modelli tecnici, configuratori, scene prodotto o contenuti 3D per siti web, questo apre un workflow molto concreto.

Repository:

[https://github.com/webita/blender-codex-mcp](https://github.com/webita/blender-codex-mcp)
