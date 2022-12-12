class Bus:
    def __init__(self, guest, max_guest=30):
        self.max_guest = max_guest
        self.cur_guest = guest
    def __del__(self):
        print("Bus클래스가 소멸되었습니다.")
    def __str__(self):
        return f"<Bus class {self.cur_guest}/{self.max_guest}>"
    def __lt__(self, target):
        return self.cur_guest < target.cur_guest
    def __le__(self, target):
        return self.cur_guest <= target.cur_guest
    def __eq__(self, target):
        return self.cur_guest == target.cur_guest
    def __ne__(self, target):
        return self.cur_guest != target.cur_guest
    def __gt__(self, target):
        return self.cur_guest > target.cur_guest
    def __ge__(self, target):
        return self.cur_guest >= target.cur_guest
    def geton(self, cnt):
        if self.max_guest > self.cur_guest + cnt:
            self.cur_guest += cnt
        return self.cur_guest

bus1 = Bus(25, 100)
bus2 = Bus(53, 300)
bus3 = Bus(23)
print(f"bus1 : {bus1}")
print(f"bus2 : {bus2}")
del bus3

print(f"bus1 < bus2 : {bus1 < bus2}")
print(f"bus1 <= bus2 : {bus1 <= bus2}")
print(f"bus1 == bus2 : {bus1 == bus2}")
print(f"bus1 != bus2 : {bus1 != bus2}")
print(f"bus1 > bus2 : {bus1 > bus2}")
print(f"bus1 >= bus2 : {bus1 >= bus2}")
