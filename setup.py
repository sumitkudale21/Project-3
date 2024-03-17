from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    '''
    this function will return a list of requirements
    '''
    
    HYPE_E_DOTE = '-e .'
    requirements = []
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        
        
        if HYPE_E_DOTE in requirements:
            requirements.remove(HYPE_E_DOTE)
    return requirements
        


setup(
    name='banglore_home_prices',
    version='0.0.1',
    packages=find_packages(),
    author='sumitkudale21',
    author_email='sumitkudale3545@gmail.com',
    install_requires=get_requirements('requirements.txt'),
)