# YouTube Demo Script

This outline is designed for a short practical video.

## Video Goal

Show that Codex can inspect and control a live Blender scene through a local MCP bridge.

Keep the promise simple:

- install the Blender addon
- configure Codex MCP
- connect to Blender
- inspect a scene
- make a small change
- take a viewport screenshot
- export a `.glb`

## Suggested Title

`Control Blender With Codex Using MCP`

Alternative:

`Blender + Codex MCP: Inspect, Edit, Screenshot, Export GLB`

## Short Description

`A practical demo of Blender Codex MCP: a local Blender addon plus MCP server that lets Codex inspect scenes, run Blender Python, capture viewport screenshots, and export GLB files.`

## Recording Flow

1. Open the GitHub repo.
2. Explain the architecture in one sentence:
   `Blender runs the addon, Codex runs the MCP server, and the two talk locally on port 9876.`
3. Install or show the installed Blender addon.
4. Click `Connect to MCP server` in Blender.
5. Show the Codex config snippet.
6. Restart or reopen Codex.
7. Ask Codex to inspect the Blender scene.
8. Ask Codex to capture a viewport screenshot.
9. Ask Codex to make one small visible change.
10. Ask Codex to export a `.glb`.
11. Show the WordPress/embed guide briefly.

## Demo Prompts

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

## What To Say Clearly

- Blender must be open.
- The Blender addon must be enabled.
- The local bridge defaults to `localhost:9876`.
- Codex must be configured to run the MCP server from this repo.
- There is no public third-party Codex plugin marketplace yet.
- The included plugin scaffold is experimental/future-facing.
- `execute_blender_code` can run Blender Python, so save your `.blend` before major operations.

## Suggested GitHub Topics

- `blender`
- `codex`
- `mcp`
- `model-context-protocol`
- `ai-tools`
- `python`
- `3d`
- `gltf`
- `glb`

## Pinned Comment

`Repo: https://github.com/webita/blender-codex-mcp`

`Install path today: GitHub repo + Blender addon + Codex MCP config. The plugin scaffold is included for future/local Codex plugin workflows.`
