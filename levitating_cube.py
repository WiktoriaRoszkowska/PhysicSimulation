import bpy
#add cube to 0,0,0
bpy.ops.mesh.primitive_cube_add()

#get a reference to the currently active object
cube = bpy.context.active_object

#insert keyframe at frame one
start_frame = 0
#cube.keyframe_insert("location", frame = start_frame)

#change the location of the cube on the z-axis
#cube.location.z = 5

#insert keyframe at last frame
last_frame =250
#cube.keyframe_insert("location", frame = last_frame)

#levitating cube loop:
while start_frame < last_frame:
    if start_frame % 40 == 0:
        cube.location.z = 5
    else:
        cube.location.z = -5
        
    cube.keyframe_insert("location", frame = start_frame)
    start_frame +=20

