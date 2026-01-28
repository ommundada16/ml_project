from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ." # Define this at the top

def get_requirements(file_path:str)->List[str]: # Change 'req' to 'get_requirements'
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[r.replace("\n","") for r in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'om',
    author_email = 'your@email.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt') # This calls the function above
)