#!e:\projects\django-python-project\btre_project\lakshenv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pip==20.3.3','console_scripts','pip3'
__requires__ = 'pip==20.3.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pip==20.3.3', 'console_scripts', 'pip3')()
    )
