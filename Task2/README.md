# Task 2 Submission
ROS [package](https://github.com/mrityunjayshukla411/Learn-ROS/tree/main/learn_ros)  
## [Writing code for publisher and subscriber and testing them with different data types](https://github.com/mrityunjayshukla411/Learn-ROS/tree/main/learn_ros/src/task2/publisher_subscriber)  
* Basic [publisher](https://github.com/mrityunjayshukla411/Learn-ROS/blob/main/learn_ros/src/task2/publisher_subscriber/python/my_custom_listner_int.py) and [subscriber](https://github.com/mrityunjayshukla411/Learn-ROS/blob/main/learn_ros/src/task2/publisher_subscriber/python/my_custom_listner_int.py) code with use of Int16 data type 

```
  roscd learn_ros/src/task2/publisher_subscriber/python
  chmod +x my_custom_talker_int.py
  chmod +x my_custom_listner_int.py
  cd
  roscore 
  rosrun learn_ros my_custom_listner_int.py #(in new terminal)
  rosrun learn_ros my_custom_talker_int.py #(in new terminal)
```
![](https://github.com/mrityunjayshukla411/Learn-ROS/blob/main/Task2/data/pub_sub_int.png)  

* Basic [publisher](https://github.com/mrityunjayshukla411/Learn-ROS/blob/main/learn_ros/src/task2/publisher_subscriber/python/my_custom_talker_char.py) and [subscriber](https://github.com/mrityunjayshukla411/Learn-ROS/blob/main/learn_ros/src/task2/publisher_subscriber/python/my_custom_listner_char.py) code with use of Char data type 

```
  roscd learn_ros/src/task2/publisher_subscriber/python
  chmod +x my_custom_talker_char.py
  chmod +x my_custom_listner_char.py
  cd
  roscore 
  rosrun learn_ros my_custom_listner_char.py #(in new terminal)
  rosrun learn_ros my_custom_talker_char.py #(in new terminal)
```
![](https://github.com/mrityunjayshukla411/Learn-ROS/blob/main/Task2/data/pub_sub_char.png)    


* Basic [publisher](https://github.com/mrityunjayshukla411/Learn-ROS/blob/main/learn_ros/src/task2/publisher_subscriber/python/my_custom_talker_bool.py) and [subscriber](https://github.com/mrityunjayshukla411/Learn-ROS/blob/main/learn_ros/src/task2/publisher_subscriber/python/my_custom_listner_bool.py) code with use of Char data type 

```
  roscd learn_ros/src/task2/publisher_subscriber/python
  chmod +x my_custom_talker_bool.py
  chmod +x my_custom_listner_bool.py
  cd
  roscore 
  rosrun learn_ros my_custom_listner_bool.py #(in new terminal)
  rosrun learn_ros my_custom_talker_bool.py #(in new terminal)
```
![](https://github.com/mrityunjayshukla411/Learn-ROS/blob/main/Task2/data/pub_sub_bool.png)  

* Publishing [messages](https://github.com/mrityunjayshukla411/Learn-ROS/tree/main/learn_ros/msg)

```
  roscd learn_ros/
  mkdir msg
  echo "int64 num" > msg/num.msg
  cd
  roscore 
  rosmsg show learn_ros/num #(in new terminal)
  rosmsg show learn_ros/custom_messge #(in new terminal)
```
![](https://github.com/mrityunjayshukla411/Learn-ROS/blob/main/Task2/data/msgs.png)  

* [Services](https://github.com/mrityunjayshukla411/Learn-ROS/tree/main/learn_ros/srv)

```
  roscd learn_ros/
  mkdir srv
  roscp rospy_tutorials AddTwoInts.srv srv/AddTwoInts.srv
  cd
  roscore 
  rossrv show learn_ros/AddTwoInts #(in new terminal)
```
![](https://github.com/mrityunjayshukla411/Learn-ROS/blob/main/Task2/data/service.png) 

