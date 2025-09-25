from typing import List
from .models import LipsCoordinates, PolkadotScoreResult

class LipsLineDetector:
    def detect(self, ascii_lines: List[str]) -> LipsCoordinates:
        for idx, line in enumerate(ascii_lines):
            if '–' in line:
                return LipsCoordinates(
                    line_index=idx,
                    start_x=line.find('–'),
                    end_x=line.rfind('–')
                )
        raise ValueError("Linha dos lábios não encontrada")

class DressPolkadotCounter:
    def count(self, ascii_lines: List[str], lips_coords: LipsCoordinates) -> PolkadotScoreResult:
        normal = 0
        double = 0
        
        for y, line in enumerate(ascii_lines):
            for x, char in enumerate(line):
                if char == 'O':
                    if lips_coords.start_x <= x <= lips_coords.end_x:
                        double += 1
                    else:
                        normal += 1
        
        return PolkadotScoreResult(
            total_score=normal + (double * 2),
            normal_count=normal,
            double_count=double
        )

class ConsoleArtRenderer:
    def render(self, ascii_lines: List[str]) -> None:
        for line in ascii_lines:
            print(line)