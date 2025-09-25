import unittest
from src.models import LipsCoordinates, PolkadotScoreResult
from src.services import LipsLineDetector, DressPolkadotCounter
from src.analyzer import PolkadotAnalyzer

class TestPolkadotAnalysis(unittest.TestCase):
    def setUp(self):
        self.sample_art = [
            "  O  O  ",
            " –––– ",
            "O   O  O"
        ]
        self.analyzer = PolkadotAnalyzer()

    def test_lip_detection(self):
        detector = LipsLineDetector()
        coords = detector.detect(self.sample_art)
        self.assertEqual(coords.line_index, 1)

    def test_polkadot_count(self):
        detector = LipsLineDetector()
        counter = DressPolkadotCounter()
        coords = detector.detect(self.sample_art)
        result = counter.count(self.sample_art, coords)
        self.assertEqual(result.total_score, 5)

    def test_full_analysis(self):
        result = self.analyzer.analyze(self.sample_art)
        self.assertIsInstance(result, PolkadotScoreResult)

if __name__ == "__main__":
    unittest.main()