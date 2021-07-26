#!/usr/bin/env python

import rospy
# from bedrock_ocean_assign.msg import FrequencyInfo
from std_msgs.msg import Float32


def frequency_publisher():
    """Create a Publisher Object"""
    
    # Create and Initialize a ROS Node with name
    rospy.init_node('freq_pub_node', anonymous=True)


    # Create publisher to publish random floating point value
    pub = rospy.Publisher('frequency', FrequencyInfo, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz = 1 message per second
        
    while not rospy.is_shutdown():
        # Generate random floating point value
        freq_info.frequency = rospy.Time.now()
        rospy.loginfo(f"SENSOR FREQUNCY: {freq_info.frequency}")

        # Publish the ROS Message
        pub.publish(freq_info)
        
        rate.sleep()

if __name__ == '__main__':
    try:
        frequency_publisher()
    except rospy.ROSInterruptException:
        pass    
