import math

import commands2
import wpilib
import wpimath

from constants.swerve_constants import OIConstants
from subsystems.drive_subsystem import DriveSubsystem


class DriveCommand(commands2.Command):

    def __init__(self, drive_sub: DriveSubsystem) -> None:
        super().__init__()

        self.driver_controller = wpilib.Joystick(0)
        self.drive_sub = drive_sub
        self.add_requirements(self.drive_sub)

    def execute(self) -> None:
        forward = self.driver_controller.get_y()
        strafe = self.driver_controller.get_x()

        gyro_degrees = self.drive_sub.get_heading()
        gyro_radians = gyro_degrees * math.pi/180
        temp = forward * math.cos(gyro_radians) + strafe * math.sin(gyro_radians)
        strafe = -forward * math.sin(gyro_radians) + strafe * math.cos(gyro_radians)
        fwd = temp

        self.drive_sub.drive(
            wpimath.apply_deadband(
                (-self.driver_controller.get_y() * math.cos(self.drive_sub.get_heading() * (math.pi / 180))) +
                (self.driver_controller.get_x() * math.sin(self.drive_sub.get_heading() * (math.pi / 180))),
                OIConstants.kDriveDeadband
            ),
            -wpimath.apply_deadband(
                (self.driver_controller.get_y() * math.sin(self.drive_sub.get_heading() * (math.pi / 180))) +
                (self.driver_controller.get_x() * math.cos(self.drive_sub.get_heading() * (math.pi / 180))),
                OIConstants.kDriveDeadband
            ),
            -wpimath.apply_deadband(
                self.driver_controller.get_z(), OIConstants.kDriveDeadband
            ),
            False,
            False,
        )

        # ----- DRIVE CODE FROM 2024-robot-code -----

        # self.robotDrive.drive(
        #     -wpimath.applyDeadband(
        #         (self.driverController.getY() * math.sin(self.robotDrive.getHeading() * (math.pi / 180))) +
        #         (self.driverController.getX() * math.cos(self.robotDrive.getHeading() * (math.pi / 180))),
        #         OIConstants.kDriveDeadband
        #     ),
        #     -wpimath.applyDeadband(
        #         (-self.driverController.getY() * math.cos(self.robotDrive.getHeading() * (math.pi / 180))) +
        #         (self.driverController.getX() * math.sin(self.robotDrive.getHeading() * (math.pi / 180))),
        #         OIConstants.kDriveDeadband
        #     ),
        #     -wpimath.applyDeadband(
        #         self.driverController.getZ(), OIConstants.kDriveDeadband
        #     ),
        #     True,
        #     False,
        # )

    def is_finished(self) -> bool:
        return False

    def end(self, interrupted: bool) -> None:
        self.drive_sub.drive(
            0,
            0,
            0,
            False,
            False,
        )
