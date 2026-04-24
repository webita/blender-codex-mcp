# Blender Codex MCP

Blender Codex MCP connects Codex to Blender through the Model Context Protocol.

- Blender runs a local socket addon on `localhost:9876` by default.
- Codex runs an MCP server from this repository.
- The MCP server forwards tool calls into Blender.

This fork is focused on practical 3D work with Codex: scene inspection, viewport screenshots, Python execution inside Blender, and optional asset/model integrations.

## Quick Install

1. Clone this repo.

```bash
git clone https://github.com/webita/blender-codex-mcp.git
cd blender-codex-mcp
```

2. Install [addon.py](./addon.py) in Blender.
3. Enable the addon and click `Connect to MCP server` in the Blender sidebar.
4. Add the MCP config below to `~/.codex/config.toml`.
5. Restart Codex and ask it to inspect Blender.

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

Useful first prompt:

```text
Inspect the open Blender scene and take a viewport screenshot.
```

> Note: Codex does not currently provide a public third-party plugin marketplace. This repository is meant to be installed from GitHub as an MCP server. A local Codex plugin scaffold is included for future/plugin-based workflows.

## MCP Server Vs Codex Plugin

These are related, but not the same thing.

- This repository is primarily an MCP server plus Blender addon.
- An MCP server exposes tools that Codex can call.
- A Codex plugin can be used as a packaging/distribution layer to make installation, discovery, and setup easier.

So yes: this project can also become a Codex plugin.

The cleanest public setup is usually:

1. keep this repo as the source of truth for the Blender addon and MCP server
2. optionally publish a Codex plugin that helps users install or configure the MCP server

In other words:

- the MCP server is the engine
- the plugin can be the smoother installation experience

This repository now also includes a repo-local plugin scaffold at [plugins/blender-codex-connector](./plugins/blender-codex-connector), so you can publish the MCP project and evolve a Codex plugin alongside it without splitting the codebase yet.

## Why This Project Exists

Most AI coding agents can write Blender Python, but they cannot see or control a live Blender scene well enough to iterate safely.

This project solves that by giving Codex a bridge to:

- inspect the current scene
- query objects
- capture viewport screenshots
- execute Blender Python step by step
- optionally search/import Poly Haven, Sketchfab, Hyper3D Rodin, and Hunyuan3D content

The result is a much tighter loop for:

- product renders
- architectural/technical mockups
- scene cleanup and organization
- scripted modeling
- export-ready 3D preparation for the web

## Features

- `get_scene_info`: inspect the current Blender scene
- `get_object_info`: inspect a specific object
- `get_viewport_screenshot`: capture the current viewport for visual feedback
- `execute_blender_code`: run Python inside Blender
- `blender_health_check`: verify that Blender and the socket bridge are reachable
- `sync_camera_to_viewport`: copy the current 3D viewport view into the active scene camera
- `export_glb`: export the scene or selected objects as `.glb`
- optional asset integrations from Poly Haven and Sketchfab
- optional AI generation integrations through Hyper3D Rodin and Hunyuan3D

## Repository Layout

- [addon.py](./addon.py): Blender addon that opens the socket bridge
- [src/blender_codex_mcp/server.py](./src/blender_codex_mcp/server.py): MCP server
- [main.py](./main.py): package entrypoint
- [TERMS_AND_CONDITIONS.md](./TERMS_AND_CONDITIONS.md): terms
- [assets](./assets): addon screenshots/icons
- [docs/WORDPRESS_EMBED.md](./docs/WORDPRESS_EMBED.md): export and embed workflow for WordPress
- [docs/PUBLISHING_CHECKLIST.md](./docs/PUBLISHING_CHECKLIST.md): GitHub/release/video checklist
- [docs/YOUTUBE_DEMO_SCRIPT.md](./docs/YOUTUBE_DEMO_SCRIPT.md): video recording outline and demo prompts
- [examples/web_ready_scene_setup.py](./examples/web_ready_scene_setup.py): generic example for centering geometry, applying base materials, and preparing a scene for web export
- [plugins/blender-codex-connector](./plugins/blender-codex-connector): repo-local Codex plugin scaffold for this MCP project
- [.agents/plugins/marketplace.json](./.agents/plugins/marketplace.json): optional local marketplace entry for plugin ordering/discovery

## Requirements

- Blender installed locally
- Codex desktop or another MCP-compatible Codex runtime
- `uv` installed locally
- Python 3.10+

## Install The Blender Addon

1. Open Blender.
2. Go to `Edit > Preferences > Add-ons`.
3. Click `Install...`.
4. Select [addon.py](./addon.py).
5. Enable `Interface: Blender Codex MCP`.
6. In the 3D viewport, press `N`, open the `BlenderCodexMCP` tab, and click `Connect to MCP server`.

By default the addon listens on `localhost:9876`.

## Configure Codex

Add this to `~/.codex/config.toml`:

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

Then restart Codex.

Only one MCP server should connect to the Blender addon at a time.

## Codex Plugin Scaffold

If you want to ship this as a Codex plugin too, start from:

- [plugins/blender-codex-connector/.codex-plugin/plugin.json](./plugins/blender-codex-connector/.codex-plugin/plugin.json)
- [plugins/blender-codex-connector/.mcp.json](./plugins/blender-codex-connector/.mcp.json)
- [.agents/plugins/marketplace.json](./.agents/plugins/marketplace.json)

The current scaffold is intentionally simple:

- plugin metadata lives in the plugin folder
- the plugin points back to this repo's MCP server with `uv`
- you can fill in public URLs, screenshots, and marketplace details when you publish

At the moment, treat this as experimental packaging. The recommended public install path is still the manual MCP setup from GitHub.

## Quick Start

1. Open Blender.
2. Enable the addon.
3. Click `Connect to MCP server` in Blender.
4. Restart or reopen Codex so it loads the MCP server.
5. Ask Codex to inspect the scene before making changes.

Useful first prompts:

- `Controlla la scena Blender e dimmi cosa contiene.`
- `Fai uno screenshot della viewport e dimmi se la camera è corretta.`
- `Sincronizza la camera alla vista attuale e poi fammi uno screenshot.`
- `Crea una camera isometrica e una luce studio morbida.`
- `Scrivi uno script Blender pulito per organizzare gli oggetti in collezioni.`
- `Prepara il modello per export GLB per il web.`

## Recommended Workflow

For best results, ask Codex to work in small steps:

1. inspect the scene
2. make one structural change
3. capture a viewport screenshot
4. refine
5. prepare export

This is safer than asking for a huge one-shot scene rewrite.

## Best Practices

- Save the `.blend` file before large operations.
- Ask for viewport screenshots often.
- Prefer incremental modeling over giant code dumps.
- Keep the scene organized in collections if you plan to export for the web.
- For web export, keep materials simple and avoid unnecessary geometry.
- Use `.glb` for distribution unless you have a specific reason to export another format.

## Export For The Web

Short version:

1. prepare the model in Blender
2. export as `.glb`
3. upload the `.glb`
4. embed it in WordPress with a WebGL viewer

Full workflow:

- [WordPress embed guide](./docs/WORDPRESS_EMBED.md)

## Examples

- [examples/web_ready_scene_setup.py](./examples/web_ready_scene_setup.py)

This example is intentionally generic and useful for many scenes:

- center geometry
- place the model on the ground plane
- apply simple base materials
- create a clean default camera
- add basic lights for screenshots and GLB export prep

## Troubleshooting

### Codex cannot connect to Blender

- Make sure Blender is open.
- Make sure the addon is enabled.
- Make sure the addon says it is running on port `9876`.
- Make sure your Codex config points to the correct repo path.
- Restart Codex after editing `~/.codex/config.toml`.

### The MCP server loads but tools fail

- Check that Blender is still open.
- Check that no second MCP server is already attached.
- Check whether the addon and repo version match.

### Viewport screenshots fail

- Make sure a `VIEW_3D` area exists in the active screen layout.
- Switch Blender back to a normal layout with a visible 3D viewport.

### Telemetry questions

Telemetry is conservative by default in this fork.

- Recommended for local/private use: `DISABLE_TELEMETRY=true`
- Internal config also supports `BLENDER_MCP_TELEMETRY_ENABLED`

If you publish publicly, document telemetry behavior clearly in GitHub and in the video.

## FAQ

### Is this a one-click Codex plugin?

Not yet. Today the reliable public install path is GitHub plus manual MCP configuration. The repo includes an experimental Codex plugin scaffold, but there is currently no public third-party Codex plugin marketplace for one-click discovery and install.

### Does Blender need to stay open?

Yes. The MCP server talks to the Blender addon running inside a live Blender session.

### Does this install Blender automatically?

No. Users install Blender separately, then install [addon.py](./addon.py) in Blender.

### Can Codex see what it is doing in Blender?

It can inspect scene data and request viewport screenshots through the MCP tools. That feedback loop is the main reason this bridge is useful.

### Can I use this for web exports?

Yes. Use `export_glb` or Blender's built-in export workflow, then embed the `.glb` with a WebGL viewer. See [docs/WORDPRESS_EMBED.md](./docs/WORDPRESS_EMBED.md).

## What I Would Improve Before Public Launch

The project is already publishable, but these would make it stronger:

1. Add a short demo GIF or video in the README.
2. Add a `docs/` folder with setup, troubleshooting, and export examples.
3. Add a release section with tested versions of Blender and Codex.
4. Add a small FAQ.

I have added the docs pieces that help most immediately for GitHub and YouTube.

## Known Limitations

- This bridge depends on a live Blender session.
- The addon uses a local socket transport; if Blender is closed, tools fail.
- `execute_blender_code` is powerful and should be used carefully.
- Viewport capture depends on a valid 3D viewport being visible in Blender.

## Safety Notes

`execute_blender_code` can run arbitrary Python inside Blender.

Before large operations:

- save your file
- work incrementally
- verify with screenshots

## License

MIT. See [LICENSE](./LICENSE).

## Credits

Blender Codex MCP is a Codex-focused fork adapted by Webita - Giorgio Sanna.

Thanks to the original open-source Blender MCP project for the base Blender socket and MCP workflow.
