import json
import os

def read_json(file_path: str) -> dict:
    """
        This function parses JSON data retrieved from the designated file path and returns the resulting dictionary. 
        To guarantee cross-compatibility across various operating systems, 
        make use of os.path.join() before passing the file path when this method is called. 
    """

    with open(file_path, 'r') as file:
        return json.load(file)


def get_image_path(image_name: str) -> str:
    """
        Returns the file or image path which is saved within the images directory inside data folder.
    """

    image_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'images', image_name)
    return image_path