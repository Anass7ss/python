class player:
    def __init__(self):
        self.name="adam"
        self.symbol="x"
    def choose_name(self):
      while True:
        name=input("enter your name(letters only):")
        if name.isalpha():
            self.name=name
            break
        print("Invalid name.please use letters only.")
    def choose_symbol(self):
       while True: 
          symbol=input(f"{self.name},choose your symbol(a singlr letter):")
          if symbol.isalpha()and len(symbol)==1:
             self.symbol=symbol.upper()
             break
          print("invalid symbol.please choose a single letter.")
class menu:
   def display_main_menu(self):
      print("welcome to my x_o game!")
      print("1.start the game")
      print("2.quit the game")
      choice=input("enter your choice (1 Or  2):")
      return choice
   def display_end_game(self):
      menu_text="""
      game over!
      1.restart the game
      2.quit the game
      enter your choice(1 or 2)"""
      choice= input(menu_text)
      return choice
