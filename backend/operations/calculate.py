import math
import decimal as dc
from operations.latlong import LatLong


class Calculations:
    def haversine(self, a, b):
        d = 0.0
        if isinstance(a, LatLong) and isinstance(b, LatLong):
            print("Hi")
            dLat = (abs(a.lat - b.lat) * dc.Decimal(11)) / dc.Decimal(630)
            dLong = (abs(a.lon - b.lon) * dc.Decimal(11)) / dc.Decimal(630)
            lart1 = (a.lat * dc.Decimal(11)) / dc.Decimal(630)
            lart2 = (b.lat * dc.Decimal(11)) / dc.Decimal(630)
            f = (pow(math.sin(dLat / 2), 2) +
                 pow(math.sin(dLong / 2), 2) *
                 math.cos(lart1) * math.cos(lart2))
            d = 12742 * math.asin(math.sqrt(f))
        else:
            print("Bye")
            d = 0.0
        return d
