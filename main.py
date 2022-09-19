# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
gullit = 'Ruud Gullit '
van_basten = 'Marco van Basten '
goal_0 = 32
goal_1 = 54
scorers = gullit + str(goal_0) +', ' + van_basten + str(goal_1)
report = f'{gullit}scored in the {goal_0}nd minute\n{van_basten}scored in the {goal_1}th minute'
print(report)
player = 'Adri van Tiggelen'
first_name = player[0:player.find(' ')]
last_name_len = len(player[player.find('v'):])
name_short = player[0] + '.' + player[player.find(' '):]
chant = ((first_name + "! ") * len(first_name))[0:-1]
good_chant = chant != ' '