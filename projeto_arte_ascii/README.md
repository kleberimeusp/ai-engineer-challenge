# **AI Engineer Challenge - ASCII Art Analyzer**  

🔍 **Challenge**: Contar *polkadots* em uma arte ASCII seguindo regras específicas de pontuação.  

🚀 **Solução**: Um sistema modular em Python que:  
✔ **Detecta** a linha dos lábios (`–`)  
✔ **Conta** pontos normais (`O` = 1 ponto) e duplos (dentro dos lábios = 2 pontos)  
✔ **Calcula** a pontuação total  

---

## **📂 Estrutura do Projeto**
```
ai-engineer-challenge/
│
├── data/
│   └── angelica_art.txt       # Arte ASCII original (~30 linhas)
│
├── src/
│   ├── __init__.py
│   ├── models.py              # Data classes (LipsCoordinates, PolkadotScoreResult)
│   ├── services.py            # Lógica de detecção e contagem
│   ├── analyzer.py            # Orchestrador principal
│   └── main.py                # CLI entrypoint
│
├── tests/
│   ├── __init__.py
│   ├── test_services.py       # Testes unitários
│   └── test_analyzer.py
│
├── .gitignore
├── requirements.txt           # Python 3.8+
└── README.md
```

---

## **⚡ Como Executar**
```bash
# Clone o repositório
git clone https://github.com/kleberimeusp/ai-engineer-challenge.git
cd ai-engineer-challenge

# Ambiente virtual (opcional)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Execute o analisador
python -m src.main
```
**Saída Esperada**:
```plaintext
=== Arte ASCII ===
(Arte renderizada aqui...)
=== Resultados ===
🔵 Pontos normais: 23
🔴 Pontos duplos: 12  
🏆 Pontuação total: 47
```

---

## **🧩 Componentes Técnicos**
### **1. Core Modules**
| Arquivo         | Responsabilidade                          |
|-----------------|------------------------------------------|
| `models.py`     | `@dataclass` para coordenadas e resultados |
| `services.py`   | `LipsLineDetector`, `DressPolkadotCounter` |
| `analyzer.py`   | Orquestração (`detect→count→render`)     |

### **2. Regras de Negócio**
- **Detecção de lábios**: Linha contendo `–`  
- **Pontuação**:  
  - `O` fora dos lábios → 1 ponto  
  - `O` entre `start_x` e `end_x` → 2 pontos  

### **3. Design Patterns**
- **Single Responsibility**: Cada classe faz uma coisa  
- **Dependency Injection**: Serviços injetados no `PolkadotAnalyzer`  

---

## **🧪 Testes**
```bash
# Execute todos os testes
python -m unittest discover tests
```
**Cobertura**:  
✔ Testes para `detect()` (linha dos lábios)  
✔ Testes para `count()` (edge cases)  
✔ Integração com `analyze()`  

---

## **🛠 Extensibilidade**
```python
# Exemplo: Adicionar novo renderizador (HTML/JSON)
class HTMLRenderer:
    def render(self, art: List[str]) -> str:
        return f"<pre>{''.join(art)}</pre>"

# Uso:
analyzer = PolkadotAnalyzer(renderer=HTMLRenderer())
```

---

## **📜 Licença**
MIT License - Disponível para uso e modificação.  
**Contribuições são bem-vindas!** ✨  

--- 

Feito com ❤️ por [Kleber Augusto](https://github.com/kleberimeusp)  
🔗 **GitHub**: [github.com/kleberimeusp/ai-engineer-challenge](https://github.com/kleberimeusp/ai-engineer-challenge)