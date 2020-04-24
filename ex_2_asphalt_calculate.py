class Road():

    def __init__(self,length=1,width=1):
        self._length = length
        self._width = width

    def how_much_asphalt_need_if_thickness_is(self,thickness=1):
        square_metr = self._length*self._width
        result = (self._length*self._width)*(thickness)*(25/1000)
        print(f'For create {square_metr} m2 road,  needs {result} tons')

new_road = Road()


new_road.how_much_asphalt_need_if_thickness_is()

test_road = Road(20,5000)
test_road.how_much_asphalt_need_if_thickness_is(5)