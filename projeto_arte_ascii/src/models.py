from dataclasses import dataclass
from typing import List

@dataclass
class LipsCoordinates:
    line_index: int
    start_x: int
    end_x: int

@dataclass
class PolkadotScoreResult:
    total_score: int
    normal_count: int
    double_count: int