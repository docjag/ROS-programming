#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32

def callback_func(message):
    """ Callback function"""
    
    rospy.loginfo(f"rospy.get_caller_id() : {message.data}")
    # rospy.loginfo(f"rospy.get_caller_id() : {message.frequency}")  # user defined message

def freq_sub():
    """ listener function"""
    
    # Create and Initialize a ROS Node
    rospy.init_node('freq_sub_node', anonymous=True)
    
    # Create a Subscriber Object
    rospy.Subscriber("frequency", Float32, callback_func)
    
    # Start Listening
    # spin() simply keeps Python from exiting until this node is stopped
    rospy.spin()
    
if __name__ == '__main__':
    freq_sub()
