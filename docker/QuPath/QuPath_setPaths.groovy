def targetStream = new FileInputStream( new File ( "/home/biop/tmp/qp_prefs.xml" ) )
println targetStream
PathPrefs.importPreferences( targetStream )

import qupath.lib.gui.prefs.PathPrefs