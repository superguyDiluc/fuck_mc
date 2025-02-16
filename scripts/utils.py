import os

def get_project_root():
    """
    Get the root directory of the project
    @return
    project_root: str
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    while current_dir != os.path.dirname(current_dir):
        if os.path.exists(os.path.join(current_dir, '.git')) or os.path.exists(os.path.join(current_dir, 'setup.py')):
            return current_dir
        current_dir = os.path.dirname(current_dir)
    return current_dir

def complete_path(filename):
    """
    Get the absolute path to the files in the project root directory
    @params
    filename: str
    @return
    absolute_path: str
    """
    project_root = get_project_root()
    return os.path.join(project_root, filename)