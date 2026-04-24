# Export And Embed A Blender Scene In WordPress

This is the simplest practical workflow if you want to publish a 3D model created with Blender Codex MCP on a WordPress site.

## Recommended Format

Use `.glb`.

Why:

- single file
- compact
- widely supported by web 3D viewers
- easier to upload and move than `.gltf + bin + textures`

## Export From Blender

In Blender:

1. Select the objects you want to publish.
2. Go to `File > Export > glTF 2.0`.
3. Choose `Format: glTF Binary (.glb)`.
4. If needed, enable `Selected Objects`.
5. Export.

Recommended export settings for the web:

- format: `.glb`
- apply modifiers: on
- include only the objects you need
- use reasonably simple materials
- keep texture sizes under control

## Keep The Model Web-Friendly

Before export:

- remove hidden junk
- keep polycount reasonable
- use simple PBR materials
- avoid unnecessary tiny geometry
- keep object names clean
- place origin logically if the viewer supports interaction

## WordPress Embed Options

There are two solid approaches.

### Option 1: Use A 3D Viewer Plugin

Best if you want a low-code workflow.

Typical flow:

1. Upload the `.glb`
2. Use a WordPress plugin that supports `.glb` or glTF display
3. Insert the model block/shortcode into a page

Good for:

- product pages
- simple interactive previews
- clients who want a WordPress-native workflow

### Option 2: Use A Custom HTML Block With `<model-viewer>`

Best if you want more control and a cleaner frontend.

Typical flow:

1. Upload the `.glb` to WordPress media or your CDN
2. Add a custom HTML block
3. Embed a viewer component that loads the `.glb`

Minimal example:

```html
<script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>

<model-viewer
  src="https://example.com/wp-content/uploads/2026/04/model.glb"
  camera-controls
  auto-rotate
  shadow-intensity="1"
  exposure="1"
  style="width:100%;height:520px;background:#f5f7f8;"
></model-viewer>
```

Good for:

- more polished websites
- custom layouts
- better control over background, dimensions, and interaction

## Background: Keep It Outside The GLB

Usually do not bake a green or custom background into the exported model.

Better approach:

- keep the `.glb` clean
- set background color in the viewer or on the page

Why:

- easier restyling later
- cleaner reuse in different pages
- better portability to other viewers

## Suggested WordPress Setup

For most cases:

1. export `.glb`
2. upload it
3. use a viewer with a neutral page background
4. set a fixed aspect ratio section on the page

For example:

- desktop height around `520px` to `700px`
- mobile height around `360px` to `520px`
- light neutral background

## If The Model Looks Wrong On The Site

Check:

- scale
- camera default
- whether materials exported correctly
- whether normals are correct
- whether the viewer is applying its own environment or tone mapping

## Recommended Final Flow

1. Build or refine the model in Blender
2. Verify the default camera
3. Export `.glb`
4. Test in a browser viewer
5. Embed in WordPress
6. Adjust page background and container size on the site side, not inside the model
