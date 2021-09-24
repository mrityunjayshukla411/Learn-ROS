#!/usr/bin/env python
import rospy
from std_msgs.msg import Char
def chatter_callback(message):
    rospy.loginfo(f"ASCII of  {chr(message.data)} = {message.data}")
    
def listener():
    rospy.init_node('listener', anonymous=True)
    
    rospy.Subscriber('chatter', Char, chatter_callback)
    
    rospy.spin()
    
if __name__ == '__main__' :
    listener()