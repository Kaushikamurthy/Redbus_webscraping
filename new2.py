import streamlit as st
import mysql.connector
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="Red Bus System",
)

# Connect to MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="redbusquery"
)
mycursor = mydb.cursor(buffered=True)

# Sidebar for navigation
st.sidebar.markdown("<h2 style='color: #0073e6;'>Navigation 🚌</h2>", unsafe_allow_html=True)
menu = ["Home", "About"]
selected_menu = st.sidebar.selectbox("Select a Page", menu, index=0)

# Page Heading
st.markdown("<h1 style='text-align: center; color: #ff6600;'>State Road Transport Corporation (SRTC) of India 🚍</h1>", unsafe_allow_html=True)

# Home Page Content
if selected_menu == "Home":
    st.markdown("""
        <div style="background-color:#f2f2f2;padding:20px;border-radius:10px;">
        <h2 style='color: #ff6600;'>Welcome to the Red Bus System 🚀</h2>
        <p>This is the ultimate platform to explore and navigate the State Road Transport Corporation (SRTC) bus routes and schedules across India. Whether you're planning your next trip or just curious about the routes, we have got you covered! 🌍</p>
        <h3 style='color: #ff6600;'>What You Can Do:</h3>
        <ul>
            <li><b>🗺️ Explore Bus Routes</b> by selecting the state you want to travel in.</li>
            <li><b>🔍 Filter Buses</b> based on your preferences, such as bus type, fare, ratings, and availability.</li>
            <li><b>📅 View Detailed Information</b> about buses, timings, and seats available.</li>
        </ul>
        <p>Our mission is to make bus travel easy, affordable, and accessible to everyone in India! 🇮🇳</p>
        </div>
    """, unsafe_allow_html=True)
else:
    # About Page Content
    st.markdown("""
        <div style="background-color:#f2f2f2;padding:20px;border-radius:10px;">
        <h2 style='color: #ff6600;'>About the Red Bus System 🚌</h2>
        <p>Welcome to the State Road Transport Corporation (SRTC) of India, where you can find detailed information about buses, routes, and schedules. This system helps you:</p>
        <ul>
            <li><b>🌍 Explore different routes</b> based on the state you are traveling in.</li>
            <li><b>🔎 Filter buses</b> based on various criteria such as bus type, fare, and ratings.</li>
            <li><b>📝 Access detailed bus information</b>, including available seats, bus timings, and much more.</li>
        </ul>
        <p>The data is sourced from the <b>Red Bus Database</b>, providing an up-to-date and easy-to-use interface for all your travel needs. Whether you're traveling for work, leisure, or anything in between, we aim to make your journey smooth and efficient. 🚄</p>
        <h3 style='color: #ff6600;'>Features:</h3>
        <ul>
            <li><b>📍 State-based bus routes</b></li>
            <li><b>🚍 Detailed bus information</b></li>
            <li><b>⚙️ Advanced filtering options</b></li>
        </ul>
        <p>If you have any questions, feel free to contact our support team or explore the system further! 💬</p>
        </div>
    """, unsafe_allow_html=True)

# Fetch distinct states from the database
if selected_menu == "Home":
    mycursor.execute("SELECT DISTINCT States FROM Bus_data")
    states = mycursor.fetchall()
    states_df = pd.DataFrame(states, columns=["States"])

    # State selection dropdown
    selected_state = st.selectbox("Select State 🌏", states_df["States"].unique())

    if selected_state:
        # Fetch route names and links for the selected state
        mycursor.execute("SELECT Route_name, Route_link FROM Bus_data WHERE States = %s", (selected_state,))
        routes = mycursor.fetchall()
        routes_df = pd.DataFrame(routes, columns=["Route_name", "Route_link"])

        if not routes_df.empty:
            # Route selection dropdown
            selected_route = st.selectbox("Select Route 🚍", routes_df["Route_name"].unique())

            if selected_route:
                # Fetch route link
                route_link = routes_df[routes_df["Route_name"] == selected_route]["Route_link"].values[0]
                st.markdown(f"Route Details: [Click Here]({route_link})")

                # Fetch bus details for the selected route
                mycursor.execute(""" 
                    SELECT Bus_name, Bus_type, Start_time, End_time, Total_duration, Ratings, Price, Seats_Available 
                    FROM Bus_data 
                    WHERE Route_name = %s
                """, (selected_route,))
                bus_details = mycursor.fetchall()

                # Create a DataFrame from the fetched data
                bus_details_df = pd.DataFrame(
                    bus_details,
                    columns=["Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration", "Ratings", "Price", "Seats_Available"]
                )

                # Ensure Start_time is in datetime format and handle errors
                bus_details_df["Start_time"] = pd.to_datetime(bus_details_df["Start_time"], format='%H:%M:%S', errors='coerce')

                # Time interval filter: Dropdown for specific start times
                start_times = ['00:00', '06:00', '12:00', '18:00']
                selected_time = st.selectbox("Select Start Time ⏰", start_times)

                # Convert selected time to a datetime object (ignoring date)
                selected_time = pd.to_datetime(selected_time, format='%H:%M').time()

                # Extract only the time part of the 'Start_time' column
                bus_details_df["Start_time_only"] = bus_details_df["Start_time"].dt.time

                # Filter buses based on selected time (start time >= selected time)
                filtered_df = bus_details_df[bus_details_df["Start_time_only"] >= selected_time]

                # Enhance table display
                st.markdown("<h3 style='color: #ff6600;'>Available Buses 🚍</h3>", unsafe_allow_html=True)

                # Display the filtered buses
                if filtered_df.empty:
                    st.write("No buses available after this time.")
                else:
                    st.dataframe(filtered_df)




