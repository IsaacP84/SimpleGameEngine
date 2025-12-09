from entities.entity import Entity
from uuid import UUID
import config
class CanHold:
    def __init__(self):
        self.offset:tuple[float,float,float] = (0, 0, 0)
        self.obj_id: UUID | None = None
        pass

    def hold(self, target:Entity, obj: Entity):
        if not obj.components.get("CanBeHeld"):
            return False
        self.obj_id = config.app.engine.getId(obj)
        obj.components["CanBeHeld"].holder_id = config.app.engine.getId(target)
        return True


class CanBeHeld:
    def __init__(self):
        self.holder_id: UUID | None = None
