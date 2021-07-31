import math
import decimal as dc
from models.latlong import LatLong


class Calculations:
    def haversine(self, a, b):
        d = dc.Decimal(0.000)
        print(d)
        if isinstance(a, LatLong) and isinstance(b, LatLong):
            dLat = (abs(a.lat - b.lat) * dc.Decimal(11)) / dc.Decimal(630)
            sLat = (abs(a.lat + b.lat) * dc.Decimal(11)) / dc.Decimal(630)
            dLong = (abs(a.lon - b.lon) * dc.Decimal(11)) / dc.Decimal(630)
            # self.lat = (a.lat * dc.Decimal(11)) / dc.Decimal(630)
            # c.lat = (b.lat * dc.Decimal(11)) / dc.Decimal(630)
            f = (1+math.cos(sLat)-(math.cos(dLong) *
                 (math.cos(sLat)+math.cos(dLat))))/2
            d = round(12742 * math.asin(math.sqrt(f)), 3)
        return d
