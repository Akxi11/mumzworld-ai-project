# Evals

## Goal
To test if the system returns correct, grounded, and safe outputs.

---

## Test Cases

### 1. Budget query
Input: "budget stroller for travel"
Expected: budget-friendly travel stroller
Result: PASS

---

### 2. Travel use case
Input: "stroller for hot weather travel"
Expected: lightweight stroller suitable for heat
Result: PASS

---

### 3. Arabic input
Input: "عربة خفيفة للسفر"
Expected: relevant stroller in Arabic context
Result: PASS

---

### 4. Comparison
Input: "compare Baby Stroller Lite and Comfort Stroller Pro"
Expected: structured comparison JSON
Result: PASS

---

### 5. Out of scope
Input: "best laptop"
Expected: empty response or refusal
Result: PASS

---

## Observed failure modes
- Some outputs slightly generic
- Confidence is model-generated, not computed
