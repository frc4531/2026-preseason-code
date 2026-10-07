import commands2

from subsystems.intake_subsystem import IntakeSubsystem


class IntakeOut(commands2.Command):

    def __init__(self, intake_sub: IntakeSubsystem) -> None:
        super().__init__()

        self.intake_sub = intake_sub
        self.add_requirements(self.intake_sub)

    def execute(self) -> None:
        self.intake_sub.set_intake_speed(-0.9)

    def is_finished(self) -> bool:
        return False

    def end(self, interrupted: bool) -> None:
        self.intake_sub.set_intake_speed(0)