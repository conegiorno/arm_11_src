# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('maze_goal_info')
        self.subscription = self.create_subscription(
            Float32,
            'referee/distance_left',
            self.distance_callback,
            10)
        self.subscription = self.create_subscription(
            Float32,
            'referee/time_elapsed',
            self.time_callback,
            10)
        self.subscription  # prevent unused variable warning
        timer_period = 2.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.goal_reached_flag = False
        self.act_dist = 0.0
        self.act_time = 0.0
        self.goal_thrs = 0.25
        self.run_time = 0.0

    def distance_callback(self, msg):
        self.act_dist = msg.data

    def time_callback(self, msg):
        self.act_time = msg.data

    def timer_callback(self):
        if self.goal_reached_flag == True:
            pass
        else:
            self.get_logger().info(f'Odległość do celu: {self.act_dist:.2f} m.')
            self.get_logger().info(f'Czas od startu: {self.act_time:.2f} sek.')
            if self.act_dist <= self.goal_thrs:
                self.goal_reached_flag = True
                self.run_time = self.act_time
                self.get_logger().info(f'CEL OSIĄGNIĘTY !!!')
                self.get_logger().info(f'Przejście labiruntu trwało: {self.run_time:.2f} sek.')
        


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
