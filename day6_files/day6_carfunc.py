#sample functions

moves_speed = 0
all_window = 0

def accelerate(moves_speed, gear):
    if gear == 1:
        moves_speed += 10
    elif gear == 2:
        moves_speed += 20
    elif gear == 3:
        moves_speed += 30
    elif gear == 4:
        moves_speed += 40

def car_window_down(all_window):
    if all_window <= 0:
        print("already down")
    else:
        all_window -= 5

