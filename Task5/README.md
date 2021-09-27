# Task 3 Submission
ROS [package](https://github.com/mrityunjayshukla411/Learn-ROS/tree/main/learn_ros)  
## [Creating a ROS node control the turtlesim bot](https://github.com/mrityunjayshukla411/Learn-ROS/blob/main/learn_ros/src/task3/turtlesim_motions.py)  

### Important Imports  
  ```
  import rospy
  from geometry_msgs.msg import Twist
  from turtlesim.msg import Pose
  import math
  import time
  from std_srvs.srv import Empty
  ```

### Callback Function 
  ```
  def poseCallback(pose_message):
    global x
    global y, yaw
    x = pose_message.x
    y = pose_message.y
    yaw = pose_message.theta
  ```

* Moving the turtlesim bot in a straight line for a given distance  

  * Python Function Used  
  
    ```
    
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
    ```
  * Calling the above function
    ```
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

        move(velocity_publisher, 1.0, 9.0, True)
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")
    ```
  * Running the python script
    ```
    roscd learn_ros/src/task3/
    chmod +x turtlesim_motions.py
    cd
    roscore 
    rosrun turtlesim turtlesim_node #(in new terminal)
    rosrun learn_ros turtlesim_motions.py #(in new terminal)
    ```
![](https://github.com/mrityunjayshukla411/Learn-ROS/blob/main/Task3/data/move.png)  

* Rotating the turtlesim bot in it's place by a given angle and angular speed

  * Python Function Used  
  
    
    ```
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
    
    ```
  * Calling the above function
    ```
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

        rotate(velocity_publisher, 45, 90, False)
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")
    ```
  * Running the python script
    ```
    roscore 
    rosrun turtlesim turtlesim_node #(in new terminal)
    rosrun learn_ros turtlesim_motions..py #(in new terminal)
    ```
![](https://github.com/mrityunjayshukla411/Learn-ROS/blob/main/Task3/data/rotate.png)  



* Travelling to a given location

  * Python Function Used  
    
    ```
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
    
    ```
  * Calling the above function
    ```
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

        go_to_goal(velocity_publisher, 9.0, 9.0)
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")
    ```
  * Running the python script
    ```
    roscore 
    rosrun turtlesim turtlesim_node #(in new terminal)
    rosrun learn_ros turtlesim_motions..py #(in new terminal)
    ```
![](https://github.com/mrityunjayshukla411/Learn-ROS/blob/main/Task3/data/go_to_goal.png)  


## [Drawing the letter 'D' using the turtle bot](https://github.com/mrityunjayshukla411/Learn-ROS/blob/main/learn_ros/src/task3/turtlesim_motions.py)

  * Python Function Used  
    
    ```
    def letterD(velocity_publisher):
    setDesiredOrientation(velocity_publisher, 45, 90)
    move(velocity_publisher, 1, 8, True)
    setDesiredOrientation(velocity_publisher, 45, 0)
    half_circle(velocity_publisher, 4, 3.9999999999999999999999999999)
    ```
  * Calling the above function
    ```
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

        letterD(velocity_publisher)
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")
    ```
  * Running the python script
    ```
    roscore 
    rosrun turtlesim turtlesim_node #(in new terminal)
    rosrun learn_ros turtlesim_motions..py #(in new terminal)
    ```
![](https://github.com/mrityunjayshukla411/Learn-ROS/blob/main/Task3/data/letterD.png)  

## [Drawing a hexagon using the turtle bot](https://github.com/mrityunjayshukla411/Learn-ROS/blob/main/learn_ros/src/task3/turtlesim_motions.py)

  * Python Function Used  
    
    ```
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
    ```
  * Calling the above function
    ```
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

        hexagon(velocity_publisher)
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")
    ```
  * Running the python script
    ```
    roscore 
    rosrun turtlesim turtlesim_node #(in new terminal)
    rosrun learn_ros turtlesim_motions..py #(in new terminal)
    ```
![](https://github.com/mrityunjayshukla411/Learn-ROS/blob/main/Task3/data/hexagon.png)  
