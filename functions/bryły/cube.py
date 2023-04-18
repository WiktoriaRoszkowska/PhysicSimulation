import bpy
#array of 4 points at the bottom of the cube 
verts = [
    (-1.0, -1.0, -1.0),
    (-1.0, 1.0, -1.0),
    (1.0, 1.0, -1.0),
    (1.0, -1.0, -1.0),
    
    (-1.0, -1.0, 1.0),
    (-1.0, 1.0, 1.0),
    (1.0, 1.0, 1.0),
    (1.0, -1.0, 1.0)
    
]
faces = [
    (0, 1, 2, 3),
    (7, 6, 5, 4),
    (4, 5, 1, 0),
    (7, 4, 0, 3),
    (6, 7, 3, 2),
    (5, 6, 2, 1),
]
edges = [] 
#
mesh_data = bpy.data.meshes.new("cube data")
#
mesh_data.from_pydata(verts, edges, faces)

#creating new object drom mesh_data
mesh_obj = bpy.data.objects.new("cube data", mesh_data)

#add the mesh_obj to scene collection
bpy.context.collection.objects.link(mesh_obj)
