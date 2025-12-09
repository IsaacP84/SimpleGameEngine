from entities.entity import Entity

class CanHold:
    def __init__(self):
        self.offset:tuple[float,float,float] = (0, 0, 0)
        self.obj: Entity | None = None
        pass

    def hold(self, obj: Entity):
        if not obj.components.get("CanBeHeld"):
            return False
        self.obj = obj
        obj.components["CanBeHeld"].holder = self
        return True


class CanBeHeld:
    def __init__(self):
        self.holder: Entity | None = None
