import commands2

from subsystems.intake_subsystem import IntakeSubsystem


class IntakeFeeder(commands2.Command):

    def __init__(self, intake_sub: IntakeSubsystem) -> None:
        super().__init__()

        self.intake_sub = intake_sub
        self.add_requirements(self.intake_sub)

    def execute(self) -> None:
        self.intake_sub.top_intake_motor.set(-0.9)
        self.intake_sub.bottom_intake_motor.set(0.9)

    def is_finished(self) -> bool:
        return False

    def end(self, interrupted: bool) -> None:
        self.intake_sub.set_intake_speed(0)