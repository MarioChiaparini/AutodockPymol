from vina import Vina 
v = Vina(sf_name='vina')
ligand_files = ['../Desktop/ligand-5kir.pdbqt']
v.set_receptor("../Desktop/5kdir.pdbqt")
v.set_ligand_from_file(ligand_files)
v.compute_vina_maps()
v.dock(exhaustiveness=32, n_poses=20)
file_name = files.split('.')[0]
v.write_pose(file_name+"-resuts.pbqt")
  
