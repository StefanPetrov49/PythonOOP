class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                result = room.take_room(people)
                if not result:
                    self.guests += people


    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                room.is_taken = False
                self.guests = 0

    def status(self):
        return f"Hotel {self.name} has {self.guests} total guests\n"\
               f"Free rooms: {', '.join([str(r.number) for r in self.rooms if r.is_taken == False])}\n" \
               f"Taken rooms: {', '.join([str(r.number) for r in self.rooms if r.is_taken == True])}"

