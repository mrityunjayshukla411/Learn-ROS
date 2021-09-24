#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time
from std_srvs.srv import Empty


def poseCallback(pose_message):
    global x
    global y, yaw
    x = pose_message.x
    y = pose_message.y
    yaw = pose_message.theta



def move(velocity_publisher, speed, distance, is_forward):
    # declare a Twist message to send velocity commands
    velocity_message = Twist()
    # get current location
    global x, y
    x0 = x
    y0 = y

    if (is_forward):
        velocity_message.linear.x = abs(speed)
    else:
        velocity_message.linear.x = -abs(speed)

    distance_moved = 0.0
    # we publish the velocity at 1 Hz (1 time a second)
    loop_rate = rospy.Rate(1)

    while True:
        rospy.loginfo("Turtlesim moves forwards")
        velocity_publisher.publish(velocity_message)

        loop_rate.sleep()

        distance_moved = abs(math.sqrt(((x-x0) ** 2) + ((y-y0) ** 2)))
        print(distance_moved)
        print(x)
        if not (distance_moved < distance):
            rospy.loginfo("reached")
            break

    # finally, stop the robot when the distance is moved
    velocity_message.linear.x = 0
    velocity_publisher.publish(velocity_message)


def rotate(velocity_publisher, angular_speed_degree, relative_angle_degree, clockwise):

    velocity_message = Twist()

    angular_speed = math.radians(abs(angular_speed_degree))

    if (clockwise):
        velocity_message.angular.z = -abs(angular_speed)
    else:
        velocity_message.angular.z = abs(angular_speed)

    angle_moved = 0.0
    # we publish the velocity at 1 Hz (1 times a second)
    loop_rate = rospy.Rate(1)
    cmd_vel_topic = '/turtle1/cmd_vel'
    velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)

    t0 = rospy.Time.now().to_sec()
    current_angle_degree = 0
    timeTaken = relative_angle_degree/angular_speed_degree
    while (rospy.Time.now().to_sec() - t0 < timeTaken):
        rospy.loginfo("Turtlesim rotates")
        velocity_publisher.publish(velocity_message)

        # t1 = rospy.Time.now().to_sec()
        # current_angle_degree = (t1-t0)*angular_speed_degree
        loop_rate.sleep()
        print(current_angle_degree - relative_angle_degree)
    rospy.loginfo("reached")

    # finally, stop the robot when the distance is moved
    velocity_message.angular.z = 0
    velocity_publisher.publish(velocity_message)


def go_to_goal(velocity_publisher, x_goal, y_goal):
    global x
    global y, yaw

    velocity_message = Twist()

    while (True):
        K_linear = 0.5
        distance = abs(math.sqrt(((x_goal-x) ** 2) + ((y_goal-y) ** 2)))

        linear_speed = distance * K_linear

        K_angular = 4.0
        desired_angle_goal = math.atan2(y_goal-y, x_goal-x)
        angular_speed = (desired_angle_goal-yaw)*K_angular

        velocity_message.linear.x = linear_speed
        velocity_message.angular.z = angular_speed

        velocity_publisher.publish(velocity_message)
        print('x=', x, ', y=', y, ', distance to goal: ', distance)

        if (distance < 0.01):
            break


def setDesiredOrientation(publisher, speed_in_degree, desired_angle_degree):
    relative_angle_radians = math.radians(desired_angle_degree) - yaw
    clockwise = 0
    if relative_angle_radians < 0:
        clockwise = 1
    else:
        clockwise = 0
    print("relative_angle_radians: ", math.degrees(relative_angle_radians))
    print("desired_angle_degree: ", desired_angle_degree)
    rotate(publisher, speed_in_degree, math.degrees(
        abs(relative_angle_radians)), clockwise)



def half_circle(velocity_publisher, speed, radius):
    vel_msg = Twist()
    loop_rate = rospy.Rate(1)
    t0 = rospy.Time.now().to_sec()
    timeTaken = 3.14159265359*radius/speed
    print("time taken ", timeTaken)
    while(timeTaken-(rospy.Time.now().to_sec() - t0 ) >0.4):
        print("time taken ", rospy.Time.now().to_sec() - t0 )
        vel_msg.linear.x = speed
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = -speed/radius
        velocity_publisher.publish(vel_msg)
        loop_rate.sleep()

    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)
    print(rospy.Time.now().to_sec()-t0)


def letterD(velocity_publisher):
    setDesiredOrientation(velocity_publisher, 45, 90)
    move(velocity_publisher, 1, 8, True)
    setDesiredOrientation(velocity_publisher, 45, 0)
    half_circle(velocity_publisher, 4, 3.9999999999999999999999999999)

def hexagon(velocity_publisher):
    
    speed = 1
    move(velocity_publisher, speed, 2, True)
    rotate(velocity_publisher, 60, 60, False)
    move(velocity_publisher, speed, 2, True)
    rotate(velocity_publisher, 60, 60, False)
    move(velocity_publisher, speed, 2, True)
    rotate(velocity_publisher, 60, 60, False)
    move(velocity_publisher, speed, 2, True)
    rotate(velocity_publisher, 60, 60, False)
    move(velocity_publisher, speed, 2, True)
    rotate(velocity_publisher, 60, 60, False)
    move(velocity_publisher, speed, 2, True)
    



if __name__ == '__main__':
    try:

        rospy.init_node('turtlesim_motion_pose', anonymous=True)

        # declare velocity publisher
        cmd_vel_topic = '/turtle1/cmd_vel'
        velocity_publisher = rospy.Publisher(
            cmd_vel_topic, Twist, queue_size=10)

        position_topic = "/turtle1/pose"
        pose_subscriber = rospy.Subscriber(position_topic, Pose, poseCallback)
        time.sleep(2)

        # move(velocity_publisher, 1.0, 9.0, True)
        # rotate(velocity_publisher, 45, 90, False)
        # go_to_goal(velocity_publisher, 9.0, 9.0)
        # setDesiredOrientation(velocity_publisher, 10, 90)
        # letterD(velocity_publisher)
        hexagon(velocity_publisher)
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")
