import bpy

from . mark_op import UEMark_OT_Operator
from . unmark_op import UEUnmark_OT_Operator
from . unity_export import UEExport2Unity_OT_Operator

class UEHelper_PT_Panel(bpy.types.Panel):
    bl_idname = "uehelper.main_panel"
    bl_label = "UE Helper"
    bl_category = "Unreal Engine"
    bl_space_type = "VIEW_3D"   
    bl_region_type = "UI"
    bl_context = "objectmode"
    #bl_parent_id = "BFU_PT_BlenderForUnrealTool"  

    
    def draw(self, context):
        layout = self.layout
        obj = context.object
        scene = context.scene
        
      
        col = layout.column(align=True)
        col.operator(UEMark_OT_Operator.bl_idname, text="Mark selected for export", icon="CONSOLE")
        col.operator(UEUnmark_OT_Operator.bl_idname, text="Unmark selected for export", icon="CONSOLE")

        layout.separator()
        layout.label(text="Options:")
        layout.prop(scene, "ue_helper_rotate_z_setting")

        layout.separator()

        box = layout.box()
        row = box.row()
        row.prop(obj, "expanded", icon="TRIA_DOWN" if obj.expanded else "TRIA_RIGHT", icon_only = True, emboss=False)
        row.label(text="Unity helpers:")
        if obj.expanded:
            box.label(text="Use with caution, very early stage of this one.\nShould work with simple static meshes.", icon="INFO")
            col = box.column(align=True)
            col.prop(scene, "ue_helper_unity_export_path" )
            col.separator()
            col.operator(UEExport2Unity_OT_Operator.bl_idname, text = "Export to Unity", icon="CONSOLE")