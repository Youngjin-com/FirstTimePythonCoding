class Bus:
    max_guest = 30
    cur_guest = 0
    def geton(self, cnt):
        if self.cur_guest + cnt <= self.max_guest:
            self.cur_guest += cnt
        return self.cur_guest

bus_1 = Bus()
bus_2 = Bus()
print(f"버스1에 {bus_1.geton(20)}명이 탑승했습니다")
print(f"버스2에 {bus_2.geton(30)}명이 탑승했습니다")
