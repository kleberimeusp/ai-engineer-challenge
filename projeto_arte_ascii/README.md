# **Documentação de Arquitetura de IA - ASCII Art Analyzer**  

## **📌 Visão Geral**  
**Objetivo**: Sistema de análise inteligente de arte ASCII que detecta padrões visuais (polkadots) e aplica regras de pontuação baseadas em IA.  

**Stack**:  
- **Linguagem**: Python 3.8+  
- **Paradigma**: Orientado a Objetos + Arquitetura Limpa  
- **IA**: Lógica de classificação heurística (sem ML)  

---

## **🧠 Arquitetura de IA**  
### **1. Pipeline de Processamento**  
```mermaid
flowchart TD
    A[Input: Arte ASCII] --> B[Detecção de Regiões<br>(LipsLineDetector)]
    B --> C[Classificação de Polkadots<br>(DressPolkadotCounter)]
    C --> D[Cálculo de Pontuação<br>(Business Rules)]
    D --> E[Output: Resultado Estruturado]
```

### **2. Componentes Inteligentes**  

| **Módulo**               | **Função de IA**                          | **Técnica**                     |
|--------------------------|-------------------------------------------|---------------------------------|
| `LipsLineDetector`       | Identifica regiões semânticas (lábios)    | Pattern Matching (`–`)          |
| `DressPolkadotCounter`   | Classifica polkadots (normais/duplos)     | Heurística Espacial (coordenadas) |

**Exemplo de Regra de IA**:  
```python
if lips_coords.start_x <= x <= lips_coords.end_x:
    pontos += 2  # Polkadot duplo (dentro dos lábios)
else:
    pontos += 1  # Polkadot normal
```

---

## **📂 Estrutura do Projeto**  
```
projeto_arte_ascii/
│
├── data/                     # Treino/Teste (arte ASCII)
├── src/
│   ├── ai_components/        # Lógica de IA
│   │   ├── feature_extractor.py  # Extrai coordenadas
│   │   └── classifier.py     # Classifica polkadots
│   └── core/                 # Orquestração
├── tests/                    # Testes de IA
│   └── test_ai_components.py
```

---

## **⚙️ Fluxo de Decisão de IA**  
1. **Entrada**: Arte ASCII (30+ linhas)  
2. **Pré-processamento**:  
   - Normalização de caracteres  
   - Mapeamento 2D de coordenadas  
3. **Inferência**:  
   ```python
   def predict_polkadot_type(x, y, lips_coords):
       return "duplo" if lips_coords.start_x <= x <= lips_coords.end_x else "normal"
   ```
4. **Pós-processamento**: Cálculo de pontuação agregada  

---

## **🧪 Testes de IA**  
**Cenários Validados**:  
```python
def test_lip_detection():
    arte = ["   –––   ", "  O  O  "]
    coords = LipsLineDetector().detect(arte)
    assert coords.line_index == 0  # Linha 0 contém os lábios

def test_polkadot_classification():
    assert classifier.predict(5, 10, lips_coords) == "duplo"  # Dentro dos lábios
```

Execute com:  
```bash
pytest tests/test_ai_components.py -v
```

---

## **🔮 Melhorias Futuras (Roadmap de IA)**  
1. **Machine Learning**:  
   - Substituir heurística por modelo CNN para classificação visual  
   - Dataset sintético de arte ASCII com labels  
2. **NLP**:  
   - Interpretação de metadados textuais na arte (ex: "ÅÑGË£ÏÇÄ")  

---

## **📜 Licença**  
MIT License - Disponível para pesquisa e uso comercial.  

**Desenvolvido por:** [Kleber Augusto](https://github.com/kleberimeusp)  
**Repositório:** [github.com/kleberimeusp/ai-engineer-challenge](https://github.com/kleberimeusp/ai-engineer-challenge)  

---

Este documento segue os padrões:  
- **ISO/IEC/IEEE 42010** (Documentação Arquitetural)  
- **Google AI Principles** (Responsabilidade em IA)