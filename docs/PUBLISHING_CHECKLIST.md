# Publishing Checklist For GitHub And YouTube

If you want to publish Blender Codex MCP publicly, this is the practical checklist.

## Before Publishing The Repo

- confirm the repo path in the README is generic, not machine-specific
- confirm the addon installs from `addon.py`
- confirm the package starts with `uv run blender-codex-mcp`
- confirm the default port is documented
- confirm telemetry behavior is documented clearly
- confirm license is present
- confirm credits are present

## Recommended Repo Improvements

- add 1 short GIF in the README
- add 1 screenshot of the Blender sidebar tab
- add 1 screenshot of Codex using the tools
- add docs for WordPress/web export
- add troubleshooting
- add known limitations

## Suggested GitHub Release Structure

### Repository title

`blender-codex-mcp`

### Short description

`Connect Codex to a live Blender scene through MCP for inspection, screenshots, and Python execution.`

### Topics

Suggested topics:

- blender
- mcp
- model-context-protocol
- codex
- ai-tools
- python
- 3d
- gltf
- glb

## Suggested YouTube Video Structure

1. What the project does
2. Install the Blender addon
3. Add the MCP server config in Codex
4. Restart Codex
5. Connect Blender
6. Ask Codex to inspect the scene
7. Ask Codex to create or modify something
8. Capture viewport screenshots
9. Export `.glb`
10. Embed the model on WordPress

## Suggested Demo Prompts For The Video

- `Controlla la scena Blender e dimmi cosa contiene.`
- `Fai uno screenshot della viewport e correggi la camera.`
- `Crea una luce studio morbida per un modello prodotto.`
- `Organizza gli oggetti in collezioni e prepara il file per export GLB.`

## Suggested Video Notes

Make these clear in the video:

- Blender must be open
- the addon must be enabled
- the MCP server must be loaded in Codex
- `execute_blender_code` is powerful and should be used carefully
- users should save the `.blend` before large changes

## What I Changed For Documentation

For this publishable version, I recommend shipping:

- stronger README
- WordPress/embed guide
- publishing checklist

That already makes the repo much easier for other people to adopt.
