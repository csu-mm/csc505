'''
Colorado State University Global
( https://csuglobal.edu/academic-programs/graduate-degrees/masters-science-degree-artificial-intelligence-machine-learning )
MS - Artificial Intelligence and Machine Learning
Course: CSC505 - Principles of Software Development
Module 4: Critical Thinking - design and python code
Professor: Dr. Bingdong Li
Created by Mukul Mondal
August 10, 2025
'''
#
'''
Problem statement:
Common Personality Traits

... Using your personal experience and observation of people who are excellent software developers, 
use a UML diagram of your choice to depict three personality traits that appear to be common among 
them. Write a Python Script that will print a brief description and names and number of the important 
steps in your program. Use OODesign.com's Builder Pattern, ...
'''

from os import system, name


# This is just a helper function to clear the screen
# This is not required, per problem statement.
def clearScreen():
    if name == 'nt':  # For windows system
        _ = system('cls')    
    else:             # for non-windows system
        _ = system('clear')
    return


# Product: Represents the complex object that is being built.
class SoftwareDeveloper:
    def __init__(self):
        self.curiosity = None
        self.attentionToDetail = None
        self.empathy = None
        self.teamPlayerLevel = None

    def __str__(self):
        return f"Curiosity: {self.curiosity}, \nAttentionToDetail: {self.attentionToDetail}, \nEmpathy: {self.empathy}, \nTeamPlayer: {self.teamPlayerLevel}"

# Builder Interface: This specifies an abstract interface for creating parts of a Product object.
class SoftwareDeveloperBuilder:
    def set_curiosity(self): pass
    def set_attentionToDetail(self): pass
    def set_empathy(self): pass
    def set_teamPlayerLevel(self): pass
    def get_softwaredeveloper(self): pass

# Concrete Builder: Constructs and puts together parts of the product by implementing the Builder interface. 
#                   Defines and keeps track of the representation.
#                   Creates and provides an interface for saving the product.
class ExcellentSoftwareDeveloperBuilder(SoftwareDeveloperBuilder):
    def __init__(self):
        self.softwareDeveloper = SoftwareDeveloper()

    def set_curiosity(self):
        self.softwareDeveloper.curiosity = """\n\tNaturally inquisitive.\n\tExplore new technologies.\n\tQuestion assumptions, and dig deep into how things work.\n\tExperiment with a new framework.\n\tContinuous learning."""

    def set_attentionToDetail(self):
        self.softwareDeveloper.attentionToDetail = """\n\tCan spot edge cases others miss.\n\tFollow naming convension.\n\tOptimize performance.\n\tCare about small stuff to improve quality.\n\tPrevent bugs.\n\tImprove maintainability.\n\tWrite code that lasts for longer time."""

    def set_empathy(self):
        self.softwareDeveloper.empathy = """\n\tThink about the user, the teammate, and the future maintainer of their code.\n\tWrite clear documentation, communicate thoughtfully.\n\tDesign APIs that feel intuitive.\n\tBetter collaborator and mentor.\n\tKnow that software is built by people, for people."""

    def set_teamPlayerLevel(self):
        self.softwareDeveloper.teamPlayerLevel = "\n\tExcellent"

    def get_softwaredeveloper(self):
        return self.softwareDeveloper


# Director: The Director class constructs the complex object using the Builder interface.
class ComplexObjCreator:
    def __init__(self, builder: SoftwareDeveloperBuilder):
        self.builder = builder

    def build_softwareDeveloper(self):
        self.builder.set_curiosity()
        self.builder.set_attentionToDetail()
        self.builder.set_empathy()
        self.builder.set_teamPlayerLevel()
        return self.builder.get_softwaredeveloper()


# Usage
def execute_module4_ct():    
    builder = ExcellentSoftwareDeveloperBuilder()
    complexObjCreator = ComplexObjCreator(builder)
    finalObj = complexObjCreator.build_softwareDeveloper()
    print(finalObj)
    return




if __name__ == "__main__":
    clearScreen()
    print("=== Module 4: Critical Thinking: Common Personality Traits ===")
    print("Properties of SoftwareDeveloper object Created by Builder Pattern for 'excellent software developer': ")
    execute_module4_ct()
