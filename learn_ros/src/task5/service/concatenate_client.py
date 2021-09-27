#!/usr/bin/env python

import sys
import rospy
from learn_ros.srv import ConcatenateTwoStrings
from learn_ros.srv import ConcatenateTwoStringsRequest
from learn_ros.srv import ConcatenateTwoStringsResponse

def concate_two_strings_clients(x, y):
    rospy.wait_for_service('concatenate_two_strings')
    try:
        concatenate_two_strings = rospy.ServiceProxy('concatenate_two_strings', ConcatenateTwoStrings)
        resp1 = concatenate_two_strings(x, y)
        return resp1.conc
    except rospy.ServiceException(e):
        print ("Service call failed: %s"%e)

def usage():
    return 

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = (sys.argv[1])
        y = (sys.argv[2])
    else:
        print ("%s [x y]"%sys.argv[0])
        sys.exit(1)
    print ("Requesting %s+%s"%(x, y))
    s = concate_two_strings_clients(x, y)
    print ("%s + %s = %s"%(x, y, s))
