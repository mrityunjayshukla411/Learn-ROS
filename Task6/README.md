# Task 6
## Turtlebot3 Installation 

### Follow the steps given below to install turtlebot3 in ROS-Noetic
  * Check for updates before starting the installation process  
    ```
    sudo apt-get update
    sudo apt-get upgrade
    ```
  * Navigate to the src directory in you Catkin workspace
    ```
    cd ~/catkin_ws/src/
    ```
  * Now we clone the turtlebot3 repositories in the present working directory
    ```
    git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git -b noetic-devel
    git clone https://github.com/ROBOTIS-GIT/turtlebot3.git -b noetic-devel
    ```
  * After that we just navigate to the Catkin workspace directory and catkin_make
    ```
    cd ~/catkin_ws && catkin_make
    ```
  * Now for installing the turtlebot3 simulator enter the commands given below
    ```
    cd ~/catkin_ws/src/
    git clone https://github.com/ROBOTIS-GIT/turtlebot3_simulations
    cd ~/catkin_ws && catkin_make
    
    ```
  * Now we have to make some changes to the .bashrc file append the given commands into your .bashrc file
    ```
    # <<< ROS <<< 
    source /opt/ros/noetic/setup.bash
    source /home/kalishasur/catkin_ws/devel/setup.bash
    export TURTLEBOT3_MODEL=waffle
    export SVGA_VGPU10=0 
    ```
      The last command is for virtual machine users
  * You can verify the installation my running the following commands
    ```
    roscore
    roslaunch turtlebot3_gazebo turtlebot3_world.launch #(in new terminal)
    ```
    ![](https://github.com/mrityunjayshukla411/Learn-ROS/blob/main/Task6/data/installationConfirmation.png)
   
