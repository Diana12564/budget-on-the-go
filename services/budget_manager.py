from typing import List, Dict
from models.transaction import Transaction, TransactionType
from models.budget_limit import BudgetLimit


class BudgetManager:
    """Управляющий класс бизнес-логики приложения BudgetOnTheGo."""

    def __init__(self):
        self.transactions: List[Transaction] = []
        self.limits: Dict[str, BudgetLimit] = {}

    def add_transaction(self, transaction: Transaction) -> str:
        """Добавляет транзакцию и проверяет соблюдение лимитов."""
        self.transactions.append(transaction)
        
        if transaction.trans_type == TransactionType.EXPENSE:
            cat = transaction.category_name
            if cat in self.limits:
                spent = self.get_total_spent_by_category(cat)
                status = self.limits[cat].calculate_usage(spent)
                
                if status["is_exceeded"]:
                    return f"ВНИМАНИЕ! Лимит по категории '{cat}' превышен на {spent - status['limit']:.2f} руб.!"
                elif status["is_warning"]:
                    return f"ПРЕДУПРЕЖДЕНИЕ: Вы израсходовали {status['percentage']}% лимита по категории '{cat}'."
        
        return "Транзакция успешно добавлена."

    def get_balance(self) -> float:
        """Рассчитывает текущий общий баланс пользователя."""
        return sum(t.get_signed_amount() for t in self.transactions)

    def get_total_spent_by_category(self, category_name: str) -> float:
        """Возвращает сумму всех расходов по конкретной категории."""
        return sum(
            t.amount for t in self.transactions 
            if t.trans_type == TransactionType.EXPENSE and t.category_name.lower() == category_name.lower()
        )

    def set_limit(self, limit: BudgetLimit):
        """Устанавливает лимит расходов на категорию."""
        self.limits[limit.category_name] = limit
