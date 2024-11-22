import uuid
import re

class Address:
    street1: str
    street2: str
    city: str
    state: str
    zip: str

class Client:
    def __init__(self, first_name, last_name, email=None, phone="", address=None, client_id=None):
        """
        Initializes a Client object with the given attributes.
        """
        if client_id:
            self.client_id: uuid.UUID = uuid.UUID(client_id)
        else:
            self.client_id: uuid.UUID = uuid.uuid4()
        self.first_name: str = first_name
        self.last_name: str = last_name
        if email:
            self.update_email(email)
        self.phone: str = phone
        # if address:
        #     self.address: Address = address
        self.address = address

    def __repr__(self) -> str:
        return f"Client({self.client_id}): {self.last_name}, {self.first_name} <{self.email}>"
    
    def __str__(self) -> str:
        return f"Client: {self.last_name}, {self.first_name}\n<{self.email}> {self.phone}"

    def get_contact_info(self) -> str:
        """
        Returns a formatted string of the client's contact information.
        """
        contact_info = f"Name:  {self.last_name}, {self.first_name}"
        if self.email:
            contact_info += f"\nEmail: {self.email}"
        if self.phone:
            contact_info += f"\nPhone: {self.display_phone()}"
        if self.address:
            contact_info += f"\nAddress: {self.address}"
        return contact_info

    def update_email(self, new_email) -> None:
        """
        Updates the client's email address. Checks for address validity before updating.

        :param new_email: New email address (str)
        """
        valid: re.Match[str] | None = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', new_email)
        if valid:
            self.email: str = new_email

    def display_phone(self) -> str:
        """
        Updates the client's phone number. Checks for digit length (10), then formats for screen.

        :param new_phone: New phone number (str)
        """
        if len(self.phone) == 10:
            return f"({self.phone[:3]}) {self.phone[3:6]}-{self.phone[6:]}"
        else:
            return self.phone
