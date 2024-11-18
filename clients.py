import uuid
import re

class Client:
    def __init__(self, first_name, last_name, email=None, phone=None, address=None):
        """
        Initializes a Client object with the given attributes.
        """
        self.__client_id = uuid.uuid4()
        self.first_name = first_name
        self.last_name = last_name
        if email:
            self.update_email(email)
        if phone:
            self.update_phone(phone)
        self.address = address

    def __repr__(self):
        return f"Client({self.__client_id}): {self.last_name}, {self.first_name} <{self.email}>"
    
    def __str__(self):
        return f"Client: {self.last_name}, {self.first_name}\n<{self.email}> {self.phone}"

    def get_contact_info(self):
        """
        Returns a formatted string of the client's contact information.
        """
        contact_info = f"Name:  {self.last_name}, {self.first_name}"
        if self.email:
            contact_info += f"\nEmail: {self.email}"
        if self.phone:
            contact_info += f"\nPhone: {self.phone}"
        if self.address:
            contact_info += f"\nAddress: {self.address}"
        return contact_info

    def update_email(self, new_email):
        """
        Updates the client's email address. Checks for address validity before updating.

        :param new_email: New email address (str)
        """
        valid: re.Match[str] | None = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', new_email)
        if valid:
            self.email = new_email

    def update_phone(self, new_phone):
        """
        Updates the client's phone number. Checks for digit length (10), then formats for screen.

        :param new_phone: New phone number (str)
        """
        if len(new_phone) == 10:
            self.phone = f"({new_phone[:3]}) {new_phone[3:6]}-{new_phone[6:]}"
