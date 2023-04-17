import bpy
#plane properties
bpy.ops.mesh.primitive_plane_add(size=2, location=(0, 0, 0))
bpy.ops.transform.resize(value=(86.9201, 86.9201, 86.9201), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False)
bpy.ops.transform.translate(value=(-0, -0, -29.066), orient_axis_ortho='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
bpy.ops.rigidbody.object_add()
bpy.context.object.rigid_body.type = 'PASSIVE'
bpy.context.object.rigid_body.collision_shape = 'BOX'

#creating 'num' cubes in x,y,z
num = 5
counter = 0
for a in range(0, num+15):
    counter +=2
    counter2 = 0
    for y in range(0, num):
        counter2 +=2
        counter3 = 0
        for z in range(0, num):
            #cube properties
            bpy.ops.mesh.primitive_cube_add(size=2, location=(counter3, counter2, counter))
            counter3 +=2
            bpy.ops.rigidbody.object_add()
            bpy.context.object.rigid_body.mass = 20
            bpy.context.object.rigid_body.collision_shape = 'BOX'
            bpy.context.object.rigid_body.friction = 1
            bpy.context.object.rigid_body.use_margin = True
            bpy.context.object.rigid_body.collision_margin = 0.00
            bpy.context.object.rigid_body.linear_damping = 0.35
            bpy.context.object.rigid_body.linear_damping = 0.35






