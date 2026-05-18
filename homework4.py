class Contact(object):
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    @classmethod
    def valid_phone(cls, phone):
        if len(phone) == 10 and phone.isdigit():
            return True
        else:
            return False
class ContactList(object):
    all_contacts = []
    @classmethod
    def add_contact (cls, name, phone):
        if Contact.valid_phone(phone) == True:
            new_contact = Contact(name, phone)
            cls.all_contacts.append(new_contact)
        else:
            raise ValueError("Invalid phone number")

ContactList.add_contact('Анатай', '0555555555')
print(ContactList.all_contacts)
for contact in ContactList.all_contacts:
    print(contact.name, contact.phone)
