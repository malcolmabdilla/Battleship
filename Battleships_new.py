from random import randint

board = []
ships = []
score = 0
win = False

for x in range(0, 10):
  board.append(["O"] * 10)

def print_board(board):
  for row in board:
    print ((" ").join(row))

def generate_coords():
  coord = []
  row = randint(0,len(board) -1)
  col = randint(0,len(board) -1)
  coord.append(row)
  coord.append(col)
  return coord

def gen_coords():
  found = False
  coords = generate_coords()
  if not ships:
    return coords
  else:
    for x in ships:
      if x == coords:
        found = True
    if found == True:
      return gen_coords()
    else:
      return coords

def aoe(guess_coord):
  print ('Ship Sank')
  
  board[guess_coord[0]][guess_coord[1]] = 'H'
  nw = [guess_coord[0]-1, guess_coord[1]-1]
  n = [guess_coord[0]-1, guess_coord[1]]
  ne = [guess_coord[0]-1, guess_coord[1]+1]
  w = [guess_coord[0], guess_coord[1]-1]
  e = [guess_coord[0], guess_coord[1]+1]
  sw = [guess_coord[0]+1, guess_coord[1]-1]
  s = [guess_coord[0] +1, guess_coord[1]]
  se = [guess_coord[0]+1, guess_coord[1]+1]
  
  affct = [nw,n,ne,w,e,sw,s,se]

  for i in affct:
    if int(-1) in i or int(10) in i:
      None
    elif board[i[0]][i[1]] == 'H':
      None
    elif i in ships:
      score =+ 1
      aoe(i)
    else:
      board[i[0]][i[1]] = 'X'
      
  
    
for x in range(10):
  ships.append(gen_coords())



for turn in range(20):
  if turn == 19:
    print ('Game Over\nScore: '+str(score))
  elif win == True:
    break
  else:
    print("Turn", turn + 1)
    ex = False
    while ex == False:
      print_board(board)
      Hit = False
      guess_row = input("Guess Row: ")
      guess_col = input("Guess Col: ")

      if guess_row not in [str(x) for x in range(10)] or guess_col not in [str(x) for x in range(10)]:
        print('Wrong Input')
      else:
        guess_row = int(guess_row)
        guess_col = int(guess_col)
        guess_coord = [guess_row,guess_col]
        
        if board[guess_row][guess_col] == 'H' or board[guess_row][guess_col] == 'X':
          print ('Location already fired at')
          ex = True
        else:
          for x in ships:
            if guess_coord == x:
              Hit = True
              break
            else:
              Hit = False
        
          if Hit ==  True:
            aoe(guess_coord)
            if score == 10:
              print ('Congratulations you won')
              win = True
              break     
          else:
            print('Miss')
            board[guess_row][guess_col] = 'X'
            ex = True
      

  '''
        
      
      
      
      
  if guess_row == ship_row and guess_col == ship_col:
    print ("Congratulations! You sank my battleship!")
  else:
    if guess_row not in range(10) or \
      guess_col not in range(10):
      print ("Oops, that's not even in the ocean.")
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
    else:
      print ("You missed my battleship!")
      board[guess_row][guess_col] = "X"
    print_board(board)
  if turn == 3:
    print ("Game Over")
'''

