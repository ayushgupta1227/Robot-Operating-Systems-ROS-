#!/usr/bin/env python
# number_counter.py - Subscribes to /number and publishes running total to /number_count
import rospy
from std_msgs.msg import Int64
class NumberCounter:
def __init__(self):
rospy.init_node(’number_counter’)
self.total = 0
self.sub = rospy.Subscriber(’/number’, Int64, self.number_callback)
self.pub = rospy.Publisher(’/number_count’, Int64, queue_size=10)
def number_callback(self, msg):
self.total += msg.data
rospy.loginfo(f"Received: {msg.data}, Running total: {self.total}")
# Publish the updated total
total_msg = Int64()
total_msg.data = self.total
self.pub.publish(total_msg)
if __name__ == ’__main__’:
counter = NumberCounter()
rospy.spin()
