from room import Room
from player import Player
from world import World
import random
from util import Stack, Queue
from ast import literal_eval
from os.path import dirname, join, realpath

map_file = join(dirname(realpath(__file__)), 'main_maze.txt')

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with ds to walk
# traversal_path = ['n', 'n']
traversal_path = []
# graph == world.rooms == {}

#initialize dicts of unknown rooms
for i in room_graph.items():
    world.rooms[i[0]] = {}
    dict_vals = []
    for v in i[1][1].keys():
        world.rooms[i[0]][v] = "?"

def completionize(room): # get all unexplored rooms from cur position
    return [possdir for possdir, label in room.items() if label == '?']

def backtrack(d): # determine reverse of given direction to backtrack
    conversion = {'n':'s', 'e':'w', 's':'n', 'w':'e'}
    return conversion[d]

def explore_rooms(player, graph):
    run = True 
    while run:
        more = False # init a state for "more to explore"

        # this if clause is covering case outside of while loop
        #   in which player must backtrack to find new unexplored rooms
        if len(traversal_path) > 0: # if we've already begun traversal
            for i in reversed(traversal_path): # for our backtracked path
                player.travel(backtrack(i)) # nextroom one step
                traversal_path.append(backtrack(i)) # add backtrack step to path
                if len(completionize(graph[player.current_room.id])) > 0:
                # adjacent rooms remaining to explore; break back to while loop
                    more = True
                    break
            if not more: # if there's no more unexplored rooms in the backtrack
                return traversal_path # return completed path

        while len(completionize(graph[player.current_room.id])) > 0:
        # while adjacent rooms remain left to explore        
                room_id = player.current_room.id
                # based on room player is in,
                unexplored = completionize(graph[room_id])
                # identify unexplored rooms
                nextroom = random.choice(unexplored)
                player.travel(nextroom)
                # and travel to one of them
                graph[room_id][nextroom] = player.current_room.id
                # update graph with this new room's id
                graph[player.current_room.id][backtrack(nextroom)] = room_id
                # and update the graph with the 'path' back to the previous room
                traversal_path.append(nextroom)
                # and add the latest turn to the traversal path

explore_rooms(player, world.rooms)

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
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
