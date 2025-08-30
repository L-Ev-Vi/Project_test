class RobotVacuum:
    def __init__(self):
        self.obstacle_detected = False
        self.obstacle_type = None  # Тип препятствия
        self.known_obstacles = {"pug": {"size": "medium", "shape": "round",
        "behavior": "dynamic"}}

    def detect_obstacle(self, obstacle):
        # Simulate obstacle detection
        if obstacle in self.known_obstacles:
            self.obstacle_detected = True
            self.obstacle_type = obstacle
        else:
            self.obstacle_detected = True
            self.obstacle_type = "unknown"

    def react_to_obstacle(self):
        if not self.obstacle_detected:
            print("Препятствий не обнаружено. Продолжаю движение.")
        elif self.obstacle_type == "pug":
            print("Обнаружен питомец. Замедляюсь и аккуратно объезжаю")
        else:
            print("Неизвестное препятствие обнаружено. Выполняю обычный маневр уклонения.")

# Пример использования
vacuum = RobotVacuum()
vacuum.detect_obstacle("pug")  # Simulate detecting a pug
vacuum.react_to_obstacle()