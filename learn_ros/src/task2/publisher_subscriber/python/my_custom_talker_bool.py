#!/usr/bin/env python
import rospy
from std_msgs.msg import Bool
import random


def talker():
    pub = rospy.Publisher('chatter', Bool, queue_size=10)

    rospy.init_node('talker', anonymous=True)

    rate = rospy.Rate(1)  # 1 Hz

    while not rospy.is_shutdown():
        # hello_str = "Jo haal dil ka idhar ho raha hai %s" % i
        bluff = [False,True]
        indi = random.randint(0,1)
        data = bluff[indi];
        # rospy.loginfo(data)
        print(f"{data}")
        pub.publish(indi)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
