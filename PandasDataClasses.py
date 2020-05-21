from dataclasses import dataclass, field
from typing import ClassVar
import datetime

@dataclass
class Employee:
    fname: str
    lname: str
    pay: int
    email: str = field(init=False)

    # class variables
    raise_amount: ClassVar[float] = 0.5
    num_of_emps: ClassVar[int] = 0

    def __post_init__(self):
        self.email = self.fname + self.lname + '@gmail.com'
        Employee.num_of_emps += 1

    def fullname(self): 
        return f'{self.fname} {self.lname}'

    def apply_raise(self): 
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        fname, lname, pay = emp_str.split('-')
        return cls(fname, lname, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
