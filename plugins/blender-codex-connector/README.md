# Blender Codex Connector

This is a repo-local Codex plugin scaffold for `blender-codex-mcp`.

It does not replace the MCP server. It packages the same MCP server in a format that is easier to surface, install, and document inside Codex environments that support plugins.

The Blender addon writes a fresh local auth token automatically to `~/.blender-codex-mcp/auth.json` each time it connects, and the MCP server reads it from there. The same file is overwritten for new sessions and removed on disconnect. Advanced setups can override this with `BLENDER_AUTH_TOKEN_FILE` or `BLENDER_AUTH_TOKEN`.

## What It Does

- points Codex at the local `blender-codex-mcp` server
- keeps the default Blender bridge config on `localhost:9876`
- gives you a clean place for plugin metadata, screenshots, and future plugin-specific docs

## Current Status

This plugin is intentionally lightweight:

- MCP server lives at the repository root
- plugin metadata lives here
- `.mcp.json` points back to the root package with `uv`

Before public release, verify the public repository, privacy policy, and terms URLs in `.codex-plugin/plugin.json`.
