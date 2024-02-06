# core dependencies
import time
from abba_python.abba import add_brainglobe_atlases
# in order to wait for a jvm shutdown
import jpype
import imagej

import os

# THIS FILE SETS MANY PATHS EXPLICITLY WHEN ABBA IS INSTALLED FROM THE INSTALLER!
# IF YOU WANT TO RUN ABBA FROM PYTHON, TRY run-abba.py first!

# In ABBA PYthon, Fiji.app is in the parent directory of this script
ij = imagej.init("/opt/Fiji.app/", mode="interactive")

add_brainglobe_atlases(ij)

# For importing java classes, do not put this import sooner
# or it will cause issue !!!
from scyjava import jimport 
from jpype.types import JString

File = jimport('java.io.File')

# Sets DeepSlice env path - hopefully it's a common location for all OSes
deepslice_env_path = str('/opt/conda/envs/deepslice/')
deepslice_version = JString(str('1.1.5'))

DeepSlice = jimport('ch.epfl.biop.wrappers.deepslice.DeepSlice')
DeepSlice.setEnvDirPath(File(deepslice_env_path))
DeepSlice.setVersion(deepslice_version)

# Elastix and transformix location,
Elastix = jimport('ch.epfl.biop.wrappers.elastix.Elastix')
Transformix = jimport('ch.epfl.biop.wrappers.transformix.Transformix')

elastixPath = str(os.path.join('/opt/elastix/bin', 'elastix'))
transformixPath = str(os.path.join('/opt/elastix/bin', 'transformix'))

Elastix.exePath = JString(str(elastixPath))
Elastix.setExePath(File(JString(str(elastixPath))))
Transformix.exePath = JString(str(transformixPath))
Transformix.setExePath(File(JString(str(transformixPath))))

# Atlas
AtlasLocationHelper = jimport('ch.epfl.biop.atlas.AtlasLocationHelper')
atlas_dir = os.path.join('/opt/abba/', 'cached_atlas')
os.makedirs(atlas_dir, exist_ok=True)
atlasPath = str(atlas_dir)

AtlasLocationHelper.defaultCacheDir = File(JString(atlasPath))

# Show the UI
ij.ui().showUI()

 # Wait for the JVM to shut down
while jpype.isJVMStarted():
    time.sleep(1)

print("JVM has shut down")