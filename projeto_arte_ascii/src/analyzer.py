from .services import LipsLineDetector, DressPolkadotCounter, ConsoleArtRenderer
from .models import PolkadotScoreResult
from typing import List

class PolkadotAnalyzer:
    def __init__(self):
        self.detector = LipsLineDetector()
        self.counter = DressPolkadotCounter()
        self.renderer = ConsoleArtRenderer()
    
    def analyze(self, ascii_art: List[str]) -> PolkadotScoreResult:
        self.renderer.render(ascii_art)
        lips_coords = self.detector.detect(ascii_art)
        result = self.counter.count(ascii_art, lips_coords)
        
        print(f"\nPontos normais: {result.normal_count}")
        print(f"Pontos duplos: {result.double_count}")
        print(f"Pontuação total: {result.total_score}")
        return result