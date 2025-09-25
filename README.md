# **ASCII Art Project - Polkadots Analyzer**  

This project implements an ASCII art analysis system that identifies and counts *polkadots* following specific scoring rules. Developed as part of an AI engineering challenge, it demonstrates:  

✅ **Clean architecture** (separation of models, services and core logic)  
✅ **Testability** (unit tests for all components)  
✅ **Extensibility** (easy adaptation for new art formats)  

---

## 📂 **Project Structure**  
```
/ascii_art_project/
│
├── /data/                     # Data layer
│   └── angelica_art.txt       # Original ASCII art
│
├── /src/                      # Core source code
│   ├── __init__.py
│   ├── models.py              # Data classes (LipsCoordinates, PolkadotScoreResult)
│   ├── services.py            # Services (detector, counter, renderer)
│   ├── analyzer.py            # Core logic (PolkadotAnalyzer)
│   └── main.py                # CLI entry point
│
├── /tests/                    # Unit tests
│   ├── __init__.py
│   └── test_analyzer.py       # Integration tests
│
├── .gitignore
├── requirements.txt           # Dependencies (Python 3.8+)
└── README.md                  # Documentation
```

---

## ⚙️ **Installation & Usage**  

### Prerequisites  
- Python 3.8+  
- Git (optional)  

### Steps:  
```bash
# 1. Clone the repository (or download manually)
git clone https://github.com/kleberimeusp/ai-engineer-challenge.git
cd ai-engineer-challenge/ascii_art_project

# 2. Set up the environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the analyzer
python -m src.main
```

**Expected output:**  
```plaintext
=== ASCII Art ===
(Art rendered in terminal...)
=== Results ===
🔵 Normal dots: 23
🔴 Double dots: 12
🏆 Total score: 47
```

---

## 🧠 **Technical Design**  

### Core Layers  
| File         | Function                                |  
|--------------|-----------------------------------------|  
| `models.py`  | Defines immutable data structures (`@dataclass`) |  
| `services.py` | Contains:  <br> • `LipsLineDetector` (detects `–`)<br> • `DressPolkadotCounter` (counts `O`)<br> • `ConsoleArtRenderer` |  
| `analyzer.py` | Orchestrates flow: `detect() → count() → render()` |  

### Business Rules  
- **Lips line**: Identified by `–` character  
- **Scoring**:  
  - `O` outside lips → **1 point**  
  - `O` between `start_x` and `end_x` → **2 points**  

---

## 🧪 **Tests**  
```bash
# Run all tests
python -m unittest discover tests
```  
**Coverage:**  
✔ Lips detection tests  
✔ Dot counting validation  
✔ Correct score calculation  

---

## 🛠 **Extensibility**  
### Advanced Use Cases  
```python  
# Example: Add JSON support  
class JSONExporter:  
    def export(self, result: PolkadotScoreResult) -> str:  
        return json.dumps(asdict(result))  

# Usage:  
analyzer = PolkadotAnalyzer(exporter=JSONExporter())  
```  

---

## 📜 **License**  
MIT License - Free for use and modification.  

**Developed by:** [Kleber Augusto](https://github.com/kleberimeusp)  
**Repository:** [github.com/kleberimeusp/ai-engineer-challenge](https://github.com/kleberimeusp/ai-engineer-challenge)  