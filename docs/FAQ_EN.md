# Article FAQ - Blender Codex MCP

## What is Blender Codex MCP?

Blender Codex MCP is an open source project that connects Codex to Blender through the Model Context Protocol. It lets Codex inspect a Blender scene, execute Python code, capture viewport screenshots, and prepare models for web export formats such as `.glb`.

## Does Blender need to stay open?

Yes. Blender must stay open because the MCP server communicates with an addon running inside Blender. If Blender is closed, Codex can no longer inspect or modify the scene.

## Do I need to install a Blender addon?

Yes. The project includes an `addon.py` file that you install in Blender through `Edit > Preferences > Add-ons > Install`. Once enabled, the addon opens a local bridge on `localhost:9876`.

## What is MCP?

MCP stands for Model Context Protocol. It is a standard that lets AI applications connect to external tools, data sources, and workflows. In this project, MCP is used to connect Codex to Blender.

## Can I install it as a one-click Codex plugin?

Not at the moment. There is currently no public official marketplace for third-party Codex plugins. The recommended way to use this project today is to clone the GitHub repository, install the Blender addon, and configure the MCP server in Codex.

## Why does the repo include a Codex plugin scaffold?

The plugin scaffold is included as an experimental foundation for future or local plugin workflows. The working engine is still the MCP server; the scaffold shows how the project could be packaged later as plugin support becomes more open.

## Can Codex really see what happens inside Blender?

Codex can inspect scene data and capture viewport screenshots through the MCP tools. This creates a much better feedback loop: edit, screenshot, verify, and refine.

## Can I export models for the web?

Yes. The project includes an `export_glb` tool and documentation for exporting `.glb` models that can be embedded in WordPress or displayed with WebGL viewers such as `<model-viewer>`.

## Does it work with Elementor or WordPress?

Yes. After exporting the `.glb` file, you can upload it to WordPress and display it in Elementor with an HTML widget using `<model-viewer>`.

## Is it safe to execute Blender Python from Codex?

It is powerful, but it should be used carefully. The `execute_blender_code` tool can run Python code inside Blender, so you should save your `.blend` file before major changes and work in small, verifiable steps.

## Can I use it for 3D configurators or product models?

Yes. This is one of the most useful applications: technical models, product scenes, web configurators, `.glb` export, and repeatable 3D automation workflows.

## Can Webita help integrate AI and automation into my website?

Yes. Webita works on AI consulting, operational automations, website integrations, chatbots, custom workflows, and tools connected to business websites. You can start from [Webita AI](https://webita.eu/en/webita-ai).

