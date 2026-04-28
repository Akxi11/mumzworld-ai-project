Mumzworld AI Shopping Assistant
1. Summary

I built an AI-powered shopping assistant for Mumzworld that helps parents discover and compare baby products based on real needs like budget, travel, and climate.

The system combines structured product data with LLM reasoning to generate grounded, explainable recommendations and supports both English and Arabic queries.

2. Problem

Parents shopping on Mumzworld often face:

Too many similar products
Unclear differences between options
Difficulty mapping needs (e.g., “travel”, “hot weather”) to product features

This leads to decision friction and drop-offs.

3. Solution

A retrieval-augmented AI assistant that:

Recommends products based on user intent
Explains why they are suitable using product attributes
Compares products side-by-side
Handles multilingual queries
Avoids hallucination by grounding responses in input data
4. How it works (Architecture)
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

5. Features
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
6. Evals
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
7. Tradeoffs
Used keyword retrieval instead of embeddings → simpler but less flexible
Used model-generated confidence → easy but not fully reliable
Small dataset → faster iteration, less coverage

Next steps:

Add embeddings for semantic search
Improve Arabic fluency
Build simple UI
8. Tooling
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
9. AI usage note

Used OpenRouter (DeepSeek Chat v3) for LLM reasoning.
Used ChatGPT as a coding assistant for debugging and prompt iteration.
Core logic implemented manually.

10. Time log
Data + design: 1h
Core logic: 2h
AI integration: 1h
Debugging: 1h
Total: ~5 hours
