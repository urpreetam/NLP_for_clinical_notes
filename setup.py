from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        rquirements= file_obj.readlines()
        rquirements = [req.replace("\n","") for req in rquirements]

        return requirements


setup(
    name='NLP_for_clinical_notes',
    version='0.0.1',
    author='Prabhu Preetam Das',
    install_requires=get_requirements('requirements.txt')
)