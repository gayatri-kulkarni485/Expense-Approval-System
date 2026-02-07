class ApprovalRouterAgent:
    def route(self, policy_result: str, fraud_flag: bool, amount: float) -> str:
        if fraud_flag:
            return "REJECTED - POSSIBLE FRAUD"

        if policy_result == "Expense is within policy" and amount <= 2000:
            return "AUTO_APPROVED"

        return "MANAGER_APPROVAL_REQUIRED"