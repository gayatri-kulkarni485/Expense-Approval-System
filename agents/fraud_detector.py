class FraudDetectorAgent:
    def detect(self, amount: float) -> bool:
        if amount > 20000:
            return True
        return False