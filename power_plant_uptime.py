import math

def calculate_power_plant_uptime(total_capacity_mwh, daily_consumption_mwh, maintenance_days_per_year, days_in_year=365):
    """
    Calculates the estimated uptime of a power plant in days.

    Args:
        total_capacity_mwh (float): The total energy the plant can store or produce before needing maintenance/refueling.
        daily_consumption_mwh (float): The average energy consumed or supplied by the plant per day.
        maintenance_days_per_year (float): The total number of days allocated for maintenance or refueling per year.
        days_in_year (int): The total number of days in a year.

    Returns:
        int: The estimated number of days the plant can operate, rounded down.
    """

    # Calculate the theoretical maximum operating days based on capacity and consumption
    theoretical_operating_days = total_capacity_mwh / daily_consumption_mwh

    # Calculate the available days for operation after accounting for maintenance
    available_days_for_operation = days_in_year - maintenance_days_per_year

    # The actual operating days cannot exceed the available days for operation
    # and is also limited by the theoretical operating days.
    estimated_operating_days = min(theoretical_operating_days, available_days_for_operation)

    # The article emphasizes rounding down to ensure a conservative estimate.
    # This is crucial for planning and avoiding unexpected outages.
    return math.floor(estimated_operating_days)

# --- Example Usage ---

# Scenario 1: A large power plant with ample fuel and minimal maintenance
plant_a_capacity = 1000000  # MWh
plant_a_daily_use = 5000    # MWh/day
plant_a_maintenance = 30    # days/year
uptime_a = calculate_power_plant_uptime(plant_a_capacity, plant_a_daily_use, plant_a_maintenance)
print(f"Plant A Estimated Uptime: {uptime_a} days")

# Scenario 2: A smaller plant with higher daily consumption and more maintenance
plant_b_capacity = 500000   # MWh
plant_b_daily_use = 8000    # MWh/day
plant_b_maintenance = 60    # days/year
uptime_b = calculate_power_plant_uptime(plant_b_capacity, plant_b_daily_use, plant_b_maintenance)
print(f"Plant B Estimated Uptime: {uptime_b} days")

# Scenario 3: A plant where theoretical capacity limits uptime even with available days
plant_c_capacity = 100000   # MWh
plant_c_daily_use = 1000    # MWh/day
plant_c_maintenance = 10    # days/year (plenty of available days)
uptime_c = calculate_power_plant_uptime(plant_c_capacity, plant_c_daily_use, plant_c_maintenance)
print(f"Plant C Estimated Uptime: {uptime_c} days")
