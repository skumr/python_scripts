"""This program allows for a user to create a Robot object and
operate it using class methods up, down, left, right. The user can
also find the distance of the robot from its current location and
the origin. The program already moves the robot up 5 units, down 3 units,
right 2 units, and left 2 units"""

import math as m


def RobotMoves():
    class Coordinate:

        def __init__(self):
            self.point = [0, 0]

        def up(self, u):
            self.point[1] += 1 * u
            return self.point

        def down(self, d):
            self.point[1] -= 1 * d
            return self.point

        def right(self, r):
            self.point[0] += 1 * r
            return self.point

        def left(self, l):
            self.point[0] -= 1 * l
            return self.point

        def distance(self):
            x = self.point[0]
            y = self.point[1]

            distance = m.sqrt(x ** 2 + y ** 2)

            return distance

    robot = Coordinate()
    robot.up(5)
    robot.down(3)
    robot.right(2)
    robot.left(3)

    print(robot.point, robot.distance())
