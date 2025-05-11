import os
import json
import re
from langchain.schema import HumanMessage
from langchain_groq import ChatGroq

def generate_packing_list(trip_details):
    # Fetch API key for Groq or OpenAI
    api_key = os.getenv("GROQ_API_KEY")  # Ensure this environment variable is set for Groq
    if not api_key:
        raise ValueError("GROQ API key not found. Please set the GROQ_API_KEY environment variable.")

    try:

        # Or if Groq provides a similar wrapper:
        llm = ChatGroq(
            model_name="llama-3.3-70b-versatile",  # Use Groq's model name
            temperature=0.7
        )
        
        # Compose full prompt
        prompt = f"""
        Act as a travel planning expert. Generate a comprehensive packing list in JSON format for a trip with the following details:

        Trip Type: {trip_details["trip_type"]}
        Destination: {trip_details["destination"]}
        Duration: {trip_details["duration"]} days
        Season: {trip_details["season"]}
        Accommodation: {trip_details["accommodation"]}
        Transportation: {trip_details["transportation"]}
        Activities: {', '.join(trip_details['activities']) or 'General sightseeing'}
        Special Needs: {trip_details["special_needs"] or "None"}

        Generate a DETAILED and PRACTICAL packing list organized into the following categories:
        1. Clothes & Toiletries
        2. Travel Documents
        3. Phone & Electronics
        4. Money & Cards
        5. Medications & First Aid
        6. Snacks & Water
        7. Maps/Apps & Navigation
        8. Trip-specific Gear
        9. Miscellaneous

        Provide ONLY valid JSON with category names as keys and arrays of strings as values:
        {{
            "Clothes & Toiletries": ["item1", "item2"],
            "Travel Documents": ["item1", "item2"],
            ...
        }}
        """

        # Ask LLM
        response = llm.invoke([HumanMessage(content=prompt)])  # Hypothetical method call
        
        # Try parsing the JSON response
        return json.loads(response.content)  # Assuming `response.content` is valid JSON

    except json.JSONDecodeError:
        # If JSON parsing fails, attempt to extract JSON from the response string
        match = re.search(r'{.*}', response.content, re.DOTALL)
        if match:
            try:
                return json.loads(match.group())
            except Exception as e:
                raise ValueError(f"Extracted JSON but failed to parse: {str(e)}")
        raise ValueError(f"Invalid JSON format returned: {response.content}")

    except Exception as e:
        raise ValueError(f"Error generating packing list: {str(e)}")
