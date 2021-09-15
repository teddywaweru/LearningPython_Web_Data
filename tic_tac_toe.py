
print(' 0  1  2')#Print the number of columns on the game


# #Define the scope of the game.
# ttt_game =  [[0,0,0],
#             [0,0,0],
#             [0,0,0]]

# player_no = 1

    
# def play_turn(player_no, col,row):
#     try:
#         ttt_game[row][col] = player_no
#         winning(ttt_game)

#     except IndexError as e:
#         print("Something went wrong.")
#         print(ttt_game)



# def winning(ttt_game):
#     #Win via rows
#     for row in ttt_game:
#         #compare count of first value against length of row to know if all values are identical
#         if row[0] != 0 and row.count(row[0]) ==len(row): 
#             print('You win the game, {}!'.format(player_no)) 

#     #Win via Columns
#     for col in range(len(ttt_game)):#Iterate through the number of columns
#         col_values = [] #Create blank list to hold values in columns for comparison 
#         for row in ttt_game:
#             #Append the row value based on the Column count ie,, al 0s,or all 1s, or all 2s
#             col_values.append(row[col])
#             #Compare list against length to check or Winner.
#     if col_values[0] != 0 and col_values.count(col_values) == len(col_values):
#         print('You win the game, {}!'.format(player_no)) 

#     #Win via Diagonals
#     #For simpler Diagonal, where indices match
#     for index in range(len(ttt_game)):
#         diag_values = []
#         diag_values.append(ttt_game[index][index])

#     #For Diagonal with varying index values - complex diagonal
#     '''iterate between len of col/rows in ascending & descending order.
#     Store value for confirmation
#     '''

#     row_index = []
#     diag_values = []
#     for row in range(len(ttt_game)):
#         print(row)
#         row_index.append(row)
#     col_index  = reversed(row_index)
#     for row_index,col_index in zip(row_index,col_index):
#         print (row_index,col_index)
#         diag_values.append(ttt_game[row_index][col_index])
#         print(diag_values)


#     row_index = []
#     for row in range(len(ttt_game)):
#         row_index.append(row)
#     col_index = reversed(row_index)

#     diag_values = []
#     for row_index,col_index in zip(row_index,col_index):
#         diag_values.append(ttt_game[row_index][col_index])

#                     #Simplified Version using enumeration & Reversibility

#                     # for row,col in enumerate(reversed(range(len(ttt_game)))):
#                     #     print(row,col)

# col = int(input(print("Player {}. It is your turn. Provide Column Number /n.".format(player_no))))
# row = int(input(print("Player {}, now provide Row Number /n.".format(player_no))))

# play_turn(player_no,col,row)

# print('   0  1  2')#Print the number of columns on the game
# for rows,ttt_values in enumerate(ttt_game):
#     print(rows, ttt_values) #print row enumeration & ttt_game values per row


player = [1,0]
choice = 1
for i in range (10):
    current_player = choice + 1
    print(current_player)
    choice = player[choice]
