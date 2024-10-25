from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e.'

def get_requirements(file_path:str)->List[str]:
    requirements=[] #emptylist
    with open(file_path) as file_obj: # opening that particular file
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements] #replacing the \n with empty
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements



setup(
    name='Fault_Detection',
    version='0.0.1',
    author="Srashti",
    author_email="srashtishukla1111@gmail.com",
    install_requirements=get_requirements('requirements.txt'),
    packages=find_packages()
)