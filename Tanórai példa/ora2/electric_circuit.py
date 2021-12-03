electric_current = 25  # A
network_voltage = 230  # V
maximum_power = electric_current * network_voltage
bulb_number = 5
bulb_power = 30  # W
airconditioner_power = 1500  # W
washing_machine_power = 1200  # W
iron_power = 2000  # W
already_used_power = bulb_power * bulb_number + airconditioner_power + washing_machine_power
power_with_iron = already_used_power + iron_power
print("Lekapcsol-e a megszakító:", power_with_iron > maximum_power)
