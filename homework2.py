from multiprocessing import shared_memory


class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education
    def introduce(self):
        if self.higher_education:
            education = "высшее образование есть"
        else:
            education = "высшего образования нет"
        print(f'Меня зовут {self.name}, я родился {self.birth_date}, по профессии {self.occupation}, {education} ')
class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name
    def introduce(self):
        print(f'My name is {self.name},I was born {self.birth_date}, I am {self.occupation}')
        print(f'My group is {self.group_name}')
class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby
    def introduce(self):
        print(f'My name is {self.name}, I was born {self.birth_date}, I am {self.occupation}')
        print(f'My hobby is {self.hobby}')
class BestFriend(Friend):
    def __init__(self, name, birth_date, occupation, higher_education,hobby, shared_memory):
        super().__init__(name, birth_date, occupation, higher_education, hobby)
        self.shared_memory = shared_memory
    def introduce(self):
        print(f'My name is {self.name}, I was born {self.birth_date}, I am {self.occupation}')
        print(f'My hobby is {self.hobby} memory: {self.shared_memory}')
classmate1=Classmate('Anatai','12.01.2000', 'programmer', True, '2b')
classmate2=Classmate('Kobi','12.02.2000', 'programmer', False, '2b')
friend1=Friend('Ben', '20.03.2010', 'designer', False, 'dancing')
friend2=BestFriend('John', '20.03.2010', 'designer', False, 'singing', 'School')
friend1.introduce()
friend2.introduce()
classmate1.introduce()
classmate2.introduce()
people=[classmate1,classmate2, friend1, friend2]
for person in people:
    person.introduce()