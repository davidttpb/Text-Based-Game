# Function to display instructions
def show_instructions():  
   #print a main menu and the commands
   print("Elden Ring Adeventure Text Game")
   print("Collect 6 items to defeat the great demi-god, Radhan.. or be slain by his gravitational powers!.")
   print("Move commands: go South, go North, go East, go West")
   print("Add to Inventory: get 'item name'\n")



# Main function
def main():
    # Calling function to display instructions
    show_instructions()
    # A dictionary linking a room to other rooms
    # and linking one item for each room
    rooms = {'Caleid' : { 'South' : 'Academy of Raya Lucaria', 'North': 'Stormveil Castle', 'East' : 'Volcano Manor', 'West' : 'Capital of Lyndel', 'item' : None},
             'Academy of Raya Lucaria' : { 'North' : 'Caleid', 'item' : 'Ezykes Decay' },
             'Capital of Lyndel' :{'East' : 'Caleid', 'item' : 'Berserker Armor'},
             'Stormveil Castle' : {'South' : 'Caleid', 'item' : 'Giant Great Sword'},
             'Volcano Manor' : { 'West' : 'Caleid', 'South' : 'Limgrave', 'item' : 'Magical Flasks' },
             'Limgrave' : { 'North' : 'Volcano Manor', 'East' : 'Great Caves of Elden Ring', 'item' : 'Torrents Great Ring'},
             'Great Caves of Elden Ring' : { 'West' : 'Limgrave', 'North' : 'Roundtable Hold', 'item' : 'Somber Stone'},
             'Roundtable Hold' : { 'South' : 'Great Caves of Elden Ring', 'North' : 'Festival of Desert\'s', 'item' : 'Black Smith'},
             'Festival of Desert\'s' : { 'South' : 'Roundtable Hold', 'item' : 'Radhan'}
            }
    
    # Starting room
    current_room = 'Caleid'
    # List to store collected items
    inventory = []
    
    # Loop to simulate moves between rooms based on the user input
    while True:
        # If current_room is Festival Of Desert’s then breaking the loop
        if current_room == 'Festival of Desert\'s':
            print("You are in ", current_room)
            print("Radhan has been summoned !",)
            if len(inventory) == 7:
                print("You have what it takes to defeat Radhan!")
            else:
                print("Radhan: YOU WERE NO MATCH FOR ME")
            break
        
        # Printing current_room
        print("\nYou are in ", current_room)
        
        # Taking user opinion to pick the item or not
        if rooms[current_room]['item'] != None:
            print("You see", rooms[current_room]['item'])
            grab_item = input("get "+rooms[current_room]['item']+"?(Y/N): ").upper()
            # Validating user input
            while grab_item not in ['Y','N']:
                print("Invalid input. Try again")
                grab_item = input("Grab "+rooms[current_room]['item']+"?(Y/N): ").upper()
            if grab_item == 'Y':
                inventory.append(rooms[current_room]['item'])
                rooms[current_room]['item'] = None  
        else:
            print("Already item collected or nothing in this room")
        
        # Printing inventory
        print("Inventory:", inventory)
        
        # Taking user input for direction to move
        direction = input("Direction to move?(East,West,North,South): ").title()
        directions = list(rooms[current_room].keys())
        directions.remove('item')
        # Validating direction
        while direction not in directions:
            print("Invalid direction from "+current_room+". Try again")
            direction = input("Direction to move?(East,West,North,South): ").title()
        
        # Setting next_room
        next_room = rooms[current_room][direction]
        print("You have just moved to",next_room)
        print("------------------------------------------------")
        
        # Updating current_room
        current_room = next_room
    
    # Printing end message
    print("Farewell Tarnished, shall you play again soon.")


# Calling main function
main()

