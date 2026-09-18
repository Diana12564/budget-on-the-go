class BudgetLimit:
    """Класс для контроля ежемесячных лимитов бюджета по категориям."""

    def __init__(self, limit_id: int, category_name: str, limit_amount: float):
        if limit_amount <= 0:
            raise ValueError("Лимит должен быть положительным числом.")
        self.limit_id = limit_id
        self.category_name = category_name
        self.limit_amount = limit_amount

    def calculate_usage(self, current_spent: float) -> dict:
        """Возвращает процент использования лимита и статус предупреждения."""
        percentage = (current_spent / self.limit_amount) * 100
        is_exceeded = current_spent >= self.limit_amount
        is_warning = percentage >= 80.0 and not is_exceeded

        return {
            "spent": current_spent,
            "limit": self.limit_amount,
            "percentage": round(percentage, 1),
            "is_warning": is_warning,
            "is_exceeded": is_exceeded
        }
