import bpy

#create paramets
cube_count = 10
frame_count = 300
location_offset = 3
fps = 30
#set the end frame
bpy.context.scene.frame_current = frame_count

#set tghe fps
bpy.context.scene.render.fps = fps

#create the row of cube along the y-axis
for i in range(cube_count):
    bpy.ops.mesh.primitive_cube_add(size=2, location=(0, i* location_offset, 0))

#create empty for tracking
bpy.ops.object.empty_add()
empty = bpy.context.active_object

#aniamte the location property of the emopty
empty.keyframe_insert("location", frame = 1)
empty.location.y = location_offset * cube_count
empty.keyframe_insert("location", frame = frame_count)

#add camera into the scene
bpy.ops.object.camera_add()
camera = bpy.context.active_object
camera.location.x = 15
camera.location.y = location_offset * cube_count /2
camera.location.z = 2


#add a constraint to track the empty
bpy.ops.object.constraint_add(type='TRACK_TO')
bpy.context.object.constraints["Track To"].target = empty
