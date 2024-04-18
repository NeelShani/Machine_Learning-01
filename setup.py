from setuptools import find_packages,setup
from typing import List


HYPER_E_DOT= '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requiremnts
    '''
    requirements = []
    with open(file_path) as file_obj:
        for line in file_obj:
            requirement = line.strip()
            if requirement != HYPER_E_DOT:
                requirements.append(requirement)
    return requirements

setup(
name= 'Machine_Learning-01',
version= '0.1.0',
author='Neel',
author_email='neeljshani@gmail.com',
packages= find_packages(),
install_requires=get_requirements('requirements.txt')
)