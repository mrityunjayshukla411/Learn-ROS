#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16
def chatter_callback(message):
    rospy.loginfo(f"Square of {message.data} = {message.data**2}")
    
def listener():
    rospy.init_node('listener', anonymous=True)
    
    rospy.Subscriber('chatter', Int16, chatter_callback)
    
    rospy.spin()
    
if __name__ == '__main__' :
    listener()