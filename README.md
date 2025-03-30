# Redbus Data Scraping and Filtering with Streamlit Applicatio

## Overview
This project automates the extraction of bus travel data from Redbus using Selenium, stores it in a SQL database, and visualizes it through an interactive Streamlit application. It aims to enhance decision-making in the transportation industry by providing real-time data insights.

## Business Use Cases
- **Travel Aggregators:** Real-time bus schedules and seat availability.
- **Market Analysis:** Insights into travel patterns and preferences.
- **Customer Service:** Personalized travel options.
- **Competitor Analysis:** Price and service comparisons.

## Approach
1. **Data Scraping:** Selenium extracts data (routes, schedules, prices, seat availability).
2. **Data Storage:** Structured storage in a SQL database.
3. **Streamlit Application:** Interactive UI for filtering and analyzing bus data.

## Required Data Fields
- Route Name & Link
- Bus Name & Type (Sleeper/Seater/AC/Non-AC)
- Departure & Arrival Time
- Duration & Star Rating
- Price & Seat Availability

## Database Schema
**Table:** `bus_routes`
| Column | Data Type | Description |
|--------|----------|-------------|
| id | INT | Primary Key (Auto-increment) |
| route_name | TEXT | Bus route details |
| route_link | TEXT | Link to route details |
| busname | TEXT | Name of the bus |
| bustype | TEXT | Bus type |
| departing_time | TIME | Departure time |
| duration | TEXT | Journey duration |
| reaching_time | TIME | Arrival time |
| star_rating | FLOAT | Passenger rating |
| price | DECIMAL | Ticket price |
| seats_available | INT | Available seats |

## Deliverables
- **Source Code:** Python scripts for scraping, database handling, and Streamlit UI.
- **Documentation:** Guide on project implementation and usage.
- **Database Schema:** SQL scripts for database creation.
- **Streamlit App:** Interactive interface for data filtering.

## Tech Stack
- **Web Scraping:** Selenium
- **Database:** SQL
- **Frontend:** Streamlit
- **Backend:** Python

## References
- [Streamlit Documentation](https://docs.streamlit.io/get-started/installation)
- [Selenium Documentation](https://www.selenium.dev/documentation/webdriver/elements/locators/)

