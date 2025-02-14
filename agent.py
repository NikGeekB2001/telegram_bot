class SimpleAgent:
    def __init__(self):
        self.knowledge = {}  # Знания агента
        self.state = "idle"  # Текущее состояние

    def perceive(self, environment):
        # Получение информации из окружения
        # Прямое обновление знаний из словаря
        self.knowledge.update(environment)

    def decide(self):
        # Принятие решения на основе знаний
        if self.knowledge.get("task") == "learn":
            return "study"
        elif self.knowledge.get("task") == "help":
            return "assist"
        return "wait"

    def act(self, action):
        # Выполнение действия
        self.state = action
        return f"Agent is {action}"

    def run(self):
        # Метод для демонстрации работы агента
        print("Агент запущен!")

        # Создаем тестовое окружение
        environment = {"task": "learn", "context": "education"}

        # Демонстрация цикла работы агента
        self.perceive(environment)
        action = self.decide()
        result = self.act(action)

        print(f"Результат: {result}")
        print(f"Состояние знаний: {self.knowledge}")
        print(f"Текущее состояние: {self.state}")


# Пример использования
if __name__ == "__main__":
    agent = SimpleAgent()
    agent.run()
