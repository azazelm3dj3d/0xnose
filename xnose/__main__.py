import sys

from xnose.core import run_exit

if sys.argv[0].endswith('__main__.py'):
    sys.argv[0] = '%s -m xnose' % sys.executable

run_exit()
