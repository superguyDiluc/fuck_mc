import os

def complete_path(filename):
    """
    Get the absolute path to the files in the project
    @params
    filename: str
    @return
    absolute_path: str
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)