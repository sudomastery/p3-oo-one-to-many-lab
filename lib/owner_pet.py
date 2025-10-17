class Pet:
    """Represents a pet belonging to an Owner."""

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        # Validate pet_type
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")

        # Validate owner when provided
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("owner must be an instance of Owner")

        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        # Track all instances
        Pet.all.append(self)


class Owner:
    """Represents a pet owner."""

    def __init__(self, name):
        self.name = name

    def pets(self):
        """Return a list of this owner's pets."""
        return [pet for pet in Pet.all if pet.owner is self]

    def add_pet(self, pet):
        """Attach a Pet to this owner after type-checking."""
        if not isinstance(pet, Pet):
            raise Exception("pet must be an instance of Pet")
        pet.owner = self
        return pet

    def get_sorted_pets(self):
        """Return pets sorted by name (ascending)."""
        return sorted(self.pets(), key=lambda p: p.name)