import ij.IJ 

IJ.run("Configure ilastik executable location", "executablefile=/opt/ilastik/run_ilastik.sh numthreads=-1 maxrammb=4096");

IJ.run("StarDist3D setup...", "stardistenvdirectory=/opt/conda/envs/stardist envtype=conda");

IJ.run("Set and Check Wrappers", "elastixexecutable=/opt/elastix/bin/elastix transformixexecutable=/opt/elastix/bin/transformix");