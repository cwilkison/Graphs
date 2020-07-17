from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)



# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# starts like breadth first. we need to visit every single room and use depth first becaues we need to get every room by path.
# using traversal_path array we can add add path directions in order to keep track of path movements length/distance.
traversal_path = []
# use a visited dictionary to keep record of all the rooms we have visited, test uses this to see how many rooms we hit
visited_rooms = {}
# use a path array to keep current location based of a queue
path = []
# using directoins dictionary we can move in and out of room.py using the get_exists function -- necessary for reversing out of a dead room
directions = {'n':'s', 's':'n', 'e':'w', 'w':'e'}

# start with current room and add it to visited.  then get the exits to start traversing the map
visited_rooms[player.current_room.id] = player.current_room.get_exits()

# begin loop while the length of visited rooms is less than the total number of rooms.  We havn't hit all the rooms yet
while len(visited_rooms) < len(room_graph) - 1:
    # if the player room is not yet visited....
    if player.current_room.id not in visited_rooms:
        # add unvisited room to visited dictionary.
        visited_rooms[player.current_room.id] = player.current_room.get_exits()
        # remove previous direction so you don't go into same room -- remove previous set of exists and replace with current exits
        prev_direction = path[-1]
        visited_rooms[player.current_room.id].remove(prev_direction)

    # bf found the shortests path, now check to see if all rooms have been visisted (visted == number of rooms) and find number of rooms.

    # change traversal to look for all rooms, not just shortest path
    # all paths have been explored, try backtrack into a previous room until you can go a new direction
    while len(visited_rooms[player.current_room.id]) == 0:
        # backtrack and pop the last get_exits directions and return it to previous direction variable and add it to the traversal_path
        prev_direction = path.pop()
        traversal_path.append(prev_direction)
        # use player travel function to move to previous room.  check if that room is visited
        player.travel(prev_direction)

    # check the current room exists, pop the last room on the list and go to that room/find last value
    nxt_move = visited_rooms[player.current_room.id].pop(0)
    # append to path since we now want to go this direction
    traversal_path.append(nxt_move)
    # append it to path so we can record visiting the room
    path.append(directions[nxt_move])
    # travel in the directoin of the move variable using travel function and opposite directions list at beginning
    player.travel(nxt_move)
   
##MVP 1004 moves, 500 rooms visited

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
