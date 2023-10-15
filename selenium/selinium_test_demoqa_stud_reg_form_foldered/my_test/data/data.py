from dataclasses import dataclass


@dataclass
class Person:
    """clas that used only for data storing"""

    first_name: str = None
    last_name: str = None
    email: str = None
    current_adress: str = None
    mobile_phone: str = None
    subject: str = None
