import bpy
from bpy.props import StringProperty
from bpy.types import AddonPreferences


class FBXBundlePreferences(AddonPreferences):
    bl_idname = __package__

    unity_assets_path: StringProperty(
        name="Unity Assets Path",
        description="Path to your Unity project's Assets folder",
        subtype="DIR_PATH",
        default="",
    )

    def draw(self, context):
        layout = self.layout

        box = layout.box()
        box.label(text="Unity Quick Export", icon="EXPORT")
        box.prop(self, "unity_assets_path")
        box.label(
            text="Configure per-scene settings in the 3D Viewport N-Panel", icon="INFO"
        )


def get_preferences():
    """Get the addon preferences instance."""
    return bpy.context.preferences.addons[__package__].preferences


def register():
    bpy.utils.register_class(FBXBundlePreferences)


def unregister():
    bpy.utils.unregister_class(FBXBundlePreferences)
