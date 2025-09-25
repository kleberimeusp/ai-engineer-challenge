Here's the English version of your AI Architecture Documentation:

---

# **AI Architecture Documentation - ASCII Art Analyzer**  

## **📌 Overview**  
**Objective**: Intelligent ASCII art analysis system that detects visual patterns (polkadots) and applies AI-based scoring rules.  

**Tech Stack**:  
- **Language**: Python 3.8+  
- **Paradigm**: Object-Oriented + Clean Architecture  
- **AI**: Heuristic classification logic (no ML)  

---

## **🧠 AI Architecture**  
### **1. Processing Pipeline**  
```mermaid
flowchart TD
    A[Input: ASCII Art] --> B[Region Detection<br>(LipsLineDetector)]
    B --> C[Polkadot Classification<br>(DressPolkadotCounter)]
    C --> D[Score Calculation<br>(Business Rules)]
    D --> E[Output: Structured Result]
```

### **2. AI Components**  

| **Module**               | **AI Function**                          | **Technique**                     |
|--------------------------|-------------------------------------------|---------------------------------|
| `LipsLineDetector`       | Identifies semantic regions (lips)       | Pattern Matching (`–`)          |
| `DressPolkadotCounter`   | Classifies polkadots (normal/double)     | Spatial Heuristics (coordinates) |

**AI Rule Example**:  
```python
if lips_coords.start_x <= x <= lips_coords.end_x:
    score += 2  # Double polkadot (within lips)
else:
    score += 1  # Normal polkadot
```

---

## **📂 Project Structure**  
```
ascii_art_project/
│
├── data/                     # Training/Test data (ASCII art)
├── src/
│   ├── ai_components/        # AI Logic
│   │   ├── feature_extractor.py  # Coordinate extraction
│   │   └── classifier.py     # Polkadot classification
│   └── core/                 # Orchestration
├── tests/                    # AI Tests
│   └── test_ai_components.py
```

---

## **⚙️ AI Decision Flow**  
1. **Input**: ASCII Art (30+ lines)  
2. **Pre-processing**:  
   - Character normalization  
   - 2D coordinate mapping  
3. **Inference**:  
   ```python
   def predict_polkadot_type(x, y, lips_coords):
       return "double" if lips_coords.start_x <= x <= lips_coords.end_x else "normal"
   ```
4. **Post-processing**: Aggregate score calculation  

---

## **🧪 AI Testing**  
**Validated Scenarios**:  
```python
def test_lip_detection():
    art = ["   –––   ", "  O  O  "]
    coords = LipsLineDetector().detect(art)
    assert coords.line_index == 0  # Line 0 contains lips

def test_polkadot_classification():
    assert classifier.predict(5, 10, lips_coords) == "double"  # Within lips
```

Execute with:  
```bash
pytest tests/test_ai_components.py -v
```

---

## **🔮 Future Improvements (AI Roadmap)**  
1. **Machine Learning**:  
   - Replace heuristics with CNN model for visual classification  
   - Synthetic dataset of labeled ASCII art  
2. **NLP**:  
   - Interpretation of textual metadata in art (e.g., "ÅÑGË£ÏÇÄ")  

---

## **📜 License**  
MIT License - Available for research and commercial use.  

**Developed by:** [Kleber Augusto](https://github.com/kleberimeusp)  
**Repository:** [github.com/kleberimeusp/ai-engineer-challenge](https://github.com/kleberimeusp/ai-engineer-challenge)  

---

This document follows:  
- **ISO/IEC/IEEE 42010** (Architectural Documentation)  
- **Google AI Principles** (AI Responsibility)  