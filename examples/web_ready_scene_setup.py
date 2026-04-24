"""
Generic Blender scene helpers for web-ready exports.

This example is intentionally generic:
- apply simple base materials
- center visible geometry in the scene
- place the scene on Z=0
- create a clean default camera
- create basic studio lighting

Use it as a starting point through `execute_blender_code`, or adapt pieces into
your own Blender scripts.
"""

import math
import bpy
from mathutils import Vector


def mesh_like_objects():
    return [
        obj for obj in bpy.data.objects
        if obj.type in {"MESH", "CURVE", "SURFACE", "FONT"} and not obj.hide_get()
    ]


def object_world_corners(obj):
    return [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]


def compute_scene_bounds(objects):
    corners = []
    for obj in objects:
        corners.extend(object_world_corners(obj))
    if not corners:
        return None

    min_corner = Vector((
        min(v.x for v in corners),
        min(v.y for v in corners),
        min(v.z for v in corners),
    ))
    max_corner = Vector((
        max(v.x for v in corners),
        max(v.y for v in corners),
        max(v.z for v in corners),
    ))
    return min_corner, max_corner


def center_scene(objects):
    bounds = compute_scene_bounds(objects)
    if bounds is None:
        return

    min_corner, max_corner = bounds
    offset = Vector((
        -((min_corner.x + max_corner.x) / 2.0),
        -((min_corner.y + max_corner.y) / 2.0),
        -min_corner.z,
    ))

    for obj in bpy.data.objects:
        obj.location += offset


def ensure_material(name, color, roughness=0.5, metallic=0.0):
    mat = bpy.data.materials.get(name)
    if mat is None:
        mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links

    output = next((node for node in nodes if node.type == "OUTPUT_MATERIAL"), None)
    bsdf = next((node for node in nodes if node.type == "BSDF_PRINCIPLED"), None)

    if output is None:
        output = nodes.new(type="ShaderNodeOutputMaterial")
    if bsdf is None:
        bsdf = nodes.new(type="ShaderNodeBsdfPrincipled")
    if not bsdf.outputs["BSDF"].is_linked:
        links.new(bsdf.outputs["BSDF"], output.inputs["Surface"])

    bsdf.inputs["Base Color"].default_value = (*color, 1.0)
    bsdf.inputs["Roughness"].default_value = roughness
    bsdf.inputs["Metallic"].default_value = metallic
    return mat


def apply_default_materials(objects):
    dark = ensure_material("DefaultDark", (0.18, 0.19, 0.20), roughness=0.55)
    light = ensure_material("DefaultLight", (0.72, 0.74, 0.77), roughness=0.45)

    for obj in objects:
        material = dark if obj.type == "MESH" else light
        if obj.data and hasattr(obj.data, "materials"):
            if obj.data.materials:
                obj.data.materials[0] = material
            else:
                obj.data.materials.append(material)


def remove_existing_lights_and_cameras():
    bpy.ops.object.select_all(action="DESELECT")
    for obj in list(bpy.data.objects):
        if obj.type in {"LIGHT", "CAMERA"}:
            obj.select_set(True)
    bpy.ops.object.delete()


def setup_camera(bounds):
    min_corner, max_corner = bounds
    center = (min_corner + max_corner) / 2.0
    extent = max(max_corner.x - min_corner.x, max_corner.y - min_corner.y, max_corner.z - min_corner.z)

    bpy.ops.object.camera_add(location=(center.x + extent * 1.2, center.y - extent * 1.8, center.z + extent * 0.9))
    cam = bpy.context.active_object
    cam.name = "Camera"
    cam.rotation_euler = (math.radians(63), 0.0, math.radians(32))
    cam.data.lens = 50
    cam.data.clip_end = 1000
    bpy.context.scene.camera = cam
    return cam


def setup_lights(bounds):
    min_corner, max_corner = bounds
    center = (min_corner + max_corner) / 2.0
    extent = max(max_corner.x - min_corner.x, max_corner.y - min_corner.y, max_corner.z - min_corner.z)

    bpy.ops.object.light_add(type="SUN", location=(center.x, center.y, center.z + extent * 3.0))
    sun = bpy.context.active_object
    sun.name = "Sun"
    sun.data.energy = 2.0
    sun.rotation_euler = (math.radians(35), math.radians(8), math.radians(28))

    bpy.ops.object.light_add(type="AREA", location=(center.x + extent * 0.7, center.y - extent * 1.0, center.z + extent * 0.8))
    key = bpy.context.active_object
    key.name = "AreaKey"
    key.rotation_euler = (math.radians(70), 0.0, math.radians(38))
    key.data.energy = 3500
    key.data.shape = "RECTANGLE"
    key.data.size = extent * 0.9
    key.data.size_y = extent * 0.45

    bpy.ops.object.light_add(type="AREA", location=(center.x - extent * 0.6, center.y + extent * 0.8, center.z + extent * 0.45))
    fill = bpy.context.active_object
    fill.name = "AreaFill"
    fill.rotation_euler = (math.radians(95), 0.0, math.radians(-65))
    fill.data.energy = 1200
    fill.data.shape = "RECTANGLE"
    fill.data.size = extent * 0.6
    fill.data.size_y = extent * 0.3


def configure_scene():
    scene = bpy.context.scene
    scene.unit_settings.system = "METRIC"
    scene.unit_settings.scale_length = 1.0
    scene.render.engine = "BLENDER_EEVEE"
    if hasattr(scene, "eevee"):
        if hasattr(scene.eevee, "taa_render_samples"):
            scene.eevee.taa_render_samples = 32
        if hasattr(scene.eevee, "taa_samples"):
            scene.eevee.taa_samples = 16
    scene.world.color = (0.98, 0.98, 0.98)
    scene.render.film_transparent = False


def main():
    configure_scene()
    objects = mesh_like_objects()
    if not objects:
        print("No visible geometry found")
        return

    center_scene(objects)
    objects = mesh_like_objects()
    bounds = compute_scene_bounds(objects)
    if bounds is None:
        print("Failed to compute bounds")
        return

    apply_default_materials(objects)
    remove_existing_lights_and_cameras()
    setup_camera(bounds)
    setup_lights(bounds)

    print("web_ready_scene_setup_complete", len(objects))


main()
