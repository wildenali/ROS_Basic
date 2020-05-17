#! /usr/bin/env python

import rospy
from exercise_33.msg import Age

rospy.init_node('publish_age_node')
pub = rospy.Publisher('/age_info', Age, queue_size=1)
rate = rospy.Rate(1)

age = Age()
age.years = 6
age.month = 12
age.days = 23

while not rospy.is_shutdown():
    pub.publish(age)
    rate.sleep()