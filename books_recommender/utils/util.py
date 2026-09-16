import yaml # this is PyYAML, the library that actually parses .yaml syntax into Python dicts/lists.
import sys # passed into AppException so it can grab sys.exc_info() internally and extract the exact
            # file name + line number where the error occurred
from books_recommender.exception.exception_handler import AppException



def read_yaml_file(file_path:str)->dict:
    """
    Reads a YAML file and returns the contents as a dictionary.
    file_path: str
    """
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
        # yaml.safe_load(yaml_file) — parses the YAML content into a Python
        # dict.safe_load(vs.plain load) is used deliberately — it only parses standard
        # YAML tags and won't execute arbitrary Python objects embedded in the file,
    except Exception as e:
        raise AppException(e,sys) # from e if anything goes wrong (file not found, malformed YAML, permissions issue),
         # it doesn't crash with a raw Python traceback. Instead it wraps the error in your custom AppException

# Role of utils/util.py in general
# Think of utils/ as your toolbox of small, generic, reusable helper functions that don't belong to any single pipeline stage but get used across multiple stages. The defining traits:
# Stateless and generic
# Used by more than one place
# Keeps stage files focused on business logic
