class Bus:
    def __init__(self, guest, max_guest=30):
        self.max_guest = max_guest
        self.cur_guest = guest
        self.price = 0
    def __str__(self):
        return f"<Bus class {self.cur_guest}/{self.max_guest}" \
               f" {self.price}>"
    def geton(self, cnt):
        if self.max_guest > self.cur_guest + cnt:
            self.cur_guest += cnt
        return self.cur_guest

class VillageBus(Bus):
    def __init__(self, guest):
        self.price = 1000
        self.max_guest = 16
        self.cur_guest = guest
    def geton(self, cnt):
        self.cur_guest += cnt
        return self.cur_guest

vbus = VillageBus(10)
vbus.geton(10)
print(vbus)
