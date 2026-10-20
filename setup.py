
""" 
The setup.py is basically an essential part of  packaging and the distributing the Python projects. 
It is used by the set up tools to define the configuration of your project such as the metadata, 
dependencies and many more. 

""" 

from setuptools import find_packages, setup 
from typing import List  

def get_requirements()-> List[str]: 

    """ 
    This function will return the list of requirements 
    
    """ 
    requirement_lst: List[str] = []  
    try: 
        with open('requiremets.txt', 'r') as file: 
            lines = file.readlines() 
            for line in lines: 
                requirements = line.strip() 
                if requirement and requirement!= '-e .': 
                    requirement_lst.append(requirement) 

    except FileNotFoundError: 
        print("requirements.txt file not found") 

    return requirement_lst 

setup(
    name = "NetworkSecurity", 
    version = "0.0.1", 
    author = "Chaitanya Mangla", 
    author_email="krishnaik06@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements() 
)