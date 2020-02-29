# Algorithm Idea: The City Grid 

## Basics 
What if we just built/hard-coded a grid of 5 rows by 20 columns deep with the following characteristics 
- First and last rows are effectively "T" shaped (except for start and end rooms of the middle 2nd-4th rows)

## Rough Idea of Layout 
(Pretend the rows and columns are even, 5 rows and 20 "columns")

The starting room is on the left 
```

|T|T|T|T|T|T|T|T|T|T|T||T|T|T|T|T||T|T|T|T|T||T|T|T|T|7| (ROW 1)
||-|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|-|| (ROW 2)

||-|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|-|| (ROWS 3-4)

[ROW FIVE is LIKE ROW 1 but Upside down T's and first room is |L|]
```

### Key: 
|T| = open to the south, open to east and west
|7| = Open only to south, 
|+| = open on all four cardinal directions
||-| = open to North, South, East 
|-|| = Open to East, North, South
|L| = open only to North and West, bottom corner 
|_|| = Last room is open to east and North only 

## Algorithim Process?
0. Create a List/Description of room names (length = 100) and a List/Array of Descriptions (length = 100) or List of a hundred objects with two parameters (Name, Description, see `Room` in models.py)
   - Important Rooms (where we really should think about description): 
    - Entrance, 
    - Western Edges: 20th Room (index 19), 40th Room, 60th, 80th Room (|-||)
    - Eastern Edges: 21st, 41st, 61st, 81st Rooms 
    - End Room (_|) (I don't know put a treasure trest here)

1. Create a hundred rooms using a For Loop (pulling name, and description) (put them in a list?)

2. Run a For loop to connect the rooms and according to the room index (if it's 20th room, it gets to be |7| and if it's the last room, i.e. room_list[99] |_|| )




