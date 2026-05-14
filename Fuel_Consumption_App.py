import streamlit as st

st.title("🚗 Fuel Calculator App")
st.write("If you can see this, Streamlit is working.")
import streamlit as st

# =========================
# PAGE CONFIG (makes it less plain)
# =========================
st.set_page_config(
    page_title="Fuel Calculator",
    page_icon="🚗",
    layout="centered"
)

# =========================
# TITLE
# =========================
st.title("🚗 Advanced Fuel Range Calculator")
st.write("Plan your trips safely with fuel estimation + margin of error")

# =========================
# SESSION DATABASE (important for Streamlit)
# =========================
import json
import os

# =========================
# LOAD DATABASE
# =========================
DATABASE_FILE = "cars.json"

def load_database():

    if os.path.exists(DATABASE_FILE):

        with open(DATABASE_FILE, "r") as file:
            return json.load(file)

    return {}

# =========================
# SAVE DATABASE
# =========================
def save_database(database):

    with open(DATABASE_FILE, "w") as file:
        json.dump(database, file, indent=4)

# Load database
car_database = load_database()

# =========================
# SIDEBAR MENU (replaces your terminal menu)
# =========================
menu = st.sidebar.selectbox(
    "📌 Menu",
    ["Calculate Trip", "View Database", "Add Car", "Delete Car"]
)

# =========================
# VIEW DATABASE
# =========================
if menu == "View Database":
    st.subheader("📊 Car Database")

    for car, data in car_database.items():
        st.write(f"**{car}**")
        st.write(f"- Fuel Economy: {data['km_per_liter']} km/L")
        st.write(f"- Tank Capacity: {data['tank_capacity']} L")
        st.divider()

# =========================
# ADD CAR
# =========================
elif menu == "Add Car":

    st.subheader("➕ Add New Car")

    name = st.text_input("Car Model & Year")

    kmpl = st.number_input(
        "Fuel Economy (km/L)",
        min_value=0.0,
        step=0.1
    )

    tank = st.number_input(
        "Tank Capacity (L)",
        min_value=0.0,
        step=1.0
    )

    if st.button("Add Car"):

        if name:

            car_database[name] = {
                "km_per_liter": kmpl,
                "tank_capacity": tank
            }

            save_database(car_database)

            st.success(f"{name} added successfully!")

        else:
            st.error("Please enter car name")
            
# =========================
# DELETE CAR
# =========================
elif menu == "Delete Car":
    st.subheader("🗑️ Delete Car")

    car_list = list(car_database.keys())

    selected = st.selectbox("Select car to delete", car_list)

if st.button("Delete"):

    del car_database[selected]

    save_database(car_database)

    st.warning(f"{selected} deleted")
# =========================
# CALCULATE TRIP
# =========================
elif menu == "Calculate Trip":

    st.subheader("🧮 Trip Calculator")

    car_list = list(car_database.keys())
    selected_car = st.selectbox("Select Car", car_list)

    car = car_database[selected_car]

    kmpl = car["km_per_liter"]
    tank = car["tank_capacity"]

    st.write(f"Fuel Economy: **{kmpl} km/L**")
    st.write(f"Tank Capacity: **{tank} L**")

    current_fuel = st.number_input("Current Fuel (L)", min_value=0.0, step=0.1)
    distance = st.number_input("Distance to Travel (km)", min_value=0.0, step=1.0)

    safety_margin = 0.90
    adjusted_kmpl = kmpl * safety_margin

    if st.button("Calculate"):

        max_distance = current_fuel * adjusted_kmpl
        fuel_needed = distance / adjusted_kmpl
        remaining = current_fuel - fuel_needed

        current_pct = (current_fuel / tank) * 100
        used_pct = (fuel_needed / tank) * 100
        remaining_pct = (remaining / tank) * 100

        st.subheader("📊 Results")

        st.write(f"Adjusted Fuel Economy: **{adjusted_kmpl:.2f} km/L**")
        st.write(f"Max Distance: **{max_distance:.2f} km**")

        st.write(f"Fuel Needed: **{fuel_needed:.2f} L ({used_pct:.1f}%)**")
        st.write(f"Current Fuel: **{current_fuel:.2f} L ({current_pct:.1f}%)**")
        st.write(f"Remaining Fuel: **{remaining:.2f} L ({remaining_pct:.1f}%)**")

        st.divider()

        if remaining >= 0:
            st.success("✅ SAFE TO TRAVEL")
        else:
            st.error("❌ NOT SAFE TO TRAVEL")
