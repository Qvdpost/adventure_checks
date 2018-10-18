import check50

# Template for checks:
'''

@check50.check()
def test_name():
    """
    Test message.
    """
    check50.run(run_command)

'''

run_command = "python3 adventure.py"

room_1_description = "You are standing at the end of a road before a small brick building.  A small stream flows out of the building and down a gully to the south.  A road runs up a small hill to the west."
room_1_name = "Outside building"

room_2_name = "End of road"
room_2_description = "You are at the end of a road at the top of a small hill. You can see a small building in the valley to the east."

room_3_name = "Inside building"
room_3_description = "You are inside a building, a well house for a large spring. The exit door is to the south.  There is another room to the north, but the door is barred by a shimmering curtain.\nKEYS: a set of keys"

room_14_description = "You are in a splendid chamber thirty feet high.  The walls are frozen rivers of orange stone.  A narrow canyon and a good passage exit from east and west sides of the chamber."
room_15_description = "You are in a splendid chamber thirty feet high.  The walls are frozen rivers of orange stone.  A narrow canyon and a good passage exit from east and west sides of the chamber. High in the cavern, you see a little bird flying around the rocks.  It takes one look at the black rod and quickly flies out of sight."
@check50.check()
def exists():
    """
    Checking if all files exist.
    """
    # check50.include("data/CrowtherRooms.txt")
    # check50.include("data/CrowtherItems.txt")

    check50.exists("adventure.py")
    check50.exists("room.py")
    check50.exists("inventory.py")
    check50.exists("item.py")

@check50.check(exists)
def moving_around():
    """
    Moving around
    """
    check50.run(run_command).stdout(room_1_description)
    check50.run(run_command).stdin("west").stdout(room_2_description)
    check50.run(run_command).stdin("WEST").stdout(room_2_description)
    check50.run(run_command).stdin("west").stdin("east").stdout(room_1_name)

@check50.check(moving_around)
def commands():
    """
    Test if program accepts user commands.
    """
    check50.run(run_command).stdin("yolo").stdout("Invalid command.").stdin("west").stdout(room_2_description)

@check50.check(commands)
def helper_commands():
    """
    Testing helper commands.
    """
    check50.run(run_command).stdin("help").stdout(
        "You can move by typing directions such as EAST/WEST/IN/OUT\n" +
        "QUIT quits the game.\n" +
        "HELP prints instructions for the game.\n" +
        "INVENTORY lists the item in your inventory.\n" +
        "LOOK lists the complete description of the room and its contents.\n" +
        "TAKE <item> take item from the room.\n" +
        "DROP <item> drop item from your inventory.\n"
        )
    check50.run(run_command).stdin("look").stdout(room_1_description)
    check50.run(run_command).stdin("quit").stdout("Thanks for playing!").exit(0)

@check50.check(helper_commands)
def items():
    """
    Test message.
    """
    check50.run(run_command).stdin("in").stdout("You are inside a building, a well house for a large spring. The exit door is to the south.  There is another room to the north, but the door is barred by a shimmering curtain.\nKEYS: a set of keys\nWATER: a bottle of water")
    check50.run(run_command).stdin("in").stdin("out").stdin("in").stdin("look").stdout("KEYS: a set of keys\nWATER: a bottle of water")
    check50.run(run_command).stdin("in").stdin("take keys").stdout("KEYS taken.")
    check50.run(run_command).stdin("in").stdin("take keys").stdin("out").stdin("drop keys").stdout("KEYS dropped.")

@check50.check(items)
def conditional_move():
    """
    Testing conditional movements.
    """
    check50.run(run_command).stdin("in").stdin("take keys").stdin("out").stdin("down\ndown\ndown\ndown").stdout("You are in a small chamber beneath a 3x3 steel grate to the surface.  A low crawl over cobbles leads inward to the west.\nLAMP: a brightly shining brass lamp")
    # Check for move with multiple conditions.
    check50.run(run_command).stdin("IN\nTAKE KEYS\nOUT\nDOWN\nDOWN\nDOWN\nDOWN\nTAKE LAMP\nIN\nWEST\nWEST\nWEST\nTAKE BIRD\nWEST\nDOWN\nSOUTH\nTAKE NUGGET\nOUT\nDROP NUGGET\nUP\nEAST\nEAST\nEAST\nTAKE ROD\nWEST\nWEST\nLOOK\n").stdout(room_14_description).stdin("EAST\nDROP BIRD\nWEST\nLOOK\n").stdout(room_15_description)

@check50.check(conditional_move)
def forced_move():
    """
    Testing for forced movements.
    """
    check50.run(run_command).stdin("down\ndown\ndown\ndown").stdout("The grate is locked and you don't have any keys.\nOutside grate")

@check50.check(forced_move)
def won():
    """
    Testing win condition.
    """
    check50.run(run_command).stdin("IN\nTAKE KEYS\nOUT\nDOWN\nDOWN\nDOWN\nDOWN\nTAKE LAMP\nIN\nWEST\nWEST\nWEST\nTAKE BIRD\nWEST\nDOWN\nSOUTH\nTAKE NUGGET\nOUT\nDROP NUGGET\nUP\nEAST\nEAST\nEAST\nTAKE ROD\nWEST\nWEST\nWEST\nDOWN\nTAKE NUGGET\nWEST\nWAVE\nTAKE DIAMOND\nWEST\nSOUTH\nSOUTH\nEAST\nNORTH\nNORTH\nTAKE CHEST\nOUT\nWEST\nDOWN\nWEST\nDOWN\nNORTH\nEAST\nTAKE COINS\nOUT\nNORTH\nDOWN\nEAST\nDROP LAMP\nDROP BIRD\nDROP NUGGET\nDROP COINS\nNORTH\nTAKE EMERALD\nOUT\nTAKE LAMP\nTAKE BIRD\nTAKE NUGGET\nTAKE COINS\nWEST\nWEST\nWEST\nDOWN\nWATER\nTAKE EGGS\nNORTH\nDOWN\nOUT\nEAST\nEAST\nEAST\nUP\nSOUTH\nSOUTH\nWEST\nWAVE\nWEST\nSOUTH\nNORTH\nNORTH\nEAST\nDOWN\nEAST\nEAST\nXYZZY\nNORTH\n").stdout("You have collected all the treasures and are admitted to the Adventurer's Hall of Fame.  Congratulations!").exit(0)
