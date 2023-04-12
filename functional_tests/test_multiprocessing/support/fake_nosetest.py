import os
import sys

import xnose
from xnose.plugins.multiprocess import MultiProcess
from xnose.config import Config
from xnose.plugins.manager import PluginManager

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("USAGE: %s TEST_FILE LOG_FILE KILL_FILE" % sys.argv[0])
        sys.exit(1)
    os.environ['NOSE_MP_LOG']=sys.argv[2]
    os.environ['NOSE_MP_KILL']=sys.argv[3]
    xnose.main(
            defaultTest=sys.argv[1], argv=[sys.argv[0],'--processes=1','-v'],
            config=Config(plugins=PluginManager(plugins=[MultiProcess()])))
