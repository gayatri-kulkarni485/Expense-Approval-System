import json

class PolicyCheckerAgent:
    def __init__(self):
        with open("data/policies.json") as f:
            self.policies = json.load(f)

    def check(self, category: str, amount: float) -> str:
        limit = self.policies.get(f"max_{category}", 0)

        if amount <= limit:
            return "Expense is within policy"
        return "Expense exceeds policy"