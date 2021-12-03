km_m = 1000
h_s = 3600
try:
    speed_km_h = float(input("Kérem adja meg a sebességet km/h-ban: "))
    speed_m_s = speed_km_h * 1000 / 3600
    print(f"A {speed_km_h} km/h sebesség az {speed_m_s} m/s-nak felel meg.")
except:
    print("Sajnálom, de nem tudom átváltani.")
