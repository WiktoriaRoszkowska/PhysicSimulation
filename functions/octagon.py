import bpy 
#array of 4 points at the bottom of the cube 
def crt_octagon():
    verts = [

        (5.0, 2.0, -1.0),
        (2.0, 5.0, -1.0),
        (-2.0, 5.0, -1.0),
        (-5.0, 2.0, -1.0),
        (-5.0, -2.0, -1.0),
        (-2.0, -5.0, -1.0),
        (2.0, -5.0, -1.0),
        (5.0, -2.0, -1.0),
        
        (5.0, 2.0, 0.0),
        (2.0, 5.0, 0.0),
        (-2.0, 5.0, 0.0),
        (-5.0, 2.0, 0.0),
        (-5.0, -2.0, 0.0),
        (-2.0, -5.0, 0.0),
        (2.0, -5.0, 0.0),
        (5.0, -2.0, 0.0)
        
    ]
    faces = [
        (0, 1, 2, 3, 4, 5, 6, 7),
        (8, 9, 10, 11, 12, 13, 14, 15),
        (0, 8, 9, 1),
        (1, 9, 10, 2),
        (2,10,11,3),
        (3,11, 12, 4),
        (4, 12, 13, 5),
        (5, 13, 14, 6),
        (6, 14, 15, 7),
        (7, 15, 8, 0),
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