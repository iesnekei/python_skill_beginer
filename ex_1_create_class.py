from time import sleep
class TrafficLight():

    __color = 'red'

    def running(self):
        prev_color = self.__color

        while True:
            prev_color = self.__color
            print(prev_color)
            sleep(7)

            if prev_color == 'red':
                prev_color = 'yellow'

            else:
                print('Colors order is wrong!')
                break

            print(prev_color)
            sleep(2)

            if prev_color == 'yellow':
                prev_color = 'green'
            else:
                print('Colors order is wrong!')
                break

            print(prev_color)
            sleep(4)




first_Tl = TrafficLight()

first_Tl.running()