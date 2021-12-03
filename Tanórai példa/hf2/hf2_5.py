room_surface = 75  # m^2
surface_per_paint_bucket = 15  # m^2
price_of_paint_bucket = 4300  # Ft
number_of_buckets = 2 * room_surface / surface_per_paint_bucket
price_of_buckets = number_of_buckets * price_of_paint_bucket  # Ft
print(price_of_buckets, "Ft értékben kell Tibornak festéket vásárolnia.")

minutes_per_surface = 13  # minutes/1 m^2
hours_per_surface = minutes_per_surface / 60  # hours/1 m^2
painter_net_price_per_hour = 2100  # Ft/hour
painting_time_of_twolayer = 2 * room_surface * hours_per_surface
painter_net_price_for_twolayer = painting_time_of_twolayer * painter_net_price_per_hour
print("A festő", painter_net_price_for_twolayer, "Ft nettó összegért festi ki Tibor szobáját 2 rétegben.")

afa = 0.27
painter_brutto_price_for_twolayer = painter_net_price_for_twolayer * (1 + afa)
print("A festő bruttó bére", painter_brutto_price_for_twolayer, "Ft.")

total_painting_price = painter_brutto_price_for_twolayer + price_of_buckets
print("A festés összesen", total_painting_price, "Ft-ba fog kerülni.")
