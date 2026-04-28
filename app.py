import json
import re
from openai import OpenAI


def clean_json(text):
    text = re.sub(r"```json", "", text)
    text = re.sub(r"```", "", text)
    return text.strip()
print("Program started")

# 🔑 PASTE YOUR API KEY HERE
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

# 📦 Load products
with open("products.json", "r", encoding="utf-8") as file:
    products = json.load(file)

print("Loaded products")

# 🔍 Search function (RAG)
def search_products(query):
    results = []
    query = query.lower()

    for product in products:
        text = " ".join(
            product.get("features", []) +
            product.get("reviews", []) +
            [product.get("name", ""), product.get("category", "")]
        ).lower()

        if any(word in text for word in query.split()):
            results.append(product)

    return results

# 🤖 AI function
def generate_response(context, query):
    prompt = f"""
You are an AI shopping assistant for Mumzworld, an e-commerce platform for mothers in the GCC.

ONLY use the product data below:
{context}

User query: {query}

Your job:
- Recommend the best products based on user needs
- Use fields like price, features, region_use_case, climate_suitability, and age_stage
- Focus on real parenting needs (travel, hot weather, safety, comfort)

Rules:
- Do NOT make up information
- If data is insufficient, return:
{{
  "recommendations": []
}}

Return JSON:
{{
  "recommendations": [
    {{
      "name": "...",
      "why_good_for_you": "...",
      "best_for": "...",
      "not_ideal_for": "...",
      "confidence": 0.0
    }}
  ]
}}
"""

    try:
        response = client.chat.completions.create(
            model="deepseek/deepseek-chat",
            messages=[{"role": "user", "content": prompt}]
        )

        # Debug: see full response
        print("\nDEBUG RESPONSE:\n", response)

        if response and response.choices:
           raw = response.choices[0].message.content
           return clean_json(raw)
        else:
            return "Error: No response from AI."

    except Exception as e:
        return f"Error occurred: {str(e)}"

def find_products_for_comparison(query):
    matches = []
    query = query.lower()

    for product in products:
        name = product.get("name", "").lower()
        if name in query:
            matches.append(product)

    return matches[:2]  # only take first 2

def compare_products(products_to_compare):
    context = json.dumps(products_to_compare, indent=2)

    prompt = f"""
You are a helpful shopping assistant.

Compare the following two products:

{context}

Rules:
- Compare features, price, and use-case
- Highlight key differences
- Say which one is better for what situation
- Do NOT make up information

Return JSON like:
{{
  "comparison": {{
    "product_1": "...",
    "product_2": "...",
    "differences": "...",
    "recommendation": "..."
  }}
}}
"""

    try:
        response = client.chat.completions.create(
            model="deepseek/deepseek-chat",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"
    
    
# 🧠 MAIN PROGRAM
query = input("\nWhat are you looking for? ")
if "compare" in query.lower():
    print("Comparison mode activated")

if "compare" in query.lower():
    products_to_compare = find_products_for_comparison(query)

    if len(products_to_compare) < 2:
        print("Need two products to compare.")
    else:
        result = compare_products(products_to_compare)
        print("\nComparison:\n")
        print(result)

else:
    results = search_products(query)

    if len(results) == 0:
        print("I don't know enough to answer this.")
    else:
        context = json.dumps(results, indent=2)
        answer = generate_response(context, query)

        print("\nAI Response:\n")
        print(answer)