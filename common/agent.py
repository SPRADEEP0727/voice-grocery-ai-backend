
import os
import json
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def organize_groceries(items):
    """Organize grocery items by store categories using OpenAI"""
    try:
        prompt = f"""You are an expert grocery categorization system. Your task is to:

1. Categorize grocery items into appropriate store sections
2. Use standard grocery store categories like: dairy, meat, vegetables, fruits, spices, bakery, grains, frozen, beverages, snacks, cleaning, personal_care, etc.
3. Return ONLY a valid JSON object with categories as keys and arrays of items as values
4. Do not include any explanatory text, only the JSON response
5. Group similar items together intelligently

Example format:
{{
  "dairy": ["milk", "cheese"],
  "meat": ["chicken", "beef"],
  "spices": ["chilli powder", "turmeric"],
  "vegetables": ["onion", "tomato"]
}}

Categorize these grocery items: {items}. Return only valid JSON with categories and items."""

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a grocery categorization expert. Return only valid JSON."},
                {"role": "user", "content": prompt}
            ],
            temperature=0,
            max_tokens=1000
        )
        
        content = response.choices[0].message.content.strip()
        
        # Try to parse JSON from the response
        try:
            # Clean the response - remove any non-JSON text
            json_start = content.find('{')
            json_end = content.rfind('}') + 1
            if json_start != -1 and json_end != 0:
                json_str = content[json_start:json_end]
                categorized_items = json.loads(json_str)
                return categorized_items
            else:
                return {"error": "Could not parse categorization response"}
        except json.JSONDecodeError:
            return {"error": "Invalid JSON response", "raw_response": content}
            
    except Exception as e:
        return {"error": f"Processing failed: {str(e)}"}

def suggest_groceries_for_recipe(recipe):
    """Suggest groceries for a recipe using OpenAI"""
    try:
        prompt = f"""You are an expert recipe analyzer and grocery list generator. Your task is to:

1. Analyze the given recipe and extract ALL required ingredients
2. Include specific quantities and measurements where possible
3. Consider common pantry items that might be needed (oils, salt, basic spices)
4. Categorize each ingredient into appropriate grocery store sections
5. Return ONLY a valid JSON object with the specified format
6. Do not include any explanatory text, only the JSON response

Example format:
{{
  "ingredients": [
    {{"item": "chicken breast", "quantity": "500g", "category": "meat"}},
    {{"item": "onion", "quantity": "2 large", "category": "vegetables"}},
    {{"item": "tomato", "quantity": "3 medium", "category": "vegetables"}},
    {{"item": "garam masala", "quantity": "1 tsp", "category": "spices"}}
  ]
}}

Analyze this recipe and provide a complete grocery list with quantities and categories: {recipe}. Return only valid JSON."""

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a recipe analyzer and grocery list generator. Return only valid JSON."},
                {"role": "user", "content": prompt}
            ],
            temperature=0,
            max_tokens=1500
        )
        
        content = response.choices[0].message.content.strip()
        
        # Try to parse JSON from the response
        try:
            # Clean the response - remove any non-JSON text
            json_start = content.find('{')
            json_end = content.rfind('}') + 1
            if json_start != -1 and json_end != 0:
                json_str = content[json_start:json_end]
                recipe_ingredients = json.loads(json_str)
                return recipe_ingredients
            else:
                return {"error": "Could not parse recipe analysis response"}
        except json.JSONDecodeError:
            return {"error": "Invalid JSON response", "raw_response": content}
            
    except Exception as e:
        return {"error": f"Recipe analysis failed: {str(e)}"}
