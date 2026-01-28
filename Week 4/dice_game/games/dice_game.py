class DiceGame:
  def __init__(self):
    self.turn = 1
    self.point = None
    self.finished = False
    self.result = ""
    
  def validate_roll(self, roll):
    if roll < 2 or roll > 12:
      raise ValueError("Dice roll must be between 2 and 12")

  def play_turn(self, roll):
    if self.finished:
      return
    
    self.validate_roll(roll)
      
    if self.turn == 1:
      if roll in (2, 3, 12):
        self.result = f"Turn {self.turn}: Rolled {roll}. You lose."
        self.finished = True
            
      elif roll in (7, 11):
        self.result = f"Turn {self.turn}: Rolled {roll}. You win!"
        self.finished = True
          
      else:
        self.point = roll
        self.result = f"Turn {self.turn}: Rolled {roll}. Point is set to {self.point}."
        self.turn += 1
            
    else:
      if roll == 7:
        self.result = f"Turn {self.turn}: Rolled {roll}. You lose."
        self.finished = True
      elif roll == self.point:
        self.result = f"Turn {self.turn}: Rolled {roll}. You win!"
        self.finished = True
      else:
        self.result = f"Turn {self.turn}: Rolled {roll}. No result, keep rolling."
        self.turn += 1