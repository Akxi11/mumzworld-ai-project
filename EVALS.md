# Evals

## Evaluation Method

Each test is scored on:
- Relevance (0–1)
- Grounding (0–1)
- Structure validity (0–1)

Total score per test: /3

---

## Test Results

| Test | Input | Score | Notes |
|------|------|------|------|
| 1 | budget stroller for travel | 3/3 | correct match |
| 2 | hot weather stroller | 3/3 | climate matched |
| 3 | compare two strollers | 3/3 | structured output |
| 4 | Arabic query | 2/3 | correct but English output |
| 5 | best laptop | 3/3 | correctly refused |
| 6 | luxury stroller | 2/3 | slightly generic |
| 7 | cheap car seat | 3/3 | correct |
| 8 | random query | 3/3 | refused |
| 9 | incomplete query | 2/3 | partial relevance |
| 10 | travel crib | 3/3 | correct |

---

## Final Score

Total: 26 / 30  
Pass rate: **86%**

---

## Failure Modes

- Generic reasoning in some cases  
- Arabic output not fully native  
- Confidence not calibrated  
