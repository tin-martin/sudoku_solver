import random
import collections
import copy
class Agent:
  def __init__(self,state):
    self.initialState = state
    self.state = copy.deepcopy(state)
  def checkSquare(self,xx,yy,state):
    nums = [0,0,0,0,0,0,0,0,0]
    for y in range(3):
      for x in range(3):
        X = x + xx;
        Y = y + yy;
        if(state[Y][X] >= 1):
          nums[state[Y][X]-1] += 1
        for j in nums:
          if(j>1):
            return False
    if(sum(nums) > 9):
      return False
    return True

  def checkColumn(self,x,state):
    nums = [0,0,0,0,0,0,0,0,0]
    for y in range(9):
      if(state[y][x] >= 1):
        nums[state[y][x]-1] += 1
      for j in nums:
        if(j>1):
          return False
    if(sum(nums) > 9):
      return False
    return True
      
  def checkRow(self,y,state):
    nums = [0,0,0,0,0,0,0,0,0]
    for x in range(9): 
      if(state[y][x] >= 1):
      
        nums[state[y][x]-1] += 1
      for j in nums:
        if(j>1):
          return False
 
    if(sum(nums) > 9):
      return False
    
    return True

  def isValid(self,state):
    for y in range(9):
      if not(self.checkRow(y,state)):
       # print("row")
        return False
    for x in range(9):
      if not (self.checkColumn(x,state)):
       # print("colun")
        return False
    for y in range(0,9,3):
      for x in range(0,9,3):
        if not(self.checkSquare(x,y,state)):
         # print("square")
          return False
    return True

  def find_empty_location(self,grid):
    for y in range(9):
      for x in range(9):
        if(grid[y][x] == 0):
          return y,x
  
  def print_grid(self,grid):
    for y in range(9):
      for x in range(9):
        print(grid[y][x],end="|")
      print()
     
  def solve(self,grid):
    isComplete = True
    for y in range(9):
      for x in range(9):
        if(grid[y][x] == 0):
          isComplete = False
    if(isComplete):
      return True
  
    y, x = self.find_empty_location(grid)

    for j in range(1,10):
      grid[y][x] = j
      if(self.isValid(grid)):
        if(self.solve(grid)):
          return True
      grid[y][x] = 0
    return False


    #if there is a 0, do other
    #else return True

    #find first zero


if __name__ == "__main__":
  grid = [[8,0,0,0,0,0,0,0,0],
 [0,0,3,6,0,0,0,0,0],
 [0,7,0,0,9,0,2,0,0],
 [0,5,0,0,0,7,0,0,0],
 [0,0,0,0,4,5,7,0,0],
 [0,0,0,1,0,0,0,3,0],
 [0,0,1,0,0,0,0,6,8],
 [0,0,8,5,0,0,0,1,0],
 [0,9,0,0,0,0,4,0,0]]

  agent = Agent(grid)
  agent.solve(grid)
  agent.print_grid(grid)
