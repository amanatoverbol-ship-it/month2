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
person1=Person(
    name='John',
    birth_date='02.12.2000',
    occupation='Doctor',
    higher_education=True,
)
person2=Person(
    name='Michael',
    birth_date='03.11.2002',
    occupation='Teacher',
    higher_education=False,
)
person3=Person(
    name='Jack',
    birth_date='06.02.2003',
    occupation='Fireman',
    higher_education=False,
)
people = [person1, person2, person3]
for person in people:
    print(f'Name: {person.name}')
    print(f'Birth date: {person.birth_date}')
    print(f'Occupation: {person.occupation}')
    print(f'Higher Education: {person.higher_education}')

person1.introduce()
person2.introduce()
person3.introduce()