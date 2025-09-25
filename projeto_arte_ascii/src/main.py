import os
import sys
from pathlib import Path
from src.analyzer import PolkadotAnalyzer

def load_art(file_path: str) -> list[str]:
    """Carrega a arte ASCII de um arquivo com tratamento de erros"""
    try:
        # Obtém o caminho absoluto do diretório do arquivo main.py
        base_dir = Path(__file__).parent.parent
        art_path = base_dir / 'data' / file_path
        
        if not art_path.exists():
            raise FileNotFoundError(f"Arquivo de arte não encontrado: {art_path}")
            
        with open(art_path, 'r', encoding='utf-8') as f:
            return [line.rstrip('\n') for line in f]
            
    except UnicodeDecodeError:
        sys.stderr.write("Erro: Problema de codificação no arquivo de arte (use UTF-8)\n")
        raise
    except Exception as e:
        sys.stderr.write(f"Erro ao carregar arte: {str(e)}\n")
        raise

def main():
    try:
        analyzer = PolkadotAnalyzer()
        art = load_art('angelica_art.txt')
        result = analyzer.analyze(art)
        return result
    except Exception as e:
        sys.stderr.write(f"\nErro durante a análise: {str(e)}\n")
        sys.exit(1)

if __name__ == "__main__":
    main()