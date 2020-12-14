#making an airport class
class Airport:

    #init is just a string of the name of an airport
    def __init__(self, name: str):
        #the name
        self.name = name
        #the list of all of its destinations
        self.destinations = []

    #What to return when wanting a string
    def __str__(self):
        return self.name

    #returns a list of the destinations
    def get_dest(self):
        return self.destinations

    #Sets its destination list to the given one
    def make_list(self, all_dests: list):
        self.destinations = all_dests

    def add_destination(self, dest):
        self.destinations.append(dest)

    #Checks to see if it can fly to a certain destination
    def fly_to(self, destination):
        for airport in self.destinations:
            if airport == destination:
                #Will return true if can
                return True
        #if not then false
        return False

#Function that finds the fastest way from one airport to another
#Uses recursion in order to find the fastest way there
def find_way(takeoff, dest):
    #Makes the main list that it will contain the route to take of flights
    main_list = []
    #Checks to see if destination is alread in takeoff's destinations
    if takeoff.fly_to(dest):
        #if so then append to list
        main_list.append(dest.name)
    else:
        #For loop to go through all of the airports
        for airports in takeoff.get_dest():
            #If the list is empty then make first list the main list
            if len(main_list) == 0:
                #Make first list main list
                main_list = find_way(airports, dest)
            else:
                #checks to see if the new way is faster or not
                if len(find_way(airports, dest)) < len(main_list):
                    #if so then make the new list the main list
                    main_list = find_way(airports, dest)
    #Instert the original takeoff spot at the beginning
    main_list.insert(0, takeoff.name)
    #return the list
    return main_list

def main():
    #Makeing a bunch of airports
    SAN = Airport("SAN")
    JFK = Airport("JFK")
    LAX = Airport("LAX")
    SFO = Airport("SFO")
    SEA = Airport("SEA")
    ATL = Airport("ATL")
    #Adding all of their destinations
    SAN.make_list([ATL, LAX])
    ATL.add_destination(JFK)
    LAX.add_destination(ATL)
    LAX.add_destination(SFO)
    SFO.add_destination(ATL)
    SFO.add_destination(SEA)
    SEA.add_destination(ATL)
    #Running fucntion to find fastest way from SAN to JFK
    the_list = find_way(SAN, JFK)
    #Printing the list
    print(the_list)

#Running it
if __name__ == '__main__':
    main()