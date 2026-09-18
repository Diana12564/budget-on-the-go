class Category:
    """Класс для категории финансовых операций."""

    def __init__(self, category_id: int, name: str, icon: str = "default_icon"):
        self.category_id = category_id
        self.name = name.strip()
        self.icon = icon

    def __eq__(self, other) -> bool:
        if isinstance(other, Category):
            return self.name.lower() == other.name.lower()
        return False

    def __repr__(self) -> str:
        return f"Category(id={self.category_id}, name='{self.name}', icon='{self.icon}')"
