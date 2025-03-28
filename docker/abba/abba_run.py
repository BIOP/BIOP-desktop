import os
import platform
import time

from abba_python import abba

import jpype  # in order to wait for a jvm shutdown
import imagej

# THIS FILE SETS MANY PATHS EXPLICITLY WHEN ABBA IS INSTALLED FROM THE INSTALLER

if __name__ == '__main__':
    directory_on_launch = os.path.dirname(os.getcwd())
    import scyjava

    # scyjava.config.add_option('-XX:+UseZGC') # Use ZGC
    scyjava.config.add_option('-Xmx8g') # 5 Gb

    # You can swap the lines below if you want to use a  Fiji instead of the maven downloaded one
    ij = imagej.init("/opt/Fiji.app/", mode="interactive")

    print('ImageJ/Fiji successfully initialized.')

    # Makes BrainGlobe atlases discoverable by ABBA in Fiji
    from abba_python.abba import add_brainglobe_atlases
    add_brainglobe_atlases(ij)

    from scyjava import jimport  # For importing java classes, do not put this import sooner

    from jpype.types import JString

    DebugTools = jimport('loci.common.DebugTools')
    # DebugTools.enableLogging('OFF') # less logging
    DebugTools.enableLogging("INFO")
    # DebugTools.enableLogging("DEBUG"); # more logging
    python_info = 'ABBA Python (BIOP-desktop) v0.10.6'
    ABBAForumHelpCommand = jimport('ch.epfl.biop.atlas.aligner.command.ABBAForumHelpCommand')
    ABBAForumHelpCommand.pythonInformation = JString(python_info)

    File = jimport('java.io.File')
    # Sets DeepSlice env path - hopefully it's a common location for all OSes
    deepslice_env_path = str('/opt/conda/envs/deepslice/')
    deepslice_version = JString(str('1.1.5.1'))
    DeepSlice = jimport('ch.epfl.biop.wrappers.deepslice.DeepSlice')
    DeepSlice.setEnvDirPath(File(deepslice_env_path))
    DeepSlice.setVersion(deepslice_version)  # not autodetected. Do not matter for 1.1.5, but may matter later

    # For setting elastix and transformix location, OS dependent
    # File ch.epfl.biop.wrappers.elastix.Elastix exePath
    # File ch.epfl.biop.wrappers.transformix.Transformix exePath
    Elastix = jimport('ch.epfl.biop.wrappers.elastix.Elastix')
    Transformix = jimport('ch.epfl.biop.wrappers.transformix.Transformix')

    # For setting the atlas cache folder, OS dependent, we want this property to be system-wide
    AtlasLocationHelper = jimport('ch.epfl.biop.atlas.AtlasLocationHelper')

    # Conda
    #Conda = jimport('ch.epfl.biop.wrappers.Conda')
    #condaPath = str(os.path.join(directory_on_launch, 'condabin', 'conda.bat'))
    #Conda.windowsCondaCommand = JString(str(condaPath))  # Sets the conda path

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

    ij.ui().showUI()  # will showing the UI at the end fix Mac threading issues ?

    # Wait for the JVM to shut down
    while jpype.isJVMStarted():
        time.sleep(1)

    print("JVM has shut down")