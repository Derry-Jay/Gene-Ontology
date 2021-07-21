import math
import decimal as dc
import pgeocode as pgc


class LatLong:
    lat = dc.Decimal(0.0)
    lon = dc.Decimal(0.0)

    def __init__(self, *args):
        if args != () and len(args) == 2:
            self.lat = args[0] if args[0] is dc.Decimal else dc.Decimal(
                args[0])
            self.lon = args[1] if args[1] is dc.Decimal else dc.Decimal(
                args[1])

    def putToDict(self):
        d = {'latitude': str(self.lat), 'longitude': str(self.lon)}
        return d

    def belongs_to(self, ll):
        flag = False
        for i in ll:
            if self.lat == i.lat and self.lon == i.lon:
                flag = True
                break
        return flag

    def haversine(self, c):
        d = 0.0
        if isinstance(c, LatLong):
            pi = dc.Decimal(math.pi)
            ro = dc.Decimal(180.0)
            dLat = abs(self.lat - c.lat) * pi / ro
            dLon = abs(self.lon - c.lon) * pi / ro
            self.lat = self.lat * pi / ro
            c.lat = c.lat * pi / ro
            f = (pow(math.sin(dLat / 2), 2) +
                 pow(math.sin(dLon / 2), 2) *
                 math.cos(self.lat) * math.cos(c.lat))
            d = 12742 * math.asin(math.sqrt(f))
        return d

    def getLatLongFromListOrTuple(self, t):
        if t != [] and t != () and len(t) == 2:
            self.lat = t[0] if t[0] is dc.Decimal else dc.Decimal(t[0])
            self.lon = t[1] if t[1] is dc.Decimal else dc.Decimal(t[1])

    def getLatLongFromDict(self, a):
        if 'latitude' in a.keys() and 'lonitude' in a.keys():
            self.lat = a['latitude'] if a['latitude'] is dc.Decimal else dc.Decimal(
                a['latitude'])
            self.lon = a['longitude'] if a['longitude'] is dc.Decimal else dc.Decimal(
                a['longitude'])
        elif 'latitude' in a.keys():
            self.lat = a['latitude'] if a['latitude'] is dc.Decimal else dc.Decimal(
                a['latitude'])
        elif 'longitude' in a.keys():
            self.lon = a['longitude'] if a['longitude'] is dc.Decimal else dc.Decimal(
                a['longitude'])

    def getLatLongFromZipCodeAndCountryCode(self, z, c):
        if z is not None and c is not None and z != "" and c != "":
            place = pgc.Nominatim(c)
            l = place.query_postal_code(z).dropna()
            return l.to_dict()
        else:
            return {}

    def getLatLongFromZipCode(self, m):
        g = []
        for i in pgc.COUNTRIES_VALID:
            place = pgc.Nominatim(i)
            if m != None and m != '':
                l = place.query_postal_code(m).dropna()
                x = l.to_dict()
                if 'latitude' in x.keys() and 'longitude' in x.keys():
                    ao1 = LatLong(x['latitude'], x['longitude'])
                    if not(ao1.belongs_to(g)):
                        g.append(ao1)
                    else:
                        continue
                else:
                    continue
            else:
                continue
        return g

    def putData(self):
        print("++++++++++++++++++++++++++++++++++++++++")
        lats = ""
        longs = ""
        if self.lat > 0:
            lats = " N"
        elif self.lat < 0:
            lats = " S"
        print("Latitude: " + str(abs(self.lat)) + lats)
        print("-----------------------------------------")
        if self.lon > 0:
            longs = " E"
        elif self.lon < 0:
            longs = " W"
        print("Longitude: " + str(abs(self.lon)) + longs)
        print("++++++++++++++++++++++++++++++++++++++++")

    def getLatLongFromZipCodeAndPutToDict(self, z):
        lldl = []
        lll = self.getLatLongFromZipCode(z)
        for i in lll:
            lldl.append(i.putToDict())
        return lldl
