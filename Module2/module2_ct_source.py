'''
Colorado State University Global
( https://csuglobal.edu/academic-programs/graduate-degrees/masters-science-degree-artificial-intelligence-machine-learning )
MS - Artificial Intelligence and Machine Learning
Course: CSC505 - Principles of Software Development
Module 2: Critical Thinking - design and python code
Professor: Dr. Bingdong Li
Created by Mukul Mondal
July 27, 2025
'''
#
'''
Problem statement:

Consider the following Waterfall Model. Carefully study and identify some of its inherent shortcomings. 
Then, using your list of shortcomings, design a modified Waterfall Model called YourLastName Model.

Using UML diagram of your choice, draft YourLastName Diagram making sure you clearly indicate your additions.

Implement the YourLastName class using Python, 
which will prompt the user to input the key elements of the diagram and 
return these objects in a well-formatted output.

'''

from os import system, name


# This is just a helper function to clear the screen.
def clearScreen():
    if name == 'nt':  # For windows system
        _ = system('cls')    
    else:             # for non-windows system
        _ = system('clear')
    return


# Problem statement asks to create this class.
class Mondal:
    registry = []  # Class-level list to store all Waterfall Phase instances
    def __init__(self):
        Mondal.registry.append(Communication("Communication"))
        Mondal.registry.append(Planning("Planning"))
        Mondal.registry.append(Modeling("Modeling"))
        Mondal.registry.append(Construction("Construction"))
        Mondal.registry.append(Deployment("Deployment"))
        Mondal.registry.append(Maintenance("Maintenance"))
    
    def ShowTasks(self):
        repeat = True
        phase_name: str = input('Enter Waterfall model phase name: ').lstrip().rstrip().lower()
        while repeat:
            repeat = False
            while len(phase_name) < 1:
                phase_name = input('Please try again, enter Waterfall model phase name OR type Q to quit: ').lstrip().rstrip().lower()
            if phase_name == 'q':                
                return
            
            foundPhase = list(filter(lambda x: x.name.lower() == phase_name, self.registry))
            if len(foundPhase) > 0 :
                print("Waterfall model phase: ",foundPhase[0].name, " has following sequential tasks: ")
                print(foundPhase[0].getTasks())                
            else:
                print("Invalid Waterfall model phase name entered.")
                phase_name = ""
                repeat = True
        return


# Parent Class for Waterfallmodel phases.
class WaterfallModelPhase:
    def __init__(self, name: str):
        self.name = name


# Child class to represent Waterfall Model's Phase: Communication
class Communication(WaterfallModelPhase):
    tasks = [
             "1. Project initiation.", 
             "2. Understand and gather the exact requirements of the customer.", 
             "3. Analyze these requirements.",
             "4. Document these analyzed requirements in software requirement specification (SRS) document.",
             "5. SRS document serves as a contract between the development team and customers."
            ]
    def getTasks(self):
        return "\n".join(self.tasks)


# Child class to represent Waterfall Model's Phase: Planning
class Planning(WaterfallModelPhase):
    tasks = [
             "1. Do all estimations.", 
             "2. Create a project work schedule, major milestones, and roadmap.", 
             "3. Establish Schedule tracking mechanism by software tools."             
            ]
    def getTasks(self):
        return "\n".join(self.tasks)


# Child class to represent Waterfall Model's Phase: Modeling
class Modeling(WaterfallModelPhase):
    tasks = [
             "1. Analyze the SRS document from design and implementaion point of view.",
             "2. Convert the requirement SRS document into a format, called Software Design Document(SDD).", 
             "3. High-Level Design (HLD): Outlines the broad structure of the system.",
             "4. HLD: Highlights the key components and how they interact with each other.",
             "5. Low-Level Design (LLD): It breaks down each component of HLD into smaller parts.",
             "6. LLD: Provides specifics about how each part will function, guiding the actual coding process."
            ]
    def getTasks(self):
        return "\n".join(self.tasks)


# Child class to represent Waterfall Model's Phase: Construction
class Construction(WaterfallModelPhase):
    tasks = [
             "1. The LLD is translated into source code using any suitable programming language.", 
             "2. The goal is to transform the design into working code using programming languages.",
             "3. Create Unit Test code.",
             "4. Do peer validation of the code.",
             "5. Run unit tests.",
             "6. Do peer validation of the code.",
             "7. Integrate various modules incrementally and run test in each step.",
             "8. There are 3 types of system testing: Alpha testing, Beta testing and Acceptance testing."
            ]
    def getTasks(self):
        return "\n".join(self.tasks)
    

# Child class to represent Waterfall Model's Phase: Testing
class Testing(WaterfallModelPhase):
    tasks = [
             "1. Run unit tests.", 
             "2. Integrate various modules incrementally and run test in each step.",
             "3. After all the modules have been successfully integrated and tested, the full working system is obtained.",
             "4. There are 3 types of system testing: Alpha testing, Beta testing and Acceptance testing."
            ]
    def getTasks(self):
        return "\n".join(self.tasks)
    

# Child class to represent Waterfall Model's Phase: Deployment
class Deployment(WaterfallModelPhase):
    tasks = [
             "1. Deploy the new system to the customer or end-users environment.", 
             "2. Focus on helping users to get comfortable with the new software system.",
             "3. End-user training, setting up necessary environments, feedback mechanism, and ensuring everything is running smoothly."
            ]
    def getTasks(self):
        return "\n".join(self.tasks)


# Child class to represent Waterfall Model's Phase: Maintenance
class Maintenance(WaterfallModelPhase):
    tasks = [
             "1. Correct errors that were not discovered during the product development phase.", 
             "2. If needed, enhance the functionalities of the system based on the customer’s request.",
             "3. Any adaptive maintenance for porting the software in a new environment such as new software platform or OS."
            ]
    def getTasks(self):
        return "\n".join(self.tasks)




if __name__ == "__main__":
    clearScreen()
    objMondal = Mondal()
    objMondal.ShowTasks()
