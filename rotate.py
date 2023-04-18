import bpy
import math
#add cube 
bpy.ops.mesh.primitive_cube_add()

#add reference to the currently active object
cube = bpy.context.active_object

#insert a keyframe at frame one
start_frame = 1
cube.keyframe_insert("rotation_euler", frame = start_frame)

#change the rotation of cube around y-axis
degrees = 720
cube.rotation_euler.y = math.radians(degrees)

#insert a keyframe at last frame
last_frame = 250
cube.keyframe_insert("rotation_euler", frame = last_frame)

