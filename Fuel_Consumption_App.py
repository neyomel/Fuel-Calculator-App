import streamlit as st

st.title("🚗 Fuel Calculator App")
st.write("If you can see this, Streamlit is working.")
# =========================================================
# ADVANCED FUEL RANGE CALCULATOR
# =========================================================
# FEATURES:
# - Welcome menu
# - Built-in car database
# - Add new cars
# - Delete cars from database
# - View database
# - Safety margin / margin of error
# - Fuel percentage calculations
# - Remaining fuel calculations
# =========================================================

car_database = {

    "2011 Hyundai i10": {
        "km_per_liter": 16,
        "tank_capacity": 35
    },

    "2015 Toyota Vios": {
        "km_per_liter": 14,
        "tank_capacity": 42
    },

    "2018 Honda Civic": {
        "km_per_liter": 12,
        "tank_capacity": 47
    },

    "2020 Mitsubishi Mirage": {
        "km_per_liter": 18,
        "tank_capacity": 35
    }
}


# =========================================================
# DISPLAY DATABASE
# =========================================================

def display_database():

    if len(car_database) == 0:
        print("\n⚠️ No cars in database.\n")
        return

    print("\n========== CURRENT CAR DATABASE ==========")

    for index, car in enumerate(car_database, start=1):

        data = car_database[car]

        print(f"{index}. {car}")

        print(f"   Fuel Economy : "
              f"{data['km_per_liter']} km/L")

        print(f"   Tank Capacity: "
              f"{data['tank_capacity']} L\n")


# =========================================================
# ADD CAR
# =========================================================

def add_car():

    print("\n========== ADD NEW CAR ==========")

    car_name = input("Enter car model and year: ")

    km_per_liter = float(
        input("Enter fuel economy (km/L): ")
    )

    tank_capacity = float(
        input("Enter tank capacity (L): ")
    )

    car_database[car_name] = {
        "km_per_liter": km_per_liter,
        "tank_capacity": tank_capacity
    }

    print("\n✅ Car added successfully!\n")


# =========================================================
# DELETE CAR
# =========================================================

def delete_car():

    if len(car_database) == 0:
        print("\n⚠️ Database is empty.\n")
        return

    print("\n========== DELETE CAR ==========")

    display_database()

    try:

        choice = int(
            input("Select car number to delete: ")
        )

        car_names = list(car_database.keys())

        selected_car = car_names[choice - 1]

        confirm = input(
            f"Are you sure you want to delete "
            f"{selected_car}? (y/n): "
        ).lower()

        if confirm == "y":

            del car_database[selected_car]

            print(f"\n✅ {selected_car} deleted successfully.\n")

        else:
            print("\nDeletion cancelled.\n")

    except:
        print("\n⚠️ Invalid selection.\n")


# =========================================================
# CALCULATE TRIP
# =========================================================

def calculate_trip():

    if len(car_database) == 0:
        print("\n⚠️ No cars in database.\n")
        return

    display_database()

    try:

        # Select car
        choice = int(
            input("Select a car number: ")
        )

        car_names = list(car_database.keys())

        selected_car = car_names[choice - 1]

        car = car_database[selected_car]

        km_per_liter = car["km_per_liter"]

        tank_capacity = car["tank_capacity"]

        # Current fuel
        current_fuel = float(
            input("\nEnter current fuel (L): ")
        )

        # Distance needed
        distance_needed = float(
            input("Enter distance to travel (km): ")
        )

        # =================================================
        # SAFETY MARGIN
        # =================================================
        # Reduce fuel economy by 10%
        # to account for:
        # - traffic
        # - aircon
        # - bad roads
        # - driving habits
        # =================================================

        safety_margin = 0.90

        adjusted_km_per_liter = (
            km_per_liter * safety_margin
        )

        # =================================================
        # CALCULATIONS
        # =================================================

        max_distance = (
            current_fuel *
            adjusted_km_per_liter
        )

        fuel_needed = (
            distance_needed /
            adjusted_km_per_liter
        )

        remaining_fuel = (
            current_fuel - fuel_needed
        )

        # =================================================
        # PERCENTAGES
        # =================================================

        current_fuel_percent = (
            current_fuel / tank_capacity
        ) * 100

        fuel_used_percent = (
            fuel_needed / tank_capacity
        ) * 100

        remaining_percent = (
            remaining_fuel / tank_capacity
        ) * 100

        # =================================================
        # OUTPUT
        # =================================================

        print("\n=================================================")
        print(f"CAR: {selected_car}")
        print("=================================================")

        print(f"Official Fuel Economy : "
              f"{km_per_liter:.2f} km/L")

        print(f"Safety Adjusted Economy (-10%) : "
              f"{adjusted_km_per_liter:.2f} km/L")

        print(f"\nTank Capacity : "
              f"{tank_capacity:.2f} L")

        print(f"Current Fuel : "
              f"{current_fuel:.2f} L "
              f"({current_fuel_percent:.2f}%)")

        print(f"\nDistance Needed : "
              f"{distance_needed:.2f} km")

        print(f"Estimated Fuel Needed : "
              f"{fuel_needed:.2f} L "
              f"({fuel_used_percent:.2f}%)")

        print(f"\nEstimated Remaining Fuel : "
              f"{remaining_fuel:.2f} L "
              f"({remaining_percent:.2f}%)")

        print(f"Maximum Safe Distance : "
              f"{max_distance:.2f} km")

        # =================================================
        # FINAL RESULT
        # =================================================

        print("\n=================================================")

        if remaining_fuel >= 0:

            print("✅ SAFE TO TRAVEL")
            print("You should reach your destination safely.")

        else:

            print("❌ NOT SAFE TO TRAVEL")
            print("You may run out of fuel before arrival.")

        print("=================================================\n")

    except:
        print("\n⚠️ Invalid input.\n")


# =========================================================
# MAIN PROGRAM LOOP
# =========================================================

while True:

    print("=================================================")
    print("         ADVANCED FUEL RANGE CALCULATOR")
    print("=================================================")

    print("1. Calculate Trip")
    print("2. Add Car To Database")
    print("3. View Car Database")
    print("4. Delete Car From Database")
    print("5. Exit")

    choice = input("\nSelect an option: ")

    # =====================================================
    # MENU OPTIONS
    # =====================================================

    if choice == "1":

        calculate_trip()

    elif choice == "2":

        add_car()

    elif choice == "3":

        display_database()

    elif choice == "4":

        delete_car()

    elif choice == "5":

        print("\nThank you for using the program!")
        break

    else:

        print("\n⚠️ Invalid choice. Please try again.\n")
