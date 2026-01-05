class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        

        
        if not isinstance(member, dict):
            raise ValueError("member must be a dict")

        if "first_name" not in member or not isinstance(member["first_name"], str) or member["first_name"].strip() == "":
            raise ValueError("first_name is required")

        if "age" not in member or not isinstance(member["age"], int) or member["age"] <= 0:
            raise ValueError("age must be an int > 0")

        if "lucky_numbers" not in member or not isinstance(member["lucky_numbers"], list):
            raise ValueError("lucky_numbers must be a list")

       
        new_member = {
            "id": self._generate_id(),
            "first_name": member["first_name"].strip(),
            "last_name": self.last_name,
            "age": member["age"],
            "lucky_numbers": member["lucky_numbers"]
        }

        self._members.append(new_member)
        return new_member

    def delete_member(self, id):
       
        for i in range(len(self._members)):
            if self._members[i]["id"] == id:
                self._members.pop(i)
                return True
        return False

    def get_member(self, id):
       
        for m in self._members:
            if m["id"] == id:
                return m
        return None

  
    def get_all_members(self):
        return self._members