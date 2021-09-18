#!/usr/bin/env python
import rospy
# from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time
from std_srvs.srv import Empty
x = 0
y = 0
z = 0
yaw = 0


def poseCallback(poseMessage):
    global x
    global y, z, yaw
    x = poseMessage.x
    y = poseMessage.y
    yaw = poseMessage.theta


def motion(speed, distance):
    velocity_message = Twist()
    # get current location
    x0 = x
    y0 = y
    # z0=z;
    # yaw0=yaw;
    velocity_message.linear.x = speed
    distance_moved = 0.0
    # we publish the velocity at 10 Hz (10 times a second)
    loop_rate = rospy.Rate(1)
    cmd_vel_topic = '/turtle1/cmd_vel'
    velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)
    while True:
        rospy.loginfo("Turtlesim moves forwards")
        velocity_publisher.publish(velocity_message)
        loop_rate.sleep()

        # rospy.Duration(1.0)

        distance_moved = distance_moved + \
            abs(0.5 * math.sqrt(((x-x0) ** 2) + ((y-y0) ** 2)))
        if not (distance_moved < distance):
            rospy.loginfo("reached")
            break

        # finally, stop the robot when the distance is moved
        velocity_message.linear.x = 0
        velocity_publisher.publish(velocity_message)


if __name__ == '__main__':
    try:

        rospy.init_node('turtlesim_motion_pose', anonymous=True)
        # declare velocity publisher
        cmd_vel_topic = '/turtle1/cmd_vel'
        velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)

        position_topic = "/turtle1/pose"
        pose_subscriber = rospy.Subscriber(position_topic, Pose, poseCallback)
        time.sleep(2)
        motion(1.0, 5.0)
        time.sleep(2)
        rospy.wait_for_service('reset')
        reset_turtle = rospy.ServiceProxy('reset', Empty)
        reset_turtle()
        rospy.spin()

    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")
