from datetime import datetime
from enum import Enum


class TransactionType(Enum):
    """Тип финансовой операции."""
    EXPENSE = "EXPENSE"
    INCOME = "INCOME"


class Transaction:
    """Класс для представления финансовой транзакции в BudgetOnTheGo."""

    def __init__(self, trans_id: int, amount: float, category_name: str, 
                 trans_type: TransactionType = TransactionType.EXPENSE, 
                 comment: str = ""):
        if amount <= 0:
            raise ValueError("Сумма транзакции должна быть больше нуля.")
        
        self.trans_id = trans_id
        self.amount = amount
        self.category_name = category_name
        self.trans_type = trans_type
        self.date = datetime.now()
        self.comment = comment

    def get_signed_amount(self) -> float:
        """Возвращает сумму со знаком (+ для доходов, - для расходов)."""
        return self.amount if self.trans_type == TransactionType.INCOME else -self.amount

    def __str__(self) -> str:
        sign = "+" if self.trans_type == TransactionType.INCOME else "-"
        return f"[{self.date.strftime('%Y-%m-%d %H:%M')}] {self.category_name}: {sign}{self.amount:.2f} руб. ({self.comment})"
