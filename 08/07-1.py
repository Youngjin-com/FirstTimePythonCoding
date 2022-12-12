import random

class Guest:
    def __init__(self, idx, max_floor):
        self.wait = True
        self.idx = idx
        self.to_floor = random.randint(1, max_floor)
        while True:
            self.from_floor = random.randint(1, max_floor)
            if self.from_floor != self.to_floor:
                break
        self.weight = random.randint(20, 120)
    def __str__(self):
        return f"<class Guest {self.idx} 대기:{self.wait} 목적:{self.to_floor} 시작:{self.from_floor} 무게:{self.weight} >"

class Elevator:
    def __init__(self, max_floor, max_weight=1000):
        self.max_weight = max_weight
        self.max_floor = max_floor
        self.current_weight = 0
        self.direction = "up"
        self.current_floor = 0
        self.guest_lists = []

    def move(self):
        if self.direction == "up":
            self.current_floor += 1
            if self.current_floor > self.max_floor:
                self.direction = "down"
                self.current_floor = self.max_floor
        else:
            self.current_floor -= 1
            if self.current_floor <= 1:
                self.direction = "up"
                self.current_floor = 1

    def get_in(self, guest):
        if self.current_weight + guest.weight < self.max_weight:
            self.current_weight += guest.weight
            self.guest_lists.append(guest)
        else:
            print("중량 초과!!")
    
    def get_off(self):
        get_off_list = []
        for x in reversed(range(len(self.guest_lists))):
            if self.guest_lists[x].to_floor == self.current_floor:
                guest = self.guest_lists.pop(x)
                self.current_weight -= guest.weight
                get_off_list.append(guest)
        return get_off_list

class Building:
    def __init__(self, floor_cnt, guest_cnt):
        self.max_floor = floor_cnt
        self.elevator = Elevator(self.max_floor)
        self.guests = [Guest(x, floor_cnt) for x in range(guest_cnt)]
    
    def work(self):
        self.elevator.move()
        for g in self.guests:
            if g.wait and g.from_floor == self.elevator.current_floor:
                g.wait = False
                self.elevator.get_in(g)
        self.elevator.get_off()
        self.output()
    
    def is_all_get_off(self):
        for g in self.guests:
            if g.wait:
                return False
        if len(self.elevator.guest_lists) > 0:
            return False
        return True

    def output(self):
        print("=" * 50)
        print(f"현재 엘레베이터 : {self.elevator.current_floor}층 방향: {self.elevator.direction}")
        print(f"현재 탑승: {len(self.elevator.guest_lists)}명  {self.elevator.current_weight}Kg")
        for g in self.elevator.guest_lists:
            print(f"\t{g.idx}번 손님 출발지: {g.from_floor}" \
                  f" 목적지: {g.to_floor}")

num_guest = int(input("생성될 승객 수를 입력하세요: "))
num_station = int(input("생성될 건물 층 수를 입력하세요: "))
print()
bd = Building(num_station, num_guest)

while not bd.is_all_get_off():
    bd.work()
