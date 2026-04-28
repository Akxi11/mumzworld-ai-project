# Tradeoffs

## Why this project
Built an AI shopping assistant for Mumzworld to help parents find and compare baby products using natural language.

---

## Key design decisions

### 1. Keyword-based retrieval
✔ Simple and fast  
❌ Not fully semantic  

Chosen because it was easy to implement within time limits.

---

### 2. LLM for reasoning
✔ Good explanations  
❌ Can hallucinate if not controlled  

Solved by strict prompting and grounding rules.

---

### 3. Small dataset
✔ Fast iteration  
❌ Limited coverage of products  

---

## Handling uncertainty
- If no match → return empty response  
- If query is out of scope → explicit “I don’t know”  

---

## What I would improve next
- Add embeddings for semantic search  
- Improve Arabic fluency  
- Build UI for better user experience  
- Integrate real Mumzworld catalog data  

---

## Summary
This project prioritizes grounded outputs and structured reasoning over complexity.
