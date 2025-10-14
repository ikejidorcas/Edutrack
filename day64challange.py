class jobs:
    def __init__(self, name, salary, hours):
        self.name = name
        self.salary = salary
        self.hours = hours
    def omo(self):
        print(f'{self.name} is being paid {self.salary}, for just {self.hours}')
class doctor(jobs):
    def __init__(self, experience, specialty):
        self.name = 'A doctor'
        self.salary ='230k'
        self.hours = '4 hours per day'
        self.experience = experience
        self.specialty = specialty
class teacher(jobs):
    def __init__(self, subject, position):
        self.name = 'A Teacher'
        self.salary ='130k'
        self.hours = '8 hours per day'
        self.subject = subject
        self.position = position


job1 = jobs('A lawyer','150k', ' 3 hours per day')
job1.omo()
job2 = doctor('2 years experience', 'paediatric consultant')
job2.omo()
print(f'The {job2.specialty} has just {job2.experience}')
job3= teacher('form teacher', 'computer science teacher')
job3.omo()
print(f'The {job3.position} is also a {job3.subject}')