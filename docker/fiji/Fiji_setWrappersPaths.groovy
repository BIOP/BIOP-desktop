import ij.IJ 

IJ.run("Configure ilastik executable location", "executablefile=/opt/ilastik/run_ilastik.sh numthreads=-1 maxrammb=4096");

IJ.run("StarDist3D setup...", "stardistenvdirectory=/opt/conda/envs/stardist envtype=conda");

IJ.run("Cellpose setup...", "cellposeenvdirectory=/opt/conda/envs/cellpose envtype=conda usegpu=true usemxnet=false usefastmode=false useresample=false version=2.0");

IJ.run("Set and Check Wrappers", "elastixexecutable=/opt/elastix/bin/elastix transformixexecutable=/opt/elastix/bin/transformix");