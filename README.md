Mumzworld AI Shopping Assistant
1. Summary

This project is an AI-powered shopping assistant for Mumzworld that helps parents find, compare, and understand baby products using structured data and AI reasoning.

It supports product recommendations, comparisons, and multilingual queries (English + Arabic), with grounded and explainable outputs.

2. Prototype Access

GitHub Repo:
👉 https://github.com/Akxi11/mumzworld-ai-project

3. 3-minute Loom

👉 [https://loom.com/share/YOUR-VIDEO-LINK](https://www.loom.com/share/a93479cd1c2940ccbf0a3b17f1a5bd67)

4. Problem

Parents shopping on Mumzworld often face:

Too many similar products
Unclear differences between options
Difficulty mapping needs (e.g., “travel”, “hot weather”) to product features

This leads to decision friction and drop-offs.

5. Solution

A retrieval-augmented AI assistant that:

Recommends products based on user intent
Explains why they are suitable using product attributes
Compares products side-by-side
Handles multilingual queries
Avoids hallucination by grounding responses in input data

6. How it works (Architecture)
User Query
   ↓
Retrieval (filter relevant products)
   ↓
Context (structured JSON)
   ↓
LLM (reasoning + structured output)
   ↓
Validation + cleaning
   ↓
Final response

Key idea:

The model is used as a reasoning layer, not as the source of truth.

7. Features
 Recommendations
budget stroller for travel

Returns:

Relevant products
Attribute-based reasoning
Confidence score
 Comparison
compare Travel Stroller Compact and Baby Stroller Lite

Returns:

Structured comparison
Differences (price, weight, features)
Recommendation
 Multilingual
عربة خفيفة للسفر
Handles Arabic queries
Uses mixed-language product data
 Uncertainty handling
best laptop
{
  "recommendations": [],
  "message": "I don't know enough to answer this."
}


8. Evals
Case	Input	Result
Recommendation	budget stroller	correct
Use-case	travel stroller	correct
Arabic	عربة خفيفة للسفر	correct
Comparison	compare products	correct
Out-of-scope	best laptop	handled

Failure modes identified:

Keyword-based retrieval limits recall
Some explanations can be generic
Confidence is model-estimated


9. Tradeoffs
Used keyword retrieval instead of embeddings → simpler but less flexible
Used model-generated confidence → easy but not fully reliable
Small dataset → faster iteration, less coverage

Next steps:

Add embeddings for semantic search
Improve Arabic fluency
Build simple UI


10. Tooling
OpenRouter + DeepSeek Chat v3 for generation
AI-assisted development (ChatGPT) for debugging, prompt iteration, and refactoring

Approach:

Prompt-driven development
Manual control over retrieval and comparison logic
Added validation + fallback handling

Challenges:

Model availability (404 errors)
JSON formatting issues

Overrides:

Enforced structured outputs
Added JSON cleaning
Prevented hallucinations via strict prompting


11. AI usage note

Used OpenRouter (DeepSeek Chat v3) for LLM reasoning.
Used ChatGPT as a coding assistant for debugging and prompt iteration.
Core logic implemented manually.

12. Time log
Data + design: 1h
Core logic: 2h
AI integration: 1h
Debugging: 1h
Total: ~5 hours
