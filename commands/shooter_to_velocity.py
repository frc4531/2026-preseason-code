import commands2
import ntcore
import rev
from rev import SparkFlexConfig, SparkBase

from subsystems.shooter_subsystem import ShooterSubsystem


class ShooterToVelocity(commands2.Command):

    def __init__(self, shooter_sub: ShooterSubsystem, target_position) -> None:
        super().__init__()

        self.target_position = target_position

        self.shooter_sub = shooter_sub
        self.add_requirements(self.shooter_sub)
        nt_instance = ntcore.NetworkTableInstance.get_default()
        shoot_table = nt_instance.get_table("shoot_table")

        self.far_shoot = shoot_table.get_double_topic("far_shoot").publish()
        self.near_shoot = shoot_table.get_double_topic("near_shoot").publish()
        #self.target_position = shoot_table.getDoubleTopic("velocity").publish()


    def execute(self) -> None:
        self.shooter_sub.set_shooter_velocity(self.target_position)
        if self.target_position == 6500:
            self.near_shoot.set(False)
            self.far_shoot.set(True)
        elif self.target_position == 3000:
            self.near_shoot.set(True)
            self.far_shoot.set(False)

    def is_finished(self) -> bool:
        return False

    def end(self, interrupted: bool) -> None:
        self.shooter_sub.set_shooter_speed(0)

        self.far_shoot.set(False)
        self.near_shoot.set(False)