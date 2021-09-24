#!/usr/bin/env python
import rospy
from std_msgs.msg import Char
import random


def talker():
    pub = rospy.Publisher('chatter', Char, queue_size=10)

    rospy.init_node('talker', anonymous=True)

    rate = rospy.Rate(1)  # 1 Hz

    while not rospy.is_shutdown():
        # hello_str = "Jo haal dil ka idhar ho raha hai %s" % i
        alpha = ['a','b','c','d','e','b','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        indi = random.randint(0, 25)
        data = alpha[indi];
        # rospy.loginfo(data)
        print(f"What is the ASCII value of {data} ?")
        pub.publish(ord(data))
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
