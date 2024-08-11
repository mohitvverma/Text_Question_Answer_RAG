import os
from pathlib import Path

os.chdir('../')
PARENT_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
print('Parent Dir :', PARENT_DIR_PATH)

MAIN_FILE_PATH = project_path = Path(__file__).parent.parent
print('Project folder path: :', MAIN_FILE_PATH)
