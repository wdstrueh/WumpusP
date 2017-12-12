'''
Created on Nov 29, 2017

@author: Will Strueh and Tyler Meserve
'''
class Room(object):
    def __init__(self, rooms, room, wumpus, pit, roomcount):
        self.wumpus = wumpus
        self.pit = pit
        self.room = room
        self.rooms = rooms
        self.roomcount = roomcount

    def AdjRooms(self, room, rooms, roomcount):
        room_adjrooms = []
        room = 0
        rooms = []
        roomcount = 0
        self.AdjRooms = room_adjrooms
        return self.AdjRooms
    
    

    def hasWumpus(self, room, wumpus):
        if room != wumpus:
            return self.wumpus
        if room == wumpus:
            return self.wumpus

    def hasPit(self, room, pit):
        if room == pit:
            return self.pit
        if room != pit:
            return self.pit
