#!/usr/bin/env python
import rospy
from std_msgs.msg import Bool
def chatter_callback(message):
        rospy.loginfo(message.data)
    
def listener():
    rospy.init_node('listener', anonymous=True)
    
    rospy.Subscriber('chatter', Bool, chatter_callback)
    
    rospy.spin()
    
if __name__ == '__main__' :
    listener()