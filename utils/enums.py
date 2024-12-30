from enum import Enum

class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"

class ActiveUser(Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"

class TypeVote(Enum):
    MAJORITAIRE = "Vote Majoritaire"
    PROPORTIONNEL = "Vote Proportionnel"
    CONDORCET = "Vote Condorcet"