#!/usr/bin/env python

import sys
import rospy
import random
import rostest
import unittest
from std_msgs.msg import Float32


PKG = 'test_roslaunch'


class TestFreqPub(unittest.TestCase):

    publish_ok = False

    def callback_func(self):
        self.publish_ok = True

    
    def test_publish_frequency(self):
        rospy.init_node('test_freq_pub_node')
        rospy.Subscriber('frequency', Float32, self.callback_func)

        counter = 0
        while not rospy.is_shutdown() and counter < 5 and (not self.publish_ok):
            rospy.sleep(1)
            counter += 1

if __name__ == '__main__':
    rostest.rosrun("bedrock_ocean_assign", 'test_freq_pub_node', TestFreqPub)