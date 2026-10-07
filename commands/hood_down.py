import commands2

from subsystems.turret_subsystem import TurretSubsystem


class HoodDown(commands2.Command):

    def __init__(self, turret_sub: TurretSubsystem) -> None:
        super().__init__()

        self.turret_sub = turret_sub
        self.add_requirements(self.turret_sub)

    def execute(self) -> None:
        self.turret_sub.set_hood_speed(-0.1)

    def is_finished(self) -> bool:
        return False

    def end(self, interrupted: bool) -> None:
        self.turret_sub.set_hood_speed(0)