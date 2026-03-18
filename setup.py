from setuptools import find_packages, setup
from typing import List

def get_requirements()-> List[str]:
    """
    This function will return the list of requirements mentioned in requirements.txt file
    """

    requirement_lst: List[str]=[]

    try:
        with open('requirements.txt', 'r') as file:
            # REad lines from the file
            lines=file.readlines()
            ## Rrocess each line
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found. Please make sure it exists in the same directory as setup.py")

    return requirement_lst


setup(
    name='NetworkSecurity',
    version='0.0.1',
    author="Ankit Sharma",
    author_email="ankit302290@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)