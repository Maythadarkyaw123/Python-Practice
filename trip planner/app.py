import streamlit as st
import os
from packing_helper import generate_packing_list
from dotenv import load_dotenv
import json
from langchain_groq import ChatGroq 


# Load environment variables from .env
load_dotenv()
api_key = os.getenv("GROQ_API_KEY", "")

if not api_key:
    st.error("❌ API key not found in .env file. Please add GROQ_API_KEY.")
    st.stop()

# Page configuration
st.set_page_config(
    page_title="Trip Packing Checklist Generator",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ Trip Packing Checklist Generator")
st.markdown("Generate a customized packing checklist based on your trip details using AI")

# Sidebar - User Inputs
with st.sidebar:
    st.header("Trip Details")

    # Input fields
    trip_type = st.selectbox("Trip Type", [
        "Business Trip", "Beach Vacation", "Mountain/Hiking Trip", "City Break",
        "Camping", "Ski Trip", "Road Trip", "Cruise", "International Travel", "Family Vacation"
    ])
    
    destination = st.text_input("Destination", "")
    duration = st.number_input("Duration (days)", min_value=1, max_value=365, value=7)
    season = st.selectbox("Season", ["Spring", "Summer", "Fall", "Winter"])
    accommodation = st.selectbox("Accommodation", [
        "Hotel", "Hostel", "Airbnb/Rental", "Camping", "Staying with Friends/Family", "Other"
    ])
    transportation = st.selectbox("Main Transportation", [
        "Plane", "Car", "Train", "Bus", "Boat", "Walking/Hiking", "Other"
    ])
    activities = st.multiselect("Planned Activities", [
        "Swimming", "Hiking", "Business Meetings", "Formal Events", "Photography",
        "Winter Sports", "Beach Activities", "Cultural Visits",
        "Outdoor Adventure", "Nightlife", "Shopping", "Sightseeing"
    ])
    
    special_needs = st.text_area("Special Needs or Considerations", "")
    generate_button = st.button("Generate Packing List", use_container_width=True)

# Main logic
if generate_button:
    with st.spinner("Generating your customized packing list with AI..."):
        trip_details = {
            "trip_type": trip_type,
            "destination": destination,
            "duration": duration,
            "season": season,
            "accommodation": accommodation,
            "transportation": transportation,
            "activities": activities,
            "special_needs": special_needs
        }

        try:
            # Get packing list from the helper function
            packing_list = generate_packing_list(trip_details)

            st.success("✅ Your customized packing list is ready!")

            # Display packing list as a list (not checkboxes)
            st.markdown("### Packing List:")
            for category, items in packing_list.items():
                st.markdown(f"#### {category}")
                if items:
                    st.write(", ".join(items))
                else:
                    st.write("No items for this category.")

            # Display the output in JSON format
            st.markdown("### Output in JSON format:")
            st.json(packing_list)

        except Exception as e:
            st.error(f"An error occurred while generating your packing list: {str(e)}")

else:
    st.info("👈 Fill in your trip details in the sidebar and click 'Generate Packing List'")
    st.markdown("### Sample Things")

    col1, col2 = st.columns(2)
    with col1:
        with st.expander("Clothes & Toiletries", expanded=True):
            st.write("Weather-appropriate outfits, Underwear, Toothbrush, toothpaste, Sleepwear, Deodorant")

    with col2:
        with st.expander("Travel Documents", expanded=True):
            st.write("Passport, Visa, Tickets, Booking Confirmations, Travel Insurance")

    st.markdown("""
    ### How It Works
    1. Fill in your trip details
    2. Click **Generate Packing List**
    """)
