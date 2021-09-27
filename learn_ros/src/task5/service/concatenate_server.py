#!/usr/bin/env python

from learn_ros.srv import ConcatenateTwoStrings
from learn_ros.srv import ConcatenateTwoStringsRequest
from learn_ros.srv import ConcatenateTwoStringsResponse
import rospy

def handle_two_strings(req):
    print ("Returning [%s + %s = %s]"%(req.s1, req.s2, (req.s1 + req.s2)))
    conca = req.s1 + req.s2
    return ConcatenateTwoStringsResponse(conca)

def concate_two_strings_server():
    rospy.init_node('concate_two_strings_server')
    s = rospy.Service('concatenate_two_strings', ConcatenateTwoStrings, handle_two_strings)
    print ("Ready to concatenate two strings.")
    rospy.spin()
    
if __name__ == "__main__":
    concate_two_strings_server()
