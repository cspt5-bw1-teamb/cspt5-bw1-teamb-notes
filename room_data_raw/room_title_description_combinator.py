import random



room_types = ["CHAMBER", "ROOM", "HALLWAY", "OVERLOOK", "CLOISTER", 
            "ANTECHAMBER", "CLOAKROOM", "LOBBY", 
            "CELLAR", "LIBRARY", "CLOSET", 
            "BEDROOM", "BARRACKS", "STOREROOM"]

room_adjectives = ["HAUNTED", "DARK", "TENEBROUS", "SHADOWY", 
            "MURKY", "DIM", "PLUTONIAN", "OBSIDIAN", 
            "CIMMERIAN","CLOUDED", "FOGGY", "DARKENED", "CALIGINOUS", "HAZY", "STYGIAN"]


room_description = ["There is nothing to see here.", 
                    "A thousand eyes stare at you from the darkness.",
                    "This place is incredibly dusty.", 
                    "A sudden melancholy over takes you.", 
                    "Even the shadows seems to pity you here.",
                    "There are only shadows, spiritual and physical here.",
                    "The light in this place has gone out a long time ago.",
                    "You wish you had brought a torch. It's really dark in here.",
                    "Unfortunately, you cannot see in the dark, so this room will forever be mysterious."]


print(f"A {random.choice(room_adjectives)} {random.choice(room_types)}")

room_dict_list = []
for num in range(100):
    room_dict_list.append({
            "title":f"A {random.choice(room_adjectives)} {random.choice(room_types)}",
            "description": random.choice(room_description)
            })

print(room_dict_list)

# 100 Room Titles and Descriptions
room_title_description_source = [{'title': 'A OBSIDIAN CLOISTER', 'description': "You wish you had brought a torch. It's really dark in here."}, {'title': 'A HAZY BARRACKS', 'description': 'A thousand eyes stare at you from the darkness.'}, {'title': 'A HAUNTED BEDROOM', 'description': 'The light in this place has gone out a long time ago.'}, {'title': 'A MURKY LOBBY', 'description': 'Even the shadows seems to pity you here.'}, {'title': 'A STYGIAN ROOM', 'description': 'This place is incredibly dusty.'}, {'title': 'A CALIGINOUS ANTECHAMBER', 'description': "You wish you had brought a torch. It's really dark in here."}, {'title': 'A FOGGY STOREROOM', 'description': 'Unfortunately, you cannot see in the dark, so this room will forever be mysterious.'}, {'title': 'A DARK HALLWAY', 'description': 'There are only shadows, spiritual and physical here.'}, {'title': 'A PLUTONIAN CHAMBER', 'description': 'Even the shadows seems to pity you here.'}, {'title': 'A HAZY CLOAKROOM', 'description': "You wish you had brought a torch. It's really dark in here."}, {'title': 'A STYGIAN LOBBY', 'description': "You wish you had brought a torch. It's really dark in here."}, {'title': 'A DARKENED BARRACKS', 'description': 'This place is incredibly dusty.'}, {'title': 'A TENEBROUS CELLAR', 'description': 'There are only shadows, spiritual and physical here.'}, {'title': 'A CIMMERIAN STOREROOM', 'description': "You wish you had brought a torch. It's really dark in here."}, {'title': 'A CIMMERIAN BEDROOM', 'description': 'A sudden melancholy over takes you.'}, {'title': 'A CLOUDED STOREROOM', 'description': "You wish you had brought a torch. It's really dark in here."}, {'title': 'A MURKY CLOISTER', 'description': 'A thousand eyes stare at you from the darkness.'}, {'title': 'A PLUTONIAN STOREROOM', 'description': 'The light in this place has gone out a long time ago.'}, {'title': 'A STYGIAN ROOM', 'description': 'The light in this place has gone out a long time ago.'}, {'title': 'A CLOUDED STOREROOM', 'description': 'There are only shadows, spiritual and physical here.'}, {'title': 'A DARKENED LIBRARY', 'description': 'This place is incredibly dusty.'}, {'title': 'A DARK ROOM', 'description': "You wish you had brought a torch. It's really dark in here."}, {'title': 'A OBSIDIAN CELLAR', 'description': 'A sudden melancholy over takes you.'}, {'title': 'A TENEBROUS CLOAKROOM', 'description': 'This place is incredibly dusty.'}, {'title': 'A HAUNTED HALLWAY', 'description': 'This place is incredibly dusty.'}, {'title': 'A CIMMERIAN LOBBY', 'description': 'A sudden melancholy over takes you.'}, {'title': 'A OBSIDIAN ROOM', 'description': 'A sudden melancholy over takes you.'}, {'title': 'A DIM ANTECHAMBER', 'description': 'A thousand eyes stare at you from the darkness.'}, {'title': 'A PLUTONIAN CLOISTER', 'description': 'This place is incredibly dusty.'}, {'title': 'A SHADOWY LIBRARY', 'description': 'Even the shadows seems to pity you here.'}, {'title': 'A OBSIDIAN CHAMBER', 'description': 'Unfortunately, you cannot see in the dark, so this room will forever be mysterious.'}, {'title': 'A TENEBROUS CLOISTER', 'description': 'Even the shadows seems to pity you here.'}, {'title': 'A HAZY ANTECHAMBER', 'description': 'A sudden melancholy over takes you.'}, {'title': 'A TENEBROUS OVERLOOK', 'description': 'A sudden melancholy over takes you.'}, {'title': 'A CLOUDED CELLAR', 'description': 'The light in this place has gone out a long time ago.'}, {'title': 'A OBSIDIAN BEDROOM', 'description': 'Even the shadows seems to pity you here.'}, {'title': 'A DARK CELLAR', 'description': 'A thousand eyes stare at you from the darkness.'}, {'title': 'A DARK STOREROOM', 'description': 'There are only shadows, spiritual and physical here.'}, {'title': 'A DIM BEDROOM', 'description': "You wish you had brought a torch. It's really dark in here."}, {'title': 'A SHADOWY CLOSET', 'description': 'Unfortunately, you cannot see in the dark, so this room will forever be mysterious.'}, {'title': 'A OBSIDIAN LOBBY', 'description': 'Even the shadows seems to pity you here.'}, {'title': 'A DARKENED LOBBY', 'description': 'A sudden melancholy over takes you.'}, {'title': 'A CIMMERIAN CLOSET', 'description': "You wish you had brought a torch. It's really dark in here."}, {'title': 'A SHADOWY OVERLOOK', 'description': 'There is nothing to see here.'}, {'title': 'A TENEBROUS BEDROOM', 'description': 'There are only shadows, spiritual and physical here.'}, {'title': 'A OBSIDIAN LOBBY', 'description': 'There is nothing to see here.'}, {'title': 'A PLUTONIAN LIBRARY', 'description': 'The light in this place has gone out a long time ago.'}, {'title': 'A CALIGINOUS CLOSET', 'description': 'There are only shadows, spiritual and physical here.'}, {'title': 'A CIMMERIAN STOREROOM', 'description': 'The light in this place has gone out a long time ago.'}, {'title': 'A CLOUDED ROOM', 'description': 'A thousand eyes stare at you from the darkness.'}, {'title': 'A DARKENED CLOISTER', 'description': "You wish you had brought a torch. It's really dark in here."}, {'title': 'A HAZY ROOM', 'description': 'A sudden melancholy over takes you.'}, {'title': 'A CIMMERIAN LOBBY', 'description': 'A thousand eyes stare at you from the darkness.'}, {'title': 'A HAUNTED CELLAR', 'description': 'Unfortunately, you cannot see in the dark, so this room will forever be mysterious.'}, {'title': 'A DIM OVERLOOK', 'description': 'A thousand eyes stare at you from the darkness.'}, {'title': 'A DARK ANTECHAMBER', 'description': 'A sudden melancholy over takes you.'}, {'title': 'A DIM ANTECHAMBER', 'description': 'This place is incredibly dusty.'}, {'title': 'A HAUNTED CHAMBER', 'description': 'Even the shadows seems to pity you here.'}, {'title': 'A HAZY CHAMBER', 'description': 'The light in this place has gone out a long time ago.'}, {'title': 'A CALIGINOUS LIBRARY', 'description': 'There is nothing to see here.'}, {'title': 'A CIMMERIAN CLOSET', 'description': 'This place is incredibly dusty.'}, {'title': 'A CALIGINOUS CHAMBER', 'description': 'The light in this place has gone out a long time ago.'}, {'title': 'A CLOUDED BEDROOM', 'description': 'This place is incredibly dusty.'}, {'title': 'A DIM STOREROOM', 'description': 'A thousand eyes stare at you from the darkness.'}, {'title': 'A SHADOWY CHAMBER', 'description': 'Even the shadows seems to pity you here.'}, {'title': 'A DARK LOBBY', 'description': "You wish you had brought a torch. It's really dark in here."}, {'title': 'A PLUTONIAN CLOISTER', 'description': 'A thousand eyes stare at you from the darkness.'}, {'title': 'A DARK LOBBY', 'description': "You wish you had brought a torch. It's really dark in here."}, {'title': 'A CIMMERIAN CLOISTER', 'description': 'There is nothing to see here.'}, {'title': 'A DARKENED BARRACKS', 'description': 'There are only shadows, spiritual and physical here.'}, {'title': 'A DARKENED OVERLOOK', 'description': 'There are only shadows, spiritual and physical here.'}, {'title': 'A CALIGINOUS LOBBY', 'description': 'There are only shadows, spiritual and physical here.'}, {'title': 'A CIMMERIAN BARRACKS', 'description': 'A sudden melancholy over takes you.'}, {'title': 'A DARKENED OVERLOOK', 'description': 'Unfortunately, you cannot see in the dark, so this room will forever be mysterious.'}, {'title': 'A CLOUDED ANTECHAMBER', 'description': 'There are only shadows, spiritual and physical here.'}, {'title': 'A CIMMERIAN BEDROOM', 'description': 'There is nothing to see here.'}, {'title': 'A CALIGINOUS BARRACKS', 'description': 'Unfortunately, you cannot see in the dark, so this room will forever be mysterious.'}, {'title': 'A CALIGINOUS CLOAKROOM', 'description': "You wish you had brought a torch. It's really dark in here."}, {'title': 'A PLUTONIAN HALLWAY', 'description': 'This place is incredibly dusty.'}, {'title': 'A MURKY CLOISTER', 'description': 'The light in this place has gone out a long time ago.'}, {'title': 'A CLOUDED ROOM', 'description': 'Unfortunately, you cannot see in the dark, so this room will forever be mysterious.'}, {'title': 'A HAZY ROOM', 'description': 'A sudden melancholy over takes you.'}, {'title': 'A HAZY OVERLOOK', 'description': 'Even the shadows seems to pity you here.'}, {'title': 'A TENEBROUS ANTECHAMBER', 'description': 'There is nothing to see here.'}, {'title': 'A CLOUDED BARRACKS', 'description': 'The light in this place has gone out a long time ago.'}, {'title': 'A CLOUDED ROOM', 'description': 'There are only shadows, spiritual and physical here.'}, {'title': 'A SHADOWY CLOAKROOM', 'description': 'A thousand eyes stare at you from the darkness.'}, {'title': 'A CIMMERIAN HALLWAY', 'description': 'A sudden melancholy over takes you.'}, {'title': 'A SHADOWY CLOAKROOM', 'description': "You wish you had brought a torch. It's really dark in here."}, {'title': 'A CALIGINOUS OVERLOOK', 'description': 'There are only shadows, spiritual and physical here.'}, {'title': 'A TENEBROUS CLOISTER', 'description': 'A thousand eyes stare at you from the darkness.'}, {'title': 'A TENEBROUS OVERLOOK', 'description': "You wish you had brought a torch. It's really dark in here."}, {'title': 'A CALIGINOUS CLOISTER', 'description': 'This place is incredibly dusty.'}, {'title': 'A HAZY BARRACKS', 'description': 'A sudden melancholy over takes you.'}, {'title': 'A TENEBROUS OVERLOOK', 'description': 'Even the shadows seems to pity you here.'}, {'title': 'A STYGIAN CHAMBER', 'description': 'Even the shadows seems to pity you here.'}, {'title': 'A TENEBROUS CLOAKROOM', 'description': 'There is nothing to see here.'}, {'title': 'A FOGGY BARRACKS', 'description': 'Even the shadows seems to pity you here.'}, {'title': 'A CIMMERIAN CLOSET', 'description': 'A thousand eyes stare at you from the darkness.'}, {'title': 'A OBSIDIAN ANTECHAMBER', 'description': 'Even the shadows seems to pity you here.'}]




# Imported this here for testing purposes. 
class Room:
    def __init__(self, id, name, description, x, y):
        self.id = id
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.x = x
        self.y = y
    def __repr__(self):
        if self.e_to is not None:
            return f"({self.x}, {self.y}) -> ({self.e_to.x}, {self.e_to.y})"
        return f"({self.x}, {self.y})"
    def connect_rooms(self, connecting_room, direction):
        '''
        Connect two rooms in the given n/s/e/w direction
        '''
        reverse_dirs = {"n": "s", "s": "n", "e": "w", "w": "e"}
        reverse_dir = reverse_dirs[direction]
        setattr(self, f"{direction}_to", connecting_room)
        setattr(connecting_room, f"{reverse_dir}_to", self)
    def get_room_in_direction(self, direction):
        '''
        Connect two rooms in the given n/s/e/w direction
        '''
        return getattr(self, f"{direction}_to")
