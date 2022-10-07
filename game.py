import sys
try:
    import time,keyboard
    class sprite:
        def __init__(self):
            self.x = 2
            self.y = 3
            self.jump = False
            self.image = "!"
        def change_image(self,char):
            if len(char) == 1:
                self.image = char
        
    player = sprite()

    grid_map = (
        (0,0,0,0,0),
        (0,0,0,0,0),
        (0,0,0,0,0),
        (0,0,2,0,0),
        (1,1,1,1,1)
    )
    key_0 = " "
    key_1 = "-"
    HEIGHT = len(grid_map)-1
    WIDTH = len(grid_map[0])-1
    for line in grid_map:
        x_line = ""
        for item in line:
            if item == 0:
                x_line += key_0
            elif item == 1:
                x_line += key_1
            elif item == 2:
                x_line += player.image
        print(x_line)
    run = True
    counter = 0
    while run:
        grid_prev = grid_map
        if keyboard.is_pressed("space"):
            if counter > 100 and player.jump == False and grid_map[player.y+1][player.x] == 1:
                counter = 0
                player.jump = True
                player.y -= 1
            else:
                input("FOOOOOl")
            grid_map[player.y][player.x] = 2 

        if grid_map[player.y-1][player.x] != 1 and player.jump == False:
            player.y += 1

        if grid_prev != grid_map:
            for line in grid_map:
                x_line = ""
                for item in line:
                    if item == 0:
                        x_line += key_0
                    elif item == 1:
                        x_line += key_1
                    elif item == 2:
                        x_line += player.image
                print(x_line)
        counter += 1
except:
    type,value,extra = sys.exc_info()
input(type,value,extra)