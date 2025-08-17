#!/usr/bin/env python
# number_publisher.py - Publishes sequential numbers to /number topic
import rospy
from std_msgs.msg import Int64
class NumberPublisher:
def __init__(self):
rospy.init_node(’number_publisher’)
self.pub = rospy.Publisher(’/number’, Int64, queue_size=10)
self.rate = rospy.Rate(1) # 1 Hz publishing rate
self.count = 0
def run(self):
while not rospy.is_shutdown():
1

self.count += 1
rospy.loginfo(f"Publishing number: {self.count}")
self.pub.publish(self.count)
self.rate.sleep()
if __name__ == ’__main__’:
try:
publisher = NumberPublisher()
publisher.run()
except rospy.ROSInterruptException:
pass
article verbatim fancyvrb [margin=1in]geometry
ROS Number Counter Script
