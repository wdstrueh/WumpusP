'''
Created on Nov 29, 2017

@author: Will Strueh and Tyler Meserve
'''
play = True

from Wumpus_Room_Generator import Room as R
from BinSearchTree import BinarySearchTree as BST
import Rooms

def deal_with_rooms(Bin_T, lines, roomss, adjrooms, room_adjroom_descs, room_adjrooms, descs):
    i = 1
    
    
    while i < len(lines):
        room_adjroom_desc = lines[i] + "," + lines[i + 1]
        room_adjrooms.append(room_adjroom_desc)
        i += 2
    
    
    i = 0
    while i < len(room_adjrooms):
        room_adjroom_descs.append(room_adjrooms[i].split(","))
        i += 1
    
    i = 0
    
    while i < len(room_adjroom_descs):
        room_adj = room_adjroom_descs[i][0]
        descs.append(room_adjroom_descs[i][1])
        roomss.append(room_adj.split(' ', 1)[0])
        
        #print(room_adj)
        adjrooms.append(room_adj.split(' ', 1)[1])
        i += 1
        
    i = 0
    while i < (len(roomss) and len(adjrooms)):
        room = roomss[i]
        adjroom = adjrooms[i]
        Rooms.store_adj_rooms(Bin_T, room, adjroom)
        i += 1

def play(Bin_T, room_count, room_wumpus_in, spider_rooms, pit_rooms, bat_room, resupply_room, descs):
    
    play = True
    room = 1
    arrows = 3
    wumpus_is_in = False
    
    
    
    
    
    while play:
        desc = Rooms.get_desc(room, descs)
        adjrooms = Rooms.get_adj_rooms(Bin_T, room)
        adjroomss = adjrooms.split()
        adjroom1 = adjroomss[0]
        adjroom2 = adjroomss[1]
        adjroom3 = adjroomss[2]
        
        print("You are in room {0}.\nYou have {1} arrows left.\n{2}\nThere are tunnels to {3}, {4}, and {5}".format(room, arrows, desc, adjroom1, adjroom2, adjroom3))
        
        Rooms.check_adjrooms_trap(room, adjrooms, room_count, room_wumpus_in, bat_room, resupply_room, spider_rooms, pit_rooms, arrows, wumpus_is_in)
        inputs = input("Do you want to move or shoot?")
        
        if inputs.lower().startswith("m") or inputs.lower() == "move":
            inputs = input("Which room?")
            if inputs in adjroomss:
                room = int(inputs)
                if inputs == room_wumpus_in:
                    print("The wumpus ate you and you could not escape in time.")
                    continue
            else:
                #can't reach
                print("Please enter a valid input.")
        elif inputs.lower().startswith("s") or inputs.lower() == "shoot":
            inputs = input("Which room?")
            if inputs in adjrooms:
                arrows -= 1
                if inputs == room_wumpus_in:
                    print("You slayed the mighty wumpus and you go home as a hero.")
                    continue
            else:
                print("Please enter a valid input.")
        else:
            print("Please enter a valid input.")

def main():
    Bin = BST()
    
    room_choices = []
    roomss = []
    adjrooms = []
    room_adjroom_descs = []
    room_adjrooms = []
    descs = []
    spider_rooms = []
    pit_rooms = []
    
    file = "Cave_Layout.txt"
    
#    file = input("Please enter the name of the cave layout.")
    
    with open(file, 'r') as fil:
        lines = fil.read().splitlines()
            
        room_spiders_pits_count = lines[0]
        
        room_spider_pits_count = room_spiders_pits_count.split()
        room_count = int(room_spider_pits_count[0])
        amount_spiders = int(room_spider_pits_count[1])
        amount_pits = int(room_spider_pits_count[2])
    
    deal_with_rooms(Bin, lines, roomss, adjrooms, room_adjroom_descs, room_adjrooms, descs)
    i = 2
    
    while i <= room_count:
        room_choices.append(i)
        i += 1
    
    random_rooms = Rooms.gen_traps_room(room_choices, amount_spiders, amount_pits)
    room_wumpus_in = random_rooms[0]
    bat_room = random_rooms[1]
    resupply_room = random_rooms[2]
    
    for x in range(len(random_rooms)):
        x = 3
        if amount_spiders >= 1:
            spider_rooms.append(random_rooms[x])
            amount_spiders -=1
            x += 1
        if amount_spiders == 0:
            if amount_pits >= 1:
                pit_rooms.append(random_rooms[x])
                amount_pits -= 1
    
    play(Bin, room_count, room_wumpus_in, spider_rooms, pit_rooms, bat_room, resupply_room, descs)

if __name__ == '__main__':
    main()