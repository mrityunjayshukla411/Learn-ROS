# Task 5 Submission
ROS [package](https://github.com/mrityunjayshukla411/Learn-ROS/tree/main/learn_ros)  
## Creating client-server models

  ### Add two integers and return their sum  
  * [service](https://github.com/mrityunjayshukla411/Learn-ROS/blob/main/learn_ros/srv/AddTwoInts.srv)
  * [client code](https://github.com/mrityunjayshukla411/Learn-ROS/blob/main/learn_ros/src/task5/service/add_client.py)
  * [server code](https://github.com/mrityunjayshukla411/Learn-ROS/blob/main/learn_ros/src/task5/service/add_server.py)

    ```
      roscore
      chmod +x add_server.py
      chmod +x add_client.py
      rosrun learn_ros add_server.py # (in new terminal)
      rosrun learn_ros add_client.py 23 46 # (in new terminal)
    ```
    ![](https://github.com/mrityunjayshukla411/Learn-ROS/blob/main/Task5/data/add_two_ints.png)
  ### Concatenate two strings and return the concatenated string  
  * [service](https://github.com/mrityunjayshukla411/Learn-ROS/blob/main/learn_ros/srv/ConcatenateTwoStrings.srv)
  * [client code](https://github.com/mrityunjayshukla411/Learn-ROS/blob/main/learn_ros/src/task5/service/concatenate_client.py)
  * [server code](https://github.com/mrityunjayshukla411/Learn-ROS/blob/main/learn_ros/src/task5/service/concatenate_server.py)

    ```
      roscore
      chmod +x concatenate_server.py
      chmod +x concatenate_client.py
      rosrun learn_ros concatenate_server.py # (in new terminal)
      rosrun learn_ros concatenate_client.py cool_ dude # (in new terminal)
    ```
    ![](https://github.com/mrityunjayshukla411/Learn-ROS/blob/main/Task5/data/concatenate_two_strings.png)
    
    
