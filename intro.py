from player import Player

def intro() -> dict:
    """
    Displays introduction to the game, allows user to choose a name for their character, and displays initial character stats.
    
    Returns:
      dict: A dictionary containing the Player object and a boolean indicating whether to start the game.
    """

    TITLE = """
███████╗ ██████╗ ███████╗██╗███████╗███████╗    ██╗     ██╗███╗   ██╗███████╗
██╔════╝██╔═══██╗██╔════╝██║██╔════╝██╔════╝    ██║     ██║████╗  ██║██╔════╝
███████╗██║   ██║█████╗  ██║█████╗  ███████╗    ██║     ██║██╔██╗ ██║█████╗  
╚════██║██║   ██║██╔══╝  ██║██╔══╝  ╚════██║    ██║     ██║██║╚██╗██║██╔══╝  
███████║╚██████╔╝██║     ██║███████╗███████║    ███████╗██║██║ ╚████║███████╗
╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚══════╝    ╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝"""

    print(TITLE)
    print("\nIn a land ravaged by the rot of brain, one man ventures forth from the cave, searching of the light.")

    while True:
      player_name = input("And that brave soul's name was... > ")
      if player_name:
         break
      else:
         print("Please enter a name.")

    print(f"\nAh yes, of course. This is the story of {player_name}.")
    
    player_character = Player(player_name)
    player_character.show_stats()

    while True:
      start_game = input("\nAre you ready to begin your journey [y/n]?\n> ")
      if start_game in ("y", "n"):
         break
      else:
         print("Please enter 'y' or 'n'")
    
    return {"player": player_character, "start_game": start_game == "y"}