# Blender Scripting Rules

When generating Blender Python for this project, especially Geometry Nodes scripts:

- First query the running Blender version with `bpy.app.version_string` or `bpy.app.version`.
- For Geometry Nodes, introspect the actual node classes and socket names/identifiers in the running Blender before building non-trivial node trees. Prefer `socket.identifier` or verified socket names over guessed indices.
- When unsure about a Blender API, consult the official docs for the detected Blender version before writing the script.
- After executing a node-generation script, immediately validate the resulting node tree by listing nodes, sockets, and links, and by evaluating the depsgraph when geometry should be produced.
- When promoting an existing node socket value to a Group Input or reusable node group interface, first read and preserve the current `default_value` from the original socket, create/link the interface socket, then assign that captured value as the Group Input/default. Never assume zero, identity rotation, unit scale, or other defaults when converting an already-tuned node setup.
- For reusable Geometry Nodes groups with viewport gizmos, keep the gizmo nodes inside the reusable group and propagate their `Transform` geometry through the group's geometry output. Do not duplicate equivalent gizmos in the parent/wrapper node tree.
- Initialize local direction/vector helper nodes explicitly, for example a radial X-axis vector must be `(1, 0, 0)`, not the node's zero-vector fallback.
- When a Linear Gizmo edits a local-space value that is displayed after a transform/scale, keep the public group input in local units for correct falloff semantics, but feed the gizmo `Value` with the corresponding viewport-space value (for example `local_radius * transformed_axis_scale`) and use a normalized direction for the drag handle.
- Reusable Geometry Nodes groups should usually have `Geometry` input/output sockets, even when they also expose field outputs. This lets the same group work as a sub-node, as a full modifier, or as a pass-through processing block in a larger graph.
- For reusable falloff/mask groups, expose the computed field both as a socket output and as an optional named attribute write. Prefer controls like `Store Attribute` and `Attribute Name` with a sensible default such as `falloff`, using `Store Named Attribute` on the passed-through geometry.
- When the source geometry is still instances, do not assume a named attribute stored before `Realize Instances` will survive onto the final mesh. If a later modifier needs to read that attribute on realized points, run the reusable falloff group again after `Realize Instances` with gizmos off, or otherwise store the attribute after realization.
- For organic/noisy falloff edges, perturb the normalized distance before the final `Map Range` rather than randomizing the final mask directly. A good default pattern is `distance_normalized + ((noise(Position) - 0.5) * 2 * Noise Amount)`, with `Noise Amount` defaulting to `0` so existing setups remain unchanged, plus exposed `Noise Scale`, `Noise Detail`, `Noise Roughness`, and `Noise Seed` controls.
- Do not split a scalar falloff into X/Y/Z just to drive uniform scale. Connect the `0..1` float directly to vector scale sockets such as `Scale Instances.Scale`; Blender will use the scalar uniformly.
- Do not add explanatory viewport objects, labels, helper meshes, or text unless the user asks for visual annotations. Temporary helper geometry should be hidden or avoided.
- Keep MCP scripts idempotent: remove or reuse only objects/node groups created by the previous run, and do not touch unrelated scene content.
