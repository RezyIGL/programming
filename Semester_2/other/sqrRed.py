import SimpleGUICS2Pygame.simpleguics2pygame as sg

Giga_chad_cubes, W, H = [], 200, 200

def draw(canvas):
    for n in range(0, len(Giga_chad_cubes)):
        canvas.draw_polygon(Giga_chad_cubes[n], 1, "white", "green")
    
def mcl(pos):
    global Giga_chad_cubes
    for i in range(0, W+50, 50):
        for j in range(0, H+50, 50):
            if (i <= pos[0] <= i+49) and (j <= pos[1] <= j+49):
                x = [(i, j), (i+50, j), (i+50, j+50), (i, j+50)]
                if x in Giga_chad_cubes:
                    Giga_chad_cubes.remove(x)
                elif x not in Giga_chad_cubes:
                    Giga_chad_cubes.append(x)
                else:
                    print("Ты как это сделал?")
                    
frame = sg.create_frame("Tests", W, H)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mcl)

frame.start()
