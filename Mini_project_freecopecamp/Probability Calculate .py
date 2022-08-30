import random
class Hat:
    # **balls Guarda toda la variable en una sola
    def __init__(self,**balls):
        self.contets = []
        for color_of_ball, quantity_bowl in balls.items():
            for qt_bowl in range(0,quantity_bowl):
               self.contets.append(color_of_ball)


    def draw(self,num_of_ball_draw):
        draw_balls = []
        list_contets = list(self.contets)

        if len(list_contets) > num_of_ball_draw:
             for draw_ball in range(0,num_of_ball_draw):
                 random_number = random.randrange(0, len(list_contets))
                 draw_balls.append(list_contets[random_number])
                 list_contets.pop(random_number)
        else:

            draw_balls = list(list_contets)

        return draw_balls
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M_count = 0
    n_count =num_experiments
    for exp in range(0,num_experiments):
        hat_list = list(hat.draw(num_balls_drawn))
        for color_ball ,value_ball in expected_balls.items():
            for num_of_time in range(0,value_ball):
                if  color_ball is  hat_list:
                    hat_list.pop(hat_list.index(color_ball))
            if hat_list.count(color_ball) == value_ball:
                M_count= M_count +1
    return M_count/n_count

hat2 = Hat(blue=4,red=2,green=3)
probability = experiment(hat=hat2,expected_balls={"blue": 2,"red": 1},num_balls_drawn=4,num_experiments=2000)
print("Probability:", probability)

