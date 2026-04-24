# FAQ articolo - Blender Codex MCP

## Che cos'e Blender Codex MCP?

Blender Codex MCP e un progetto open source che collega Codex a Blender tramite Model Context Protocol. Permette a Codex di ispezionare una scena Blender, eseguire codice Python, catturare screenshot della viewport e preparare modelli per export web come `.glb`.

## Serve tenere Blender aperto?

Si. Blender deve essere aperto perche il server MCP comunica con un addon installato dentro Blender. Se Blender viene chiuso, Codex non puo piu leggere o modificare la scena.

## Devo installare un addon in Blender?

Si. Il progetto include un file `addon.py` da installare in Blender tramite `Edit > Preferences > Add-ons > Install`. Una volta abilitato, l'addon apre un bridge locale su `localhost:9876`.

## Cos'e MCP?

MCP significa Model Context Protocol. E uno standard che permette alle applicazioni AI di collegarsi a strumenti esterni, dati e workflow. In questo caso viene usato per collegare Codex a Blender.

## Posso installarlo come plugin Codex con un click?

Al momento no. Non esiste ancora un marketplace pubblico ufficiale per plugin Codex di terze parti. Il modo consigliato per usarlo oggi e scaricare la repo da GitHub, installare l'addon Blender e configurare il server MCP in Codex.

## Allora a cosa serve lo scaffold plugin Codex incluso nella repo?

Serve come base sperimentale per futuri workflow plugin/locali. Il motore reale del progetto resta il server MCP; lo scaffold plugin documenta come potrebbe essere impacchettato in futuro quando il supporto plugin sara piu aperto.

## Codex puo vedere davvero cosa succede in Blender?

Codex puo leggere informazioni della scena e catturare screenshot della viewport attraverso gli strumenti MCP. Questo rende possibile un ciclo di lavoro piu affidabile: modifica, screenshot, verifica e correzione.

## Posso esportare modelli per il web?

Si. Il progetto include uno strumento `export_glb` e una guida per esportare modelli `.glb`, caricandoli poi su WordPress o in un viewer WebGL come `<model-viewer>`.

## Funziona con Elementor o WordPress?

Si. Una volta esportato il file `.glb`, puoi caricarlo su WordPress e mostrarlo in Elementor con un widget HTML usando `<model-viewer>`.

## E sicuro eseguire codice Blender Python da Codex?

E potente, ma va usato con attenzione. Lo strumento `execute_blender_code` puo eseguire codice Python dentro Blender, quindi e consigliabile salvare sempre il file `.blend` prima di modifiche importanti e lavorare per piccoli passaggi.

## Posso usarlo per configuratori 3D o modelli prodotto?

Si. E uno degli utilizzi piu interessanti: preparare modelli tecnici, scene prodotto, configuratori web, export `.glb` e workflow di automazione 3D.

## Webita puo aiutarmi a integrare AI e automazioni nel mio sito?

Si. Webita lavora su consulenza AI, automazioni operative, integrazioni web, chatbot, workflow personalizzati e strumenti collegati a siti aziendali. Puoi partire dalla pagina [Webita AI](https://webita.eu/it/webita-ai).

