import bpy 
#array of 4 points at the bottom of the cube 
verts = [

    (4.0, 0.0, -1.0),
    (2.0, 3.5, -1.0),
    (-2.0, 3.5, -1.0),
    (-4.0, 0.0, -1.0),
    (-2.0, -3.5, -1.0),
    (2.0, -3.5, -1.0),
    
    (4.0, 0.0, 0.0),
    (2.0, 3.5, 0.0),
    (-2.0, 3.5, 0.0),
    (-4.0, 0.0, 0.0),
    (-2.0, -3.5, 0.0),
    (2.0, -3.5, 0.0),
    
    
    
]
faces = [
    (0, 1, 2, 3, 4, 5),
    (6, 7, 8, 9, 10, 11),
    (0, 6, 7, 1),
    (1, 7, 8, 2),
    (2, 8, 9, 3),
    (3, 9, 10, 4),
    (4, 10, 11, 5),
    (5, 11, 6, 0),
]
edges = [] 
#
mesh_data = bpy.data.meshes.new("cube data")
#
mesh_data.from_pydata(verts, edges, faces)

#creating new object drom mesh_data
octagon = bpy.data.objects.new("cube data", mesh_data)

#add the mesh_obj to scene collection
bpy.context.collection.objects.link(octagon)