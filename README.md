# **Projeto Arte ASCII - Analisador de Polkadots**  

Este projeto implementa um sistema de análise de arte ASCII que identifica e conta *polkadots* seguindo regras específicas de pontuação. Desenvolvido como parte de um desafio de engenharia de IA, ele demonstra:  

✅ **Arquitetura limpa** (separação de modelos, serviços e lógica principal)  
✅ **Testabilidade** (testes unitários para todas as componentes)  
✅ **Extensibilidade** (fácil adaptação para novos formatos de arte)  

---

## 📂 **Estrutura do Projeto**  
```
/projeto_arte_ascii/
│
├── /data/                     # Camada de dados
│   └── angelica_art.txt       # Arte ASCII original
│
├── /src/                      # Código fonte principal
│   ├── __init__.py
│   ├── models.py              # Data classes (LipsCoordinates, PolkadotScoreResult)
│   ├── services.py            # Serviços (detector, contador, renderizador)
│   ├── analyzer.py            # Lógica central (PolkadotAnalyzer)
│   └── main.py                # Ponto de entrada CLI
│
├── /tests/                    # Testes unitários
│   ├── __init__.py
│   └── test_analyzer.py       # Testes de integração
│
├── .gitignore
├── requirements.txt           # Dependências (Python 3.8+)
└── README.md                  # Documentação
```

---

## ⚙️ **Instalação e Uso**  

### Pré-requisitos  
- Python 3.8+  
- Git (opcional)  

### Passos:  
```bash
# 1. Clone o repositório (ou baixe manualmente)
git clone https://github.com/kleberimeusp/ai-engineer-challenge.git
cd ai-engineer-challenge/projeto_arte_ascii

# 2. Configure o ambiente (recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 3. Instale dependências
pip install -r requirements.txt

# 4. Execute o analisador
python -m src.main
```

**Saída esperada:**  
```plaintext
=== Arte ASCII ===
(Arte renderizada no terminal...)
=== Resultados ===
🔵 Pontos normais: 23
🔴 Pontos duplos: 12
🏆 Pontuação total: 47
```

---

## 🧠 **Design Técnico**  

### Camadas Principais  
| Arquivo       | Função                                |  
|---------------|---------------------------------------|  
| `models.py`   | Define estruturas de dados imutáveis (`@dataclass`) |  
| `services.py` | Contém:  <br> • `LipsLineDetector` (detecta `–`)<br> • `DressPolkadotCounter` (conta `O`)<br> • `ConsoleArtRenderer` |  
| `analyzer.py` | Orquestra o fluxo: `detect() → count() → render()` |  

### Regras de Negócio  
- **Linha dos lábios**: Identificada pelo caractere `–`  
- **Pontuação**:  
  - `O` fora dos lábios → **1 ponto**  
  - `O` entre `start_x` e `end_x` → **2 pontos**  

---

## 🧪 **Testes**  
```bash
# Execute todos os testes
python -m unittest discover tests
```  
**Cobertura:**  
✔ Testes para detecção de lábios  
✔ Validação da contagem de pontos  
✔ Cálculo correto da pontuação  

---

## 🛠 **Extensibilidade**  
### Casos de Uso Avançados  
```python  
# Exemplo: Adicionar suporte a JSON  
class JSONExporter:  
    def export(self, result: PolkadotScoreResult) -> str:  
        return json.dumps(asdict(result))  

# Uso:  
analyzer = PolkadotAnalyzer(exporter=JSONExporter())  
```  

---

## 📜 **Licença**  
MIT License - Disponível para uso e modificação.  

**Desenvolvido por:** [Kleber I.](https://github.com/kleberimeusp)  
**Repositório:** [github.com/kleberimeusp/ai-engineer-challenge](https://github.com/kleberimeusp/ai-engineer-challenge)  

--- 

✨ **Dúvidas?** Abra uma *issue* no GitHub!