#!/usr/bin/env python
import rospy
from std_msgs.msg import String


def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)

    rospy.init_node('talker', anonymous=True)

    rate = rospy.Rate(1)  # 1 Hz

    i = 0
    while not rospy.is_shutdown():
        hello_str = "Jo haal dil ka idhar ho raha hai %s" % i
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
        i = i + 1


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
