kernels/ should be copy to /home/biop/.local/share/jupyter/kernels/
so the different conda env are available in notebooks

command to install a new kernel:


python -m ipykernel install --user --name myEnv --display-name "Python (myenv)"