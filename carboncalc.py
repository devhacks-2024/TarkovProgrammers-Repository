def calculate_house_co2_emissions(electricity_kwh, natural_gas_kwh, heating_oil_liters, coal_metric_tons, lpg_liters, propane_liters, wooden_pellets_metric_tons):

    emission_factors = {
        'electricity': 0.002,  # in kgCO2e/kWh
        'natural_gas': 0.203,  # in kgCO2e/kWh
        'heating_oil': 2.52,   # in kgCO2e/liter
        'coal': 2916.47,       # in kgCO2e/metric ton
        'lpg': 1.49,           # in kgCO2e/liter
        'propane': 1.49,       # in kgCO2e/liter
        'wooden_pellets': 113.14  # in kgCO2e/metric ton
    }
    electicity = electricity_kwh * emission_factors['electricity']
    natural_gas = natural_gas_kwh * emission_factors['natural_gas']
    heating_oil = heating_oil_liters * emission_factors['heating_oil']
    coal = coal_metric_tons * emission_factors['coal']
    lpg = lpg_liters * emission_factors['lpg']
    propane = propane_liters * emission_factors['propane']
    emission = wooden_pellets_metric_tons * emission_factors['wooden_pellets']
    total_co2 = (electicity + natural_gas + heating_oil + coal + lpg + propane + emission)
    
    total_co2_metric_tons = total_co2 / 1000

    return electicity, natural_gas, heating_oil, coal, lpg, propane, emission, total_co2_metric_tons

total_co2_emissions = calculate_house_co2_emissions( electricity_kwh=1, natural_gas_kwh=1, heating_oil_liters=1, coal_metric_tons=1, lpg_liters=1, propane_liters=1, wooden_pellets_metric_tons=1)
print(total_co2_emissions)

def calculate_flight_co2_emissions(flight_distance_km):
    RADIATIVE_FORCING_MULTIPLIER = 2
    fuel_consumption = (flight_distance_km*3)/100
    co2_emission = fuel_consumption*2.5
    total_impact_in_metric = (co2_emission*RADIATIVE_FORCING_MULTIPLIER)/1000
    return total_impact_in_metric
total_co2_flight = calculate_flight_co2_emissions(1505)
print(total_co2_flight)

def calculate_car_co2_emissions(distance_km, fuel_efficiency_100km_liter, fuel_type):
    if fuel_type == "gasoline" or fuel_type == "petrol":
        emission_factor = 2.31
    elif fuel_type == "diesel":
        emission_factor = 2.68
    else:
        return "Unsupported fuel type"
    fuel_consumption = (distance_km * fuel_efficiency_100km_liter) / 100
    co2_emission = fuel_consumption * emission_factor
    total_impact_in_metric = co2_emission / 1000
    return total_impact_in_metric

total_co2_car = calculate_car_co2_emissions(100, 5, "gasoline")
print(total_co2_car)
