from setuptools import setup,find_packages
from typing import List

def get_requirements(filepath:str)->List[str]:
    "returns list of requirements"
    HYPEN_E_DOT =   "-e ."
    
    reuirements=[]
    with open(filepath) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n","")  for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name="InsightIQ-Turn your Documents into Smart Interview Questions",
    version="1.0.0",
    author="Rahul Rajan",
    author_email="rahuldatascienceprac@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)