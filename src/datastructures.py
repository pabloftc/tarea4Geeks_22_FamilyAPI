
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [{
    "id": 76576,
    "first_name": "John",
    "age": 30,
    "lucky_numbers": [3, 5, 8]
}]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        try:
            if member["id"] == None:
                pass
        except Exception as e:
            print(f"Add member: {e}")
            member["id"] = self._generateId()
        self._members.append(member)

    def delete_member(self, id):
        result = {"done": False}
        try:
            self._members = list(filter(lambda member: id != member["id"], self._members))
            result["done"] = True
        except Exception as e:
            print(f"Get member: {e}")
        return result

    def get_member(self, id):
        result = {}
        try:
            for member in self._members:
                if member["id"] == id:
                    result = member
        except Exception as e:
            print(f"Get member: {e}")
        return result
 
       

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        print(self._members)
        return self._members
