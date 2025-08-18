# Python Program: 
# CSC505: Principles of Software Development
# Module 5: Critical Thinking
# Professor: Dr. Bingdong Li 
# Created by Mukul Mondal
# Saturday, Aug 17, 2025

'''
Problem statement:
-- Web-based Pothole Tracking and Repair System --
The department of public works for a large city has decided to develop a web-based pothole tracking and repair system (PHTRS). 
A description follows:

Citizens can log onto a website and report the location and severity of potholes. As potholes are reported, they are logged within 
a "public works department repair system" and are assigned an identifying number, stored by street address, size (on a scale of 1 to 10), 
location (middle, curb, etc.), district (determined from street address), and repair priority (determined from the size of the pothole).

Work order data are associated with each pothole and include pothole location and size, repair crew identifying number, number of people 
on crew, equipment assigned, hours applied to repair, hole status (work in progress, repaired, temporary repair, not repaired), amount 
of filler material used, and cost of repair (computed from hours applied, number of people, material and equipment used).

Finally, a damage file is created to hold information about reported damage due to the pothole and includes the citizen's name, address, 
phone number, type of damage, and dollar amount of damage. PHTRS is an online system; all queries are to be made interactively.

Draw a UML use case diagram for a PHTRS system. You'll have to make a number of assumptions about the manner in which a user interacts 
with this system. Use Python to write a script that will print out the different actors and use cases  and a brief description of 
your diagram.
'''


from os import system, name
from typing import List
from enum import Enum, auto
import random, uuid


# This is just a helper function to clear the screen
# This is not required, per problem statement.
def clearScreen():
    if name == 'nt':  # For windows system
        _ = system('cls')    
    else:             # for non-windows system
        _ = system('clear')
    return


# Pothole severity (Critical, High, Medium, Low)
# Repair priority (Low: size 0-3, Medium: size 4-7, High: size 8-10)
# Pothole status (WIP, Repaired, Temporary_Repair, Unrepaired)
# Citizen's Damage type (Financial, Relocation, Rebuild, etc)

class PotholeSeverity(Enum):
    CRITICAL = auto()
    HIGH = auto()
    MEDIUM = auto()
    LOW = auto()

class PotholeLocation(Enum):
    MIDDLE = auto()
    CURB = auto()
    OTHERS = auto()    

class RepairPriority(Enum):    
    HIGH = auto()
    MEDIUM = auto()
    LOW = auto()

class PotholeStatus(Enum):    
    WIP = auto()
    REPAIRED = auto()
    TEMPORARY_REPAIRED = auto()
    UNREPAIRED = auto()

class CitizensDamageType(Enum):
    FINANCIAL = auto()
    RELOCATION = auto()
    REBUILD = auto()
    OTHERS = auto()



class RepairCrew:
    def __init__(self, peoplecount:int, perHrPrice: float):
        self.id: uuid = uuid.uuid4()
        self.peopleCount: int = peoplecount
        perMemberPerHrPrice: float = perHrPrice    


class Equipment:
    def __init__(self, desc:str, perHrPrice: float):
        self.id: uuid = uuid.uuid4()
        self.description: str = desc.lstrip().rstrip()
        self.perHrPrice: float = perHrPrice


class FillerMaterial:
    def __init__(self, desc:str, perHrPrice: float):
        self.id: uuid = uuid.uuid4()
        self.description: str = desc.lstrip().rstrip()
        self.unitPrice: float = perHrPrice


class Pothole:
    def __init__(self, addr:str, sevrt: PotholeSeverity):
        self.id: uuid = uuid.uuid4()
        self.address: str = addr.lstrip().rstrip()
        self.district: str = addr.lstrip().rstrip() # has to be parsed from address
        self.severity: PotholeSeverity = sevrt
        self.size: int = random.randint(1, 10)
        self.repairPriority: RepairPriority
        self.setRepairPriority()
    def setRepairPriority(self):
        if self.size > 7 and self.size < 11:
            self.repairPriority = RepairPriority.HIGH
        elif self.size > 3 and self.size < 8:
            self.repairPriority = RepairPriority.MEDIUM
        else:
            self.repairPriority = RepairPriority.LOW
        return
    


class WorkOrder:
    def __init__(self, pthid: uuid, repCrewId: uuid, crMemCount: int, wrkhours: int, fltMatuuid: uuid, fltMatAmount: float):
        self.id: uuid = uuid.uuid4()
        self.potholeid: uuid = pthid
        self.repairCrewId: uuid = repCrewId
        self.crewMemberCount: int = crMemCount
        self.equipments: List[Equipment]
        self.workedHours: int = wrkhours
        self.fillerMaterialId: uuid = fltMatuuid
        self.fillerMaterialAmount: float = fltMatAmount
        self.repairCost: float = self.getRepairCost()
    '''
    repairCost : Calculated as : 
            FillerMaterialAmount1*unitPrice + FillerMaterialAmount2*unitPrice + ..
          + (RepairCrew.peopleCount)*(RepairCrew.perMemberPerHrPrice)*(workedHours) 
          + equipment1*perHrPrice*workedHours + equipment2*perHrPrice*workedHours 
    '''
    def getRepairCost(self):
        return 450.59 # some random selected, actually can be calculated as explained above


   
class DamageFile:
    def __init__(self, ctzName: str, ctzAddr: str, ctzPhs: str, dmgType: CitizensDamageType, dmgCost: float):
        self.citizenName: str = ctzName.lstrip().rstrip()
        self.citizenAddress: str = ctzAddr.lstrip().rstrip()
        self.citizenPhones: str = ctzPhs.lstrip().rstrip()
        self.damageType: CitizensDamageType = dmgType
        self.cost: float = dmgCost
    def SaveFile():
        print("Create and Save a report file for the Citizen's damage")
        return




# Usage
# Usecase, Actor and usecase details
def execute_module5_ct_usecase_trigger_sequence():    
    print("Public works department repair system")
    print("=== Use Cases and Trigger Sequences ===")
    print("Use Case: PHTRS and and Running")
    print("\t: PHTRS is ready to accept web requests from citizens")

    print("Use Case: Citizen login. Actor: Primary actor.")
    print("Use Case(optional): Unsuccessful login. Possibly Registration update needed.")
    print("\t: Citizen logs in with their credential.")
    print("\t: Citizen goes to Pothole reporting web page.")    
    
    print("Use Case: Register/Report Pothole. Actor: Primary actor.")
    print("\t: Citizen registers the Pothole with it's address and sevirity.")
    
    print("Use Case: Create and initialize other supporting objects. Actor: System actor.")
    print("\t: Create and initialize other supporting objects like RepairCrew, Equipment, FillerMaterial etc")
    
    print("Use Case: Create Pothole object. Actor: System actor.")
    print("\t: Initializes all other required properties of the Pothole")
    
    print("Use Case: Save Pothole object in Storage. Actor: System actor.")
    print("\t: Saves the Pothole object's Sate in Storage.")

    print("Use Case: Create WorkOrder object. Actor: Human actor and System actor.")
    print("\t: An Employee within 'the department of public works' creates the WorkOrder based on the Pothole object.")
    print("\t: WorkOrder object fully initialized by the System actor")

    print("Use Case: Save WorkOrder object in Storage. Actor: System actor.")
    print("\t: Saves the WorkOrder object's Sate in Storage.")
    
    print("Use Case: Start WorkOrder. Actor: Human actor.") # An Employee within 'the department of public works' Starts the WorkOrder.
    print("\t: An Employee within 'the department of public works' Starts the WorkOrder.")

    print("Use Case: Update WorkOrder as work progress. Actor: System actor.") # During execution of the WorkOrder, different properties of the WorkOrder get updated.    
    print("\t: During execution of the WorkOrder, different properties of the WorkOrder get updated.")

    print("Use Case: Create Damage Report. Actor: Human actor.") # An Employee within 'the department of public works' Creates the 'Citizen's Damage report' dues to the Pothole.
    print("\t: An Employee within 'the department of public works' creates the Damage Report.")
    print("\t: Damage Report contains. Citizen's personal information, type of damage and associated cost.")

    print("Use Case: Store Damage Report. Actor: System actor.") # Saves the 'Damage Report' in storage.
    print("\t: Saves the Damage Report in Storage.")
    return


# object creation sequences
def execute_module5_ct_object_creation():
    print("PHTRS system : running")
    print("Public works department repair system")
    print("Creating few common objects which will be used later by the PHTRS system")
    print("RepairCrew : object created")
    print("Equipment : object created")
    print("FillerMaterial : object created")

    print("PHTRS system Home page: displayed")
    print("User selects login page")
    print("Please describe pothole, you like to report")
    
    # Pothole object creation
    print("Logged in user enters: pathole address")
    print("Logged in user enters: pathole Severity(CRITICAL, HIGH, MEDIUM, LOW)")
    print("Pothole : object created with above Address and Severity.")

    print("PHTRS system initilizes other properties of the Pothole object, as follows.")
    print("uuid: identifying number")
    print("district: parsed district part from the user entered full address")
    print("size: an integer number 1-10")
    print("RepairPriority: LOW, MEDIUM, LOW")

    # WorkOrder object creation
    print("WorkOrder : object created with uuid.")
    print("potholeid : initialized with above created pathole object's uuid.")
    print("repairCrewId : initialized with already existing RepairCrew object's uuid.")
    print("equipments : initialized with couple of already existing Equipment objects.")
    print("workedHours : initialize this property")
    print("fillerMaterialId : initialize this by FillerMaterial's uuid property")
    print("fillerMaterialAmount : initialize this with how many units of FillerMaterial used")
    print('''repairCost : initialize or calculated as : 
            FillerMaterialAmount1*unitPrice + FillerMaterialAmount2*unitPrice + ..
          + (RepairCrew.peopleCount)*(RepairCrew.perMemberPerHrPrice)*(workedHours) 
          + equipment1*perHrPrice*workedHours + equipment2*perHrPrice*workedHours ''')
    
    # DamageFile object creation
    print("DamageFile : object creating")
    print("citizenName : assigned to the object")
    print("citizenAddress : assigned to the object")
    print("citizenPhones : assigned to the object")
    print("damageType : CitizensDamageType(FINANCIAL,RELOCATION,REBUILD,OTHERS) assigned to the object")
    print("cost : Calculated and assigned to the object")
    print("Create and Save a report file based on this object for the Citizen's damage")
    return




if __name__ == "__main__":
    clearScreen()
    print("=== Module 5: Critical Thinking: Web-based Pothole Tracking and Repair System (PHTRS) ===")
    print(" == Use Cases, Actors and use case details == ")
    execute_module5_ct_usecase_trigger_sequence()

    print("\n")
    print(" == Use Cases, and General working sequence == ")
    execute_module5_ct_object_creation()
