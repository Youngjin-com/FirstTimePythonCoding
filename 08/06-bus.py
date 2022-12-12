import random

num_guest = int(input("생성될 승객 수를 입력하세요: "))
num_station = int(input("생성될 정류장 갯수를 입력하세요: "))

class Guest:
    def __init__(self, idx, station):
        self.get_off = False
        self.idx = idx
        self.start_station = random.randint(0, station)
        while True:
            self.end_station = random.randint(0, station)
            if self.end_station != self.start_station:
                break

class Bus:
    def __init__(self, end_station, station):
        self.end_station = end_station
        self.current_station = station
        self.move_direction = "right"
        self.guest_list = []

    def move_bus(self):
        if self.move_direction == "right":
            self.current_station += 1
            if self.current_station >= self.end_station:
                self.move_direction = "left"
        else:
            self.current_station -= 1
            if self.current_station <= 0:
                self.move_direction = "right"

    def get_in_bus(self, guest):
        self.guest_list.append(guest)
    
    def get_off_bus(self):
        get_off_list = []
        for x in reversed(range(len(self.guest_list))):
            if self.guest_list[x].end_station == self.current_station:
                guest = self.guest_list.pop(x)
                guest.get_off = True
                get_off_list.append(guest)
        return get_off_list

class Line:
    def __init__(self, station_cnt, guest_cnt):
        self.guest_count = guest_cnt
        self.guests = [Guest(x, station_cnt) for x in range(guest_cnt)]
        self.get_off_list = []
        self.station_count = station_cnt
        self.bus = Bus(station_cnt, random.randint(0, self.station_count))
    
    def main(self):
        self.bus.move_bus()
        for i, p in enumerate(self.guests):
            if not p.get_off and p.start_station == self.bus.current_station:
                guest = self.guests.pop(i)
                self.bus.get_in_bus(guest)
        self.get_off_list.extend(self.bus.get_off_bus())
        self.output()
    
    def is_all_get_off(self):
        return len(self.get_off_list) == self.guest_count
    
    def output(self):
        print("=" * 50)
        print(f"현재 정류장 : {self.bus.current_station}")
        print(f"현재 버스 탑승 손님 : {len(self.bus.guest_list)}")
        for p in self.bus.guest_list:
            print(f"\t{p.idx}번 손님 출발지: {p.start_station}" \
                  f" 목적지: {p.end_station}")

print()
line = Line(num_station, num_guest)
while not line.is_all_get_off():
    line.main()
