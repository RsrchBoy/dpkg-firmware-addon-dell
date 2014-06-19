
import os

def mkselfrelpath(*args):
    return os.path.normpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), *args))

__VERSION__="2.2.9"
PKGLIBEXECDIR="/usr/local/libexec/firmware-addon-dell"
