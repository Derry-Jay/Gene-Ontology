import re
import decimal as dc


class MetricDistance:
    km = 0
    m = 0

    def __init__(self, *args):
        if len(args) == 1:
            if isinstance(args[0], str) and len(re.findall(".", args[0])) == 1:
                valist = args[0].split(".")
                self.km = int(valist[0])
                self.m = int(valist[1])
            elif isinstance(args[0], float) or isinstance(args[0], dc.Decimal):
                vl = str(round(args[0], 3)).split(".")
                self.km = int(vl[0])
                self.m = int(vl[1])

    def __eq__(self, value):
        return isinstance(value, MetricDistance) and self.km == value.km and self.m == value.m

    def __add__(self, value):
        sm = 0
        sk = 0
        if isinstance(value, MetricDistance):
            sm = self.m + value.m
            if sm > 999:
                sk += 1
                sm -= 1000
            sk += (self.km + value.km)
        return MetricDistance(round(float(sk + (sm/1000)), 3))

    def __sub__(self, value):
        dm = 0
        dk = 0
        if isinstance(value, MetricDistance):
            if self.km > value.km:
                dm = self.m - value.m
                if dm < 0:
                    dm += 1000
                    dk = self.km - (value.km + 1)
                else:
                    dk = self.km - value.m
            elif self.km == value.km:
                if self.m > value.m:
                    dm = self.m - value.m
        return MetricDistance(round(float(dk + (dm/1000)), 3))

    def __str__(self):
        return str(round(self.km + (self.m/1000), 3)) + " Kilometres"
