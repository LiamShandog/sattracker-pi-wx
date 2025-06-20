# get noaa 19's position

from skyfield.api import load, wgs84

def get_noaa19_position(norad_id=33591, lat=45.255383, lon=-75.924449):
    # load all current satellite TLE data
    url = 'https://celestrak.org/NORAD/elements/weather.txt'
    satellites = load.tle_file(url)

    # find the NOAA 19 satellite by NORAD ID
    target = None
    for sat in satellites:
        if sat.model.satnum == norad_id:
            target = sat
            break
    
    if not target:
        raise ValueError("Satellite not found :(")
    
    # define observer'a location
    observer = wgs84.latlon(lat, lon)

    # Get current time
    ts = load.timescale()
    t = ts.now()

    # calculate satellite position from observer's location
    difference = target - observer
    topocentric = difference.at(t)
    alt, az, distance = topocentric.altaz()

    # outputs the altitude above the horizon, azimuth (0 = north, 90 = east, 180 = south, 270 = west), and distance in km
    return alt.degrees, az.degrees, distance.km

if __name__ == "__main__":
    alt, az, distance = get_noaa19_position()
    print(f"NOAA 19 Position:\nAltitude: {alt} degrees\nAzimuth: {az} degrees\nDistance: {distance} km")