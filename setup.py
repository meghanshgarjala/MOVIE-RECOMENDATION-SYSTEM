from setuptools import find_packages,setup
from typing import List
hypen_e_dot='-e.'

def requirements(filepath:str)->List[str]:
    requirements=[]
    with open(filepath) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]
        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
        
    return requirements

setup(
    name='MOVIE RECOMENDATION SYSTEM',
    version=1.0,
    author='G.MEGHANSH RAO',
    install_requires=requirements('requirements.txt'),
    packages=find_packages()
)
