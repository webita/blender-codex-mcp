# Connect Codex To Blender With MCP: Inspect Scenes, Edit Models, Export GLB, And Embed 3D On The Web

SEO title:
`Codex + Blender MCP: Control Blender with AI`

Meta description:
`A practical guide to connecting Codex to Blender with a local MCP server and Blender addon: scene inspection, viewport screenshots, Blender Python execution, GLB export, and web embedding.`

Repository:
[https://github.com/webita/blender-codex-mcp](https://github.com/webita/blender-codex-mcp)

## Introduction

AI coding agents can already write Blender Python. The harder part is giving the agent a feedback loop.

If the agent cannot inspect the scene, capture a viewport screenshot, or verify the result, it is mostly working blind.

**Blender Codex MCP** solves that problem by connecting Codex to a live Blender session through the **Model Context Protocol**.

The architecture is simple:

- Blender runs a local addon
- the addon opens a bridge on `localhost:9876`
- Codex runs an MCP server from this repository
- the MCP server forwards tool calls into Blender
- Codex can inspect, edit, screenshot, and prepare the scene for export

Repository:

[https://github.com/webita/blender-codex-mcp](https://github.com/webita/blender-codex-mcp)

## Why MCP For Blender

Blender automation usually starts with Python scripts. That works well, but an AI agent needs more than code execution.

It needs to know:

- what objects exist in the scene
- whether the camera is framed correctly
- whether the model is centered
- whether materials and lights are acceptable
- whether the exported file is ready for the web

With Blender Codex MCP, the workflow becomes iterative:

1. Codex inspects the scene.
2. Codex runs a small Blender Python change.
3. Codex captures a viewport screenshot.
4. The user checks the result.
5. Codex refines camera, lights, materials, or export settings.

This is useful for:

- product visualization
- technical 3D mockups
- architectural drafts
- web configurators
- `.glb` preparation
- repeatable Blender cleanup tasks

## What Is MCP

MCP, the Model Context Protocol, is an open standard for connecting AI applications to external tools, systems, data sources, and workflows.

Official documentation:

[Model Context Protocol documentation](https://modelcontextprotocol.io/)

In this project, Blender is the external tool, and Codex talks to it through the MCP server.

## What Blender Codex MCP Provides

The server exposes practical tools such as:

- `get_scene_info`: inspect the current Blender scene
- `get_object_info`: inspect a specific object
- `get_viewport_screenshot`: capture a viewport screenshot
- `execute_blender_code`: run Python inside Blender
- `blender_health_check`: verify that the bridge is reachable
- `sync_camera_to_viewport`: copy the current viewport into the active camera
- `export_glb`: export the scene or selected objects as `.glb`

The goal is not to replace Blender. The goal is to make Blender controllable and inspectable from Codex.

## Requirements

You need:

- Blender installed locally
- Codex desktop or another MCP-compatible Codex runtime
- `uv`
- Python 3.10+
- this repository

`uv` is used to run the Python MCP server:

[uv documentation](https://docs.astral.sh/uv/)

## Installation

Clone the repository:

```bash
git clone https://github.com/webita/blender-codex-mcp.git
cd blender-codex-mcp
```

Install the Blender addon:

1. open Blender
2. go to `Edit > Preferences > Add-ons`
3. click `Install...`
4. select `addon.py` from this repository
5. enable `Interface: Blender Codex MCP`
6. in the 3D viewport, press `N`
7. open the `BlenderCodexMCP` tab
8. click `Connect to MCP server`

By default, Blender listens on:

```text
localhost:9876
```

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

Replace `/absolute/path/to/blender-codex-mcp` with your real local path.

Then restart Codex.

## First Test

With Blender open and the addon connected, ask Codex:

```text
Inspect the open Blender scene and take a viewport screenshot.
```

If the setup is correct, Codex should be able to read the scene and call the Blender MCP tools.

## Recommended Workflow

The best results come from small, visible steps.

Do not ask the agent to rebuild a complex Blender scene in one huge operation. Instead:

1. inspect the scene
2. make one change
3. capture a screenshot
4. refine the camera, scale, materials, or lights
5. export the result

Useful prompts:

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

## GLB Export And WordPress Embedding

For web publishing, `.glb` is usually the easiest 3D format to distribute.

A practical workflow:

1. prepare the model in Blender
2. center the geometry
3. keep materials lightweight
4. set camera and lights for preview
5. export `.glb`
6. upload the file to WordPress
7. display it with a WebGL viewer

For WordPress and Elementor, `<model-viewer>` is a convenient option:

[model-viewer documentation](https://modelviewer.dev/)

Example:

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

The repository also includes a dedicated WordPress guide:

[WordPress embed guide](https://github.com/webita/blender-codex-mcp/blob/main/docs/WORDPRESS_EMBED.md)

## What About A Codex Plugin

It is natural to ask whether this can be installed as a one-click Codex plugin.

At the moment, there is no public third-party Codex plugin marketplace. The reliable public installation path is:

1. GitHub repository
2. Blender addon
3. manual MCP configuration in Codex

This repository includes an experimental local Codex plugin scaffold, but it should be treated as future-facing packaging rather than the main install path.

In short:

- MCP server: the working engine
- Blender addon: the bridge inside Blender
- plugin scaffold: local/future packaging support

## Safety Notes

The `execute_blender_code` tool can run Python inside Blender.

That is powerful, but it should be used carefully:

- save your `.blend` file before large operations
- work incrementally
- verify with screenshots
- only run code from sources you trust

## References

- Blender Codex MCP repository: [https://github.com/webita/blender-codex-mcp](https://github.com/webita/blender-codex-mcp)
- Model Context Protocol: [https://modelcontextprotocol.io/](https://modelcontextprotocol.io/)
- Blender Python API: [https://docs.blender.org/api/](https://docs.blender.org/api/)
- uv documentation: [https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)
- model-viewer: [https://modelviewer.dev/](https://modelviewer.dev/)

## Conclusion

Blender Codex MCP is useful because it gives Codex a practical feedback loop inside Blender.

The important part is not only code generation. It is the cycle:

```text
Codex edits -> Blender shows -> Codex verifies -> user guides -> export
```

For product models, technical scenes, web configurators, and GLB publishing, that loop is where the workflow becomes genuinely useful.

Repository:

[https://github.com/webita/blender-codex-mcp](https://github.com/webita/blender-codex-mcp)
