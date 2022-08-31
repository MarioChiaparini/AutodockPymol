from vina import Vina
from rdkit import Chem 
from vina import Vina 
from rdkit.Chem.rdMolTransforms import ComputeCentroid

v = Vina(sf_name='vina')

ligante = Chem.SDMolSupplier('/home/ABTLUS/mario.neto/Desktop/ligantes/ligante5kdir.sdf', removeHs=False)

centroid = ComputeCentroid(ligante.GetConformer())

v.set_receptor("/home/ABTLUS/mario.neto/Desktop/5kdir.pdbqt")

v.set_ligand_from_file(ligantes)

v.compute_vina_maps(center=[centroid.x, centroid.y, centroid.z], box_size=[20, 20, 20])

energy_minim = v.optimize()

v.dock(exhaustiveness=32, n_poses=20)

file_name = files.split('.')[0]

v.write_pose(file_name+"-resuts.pbqt")  
