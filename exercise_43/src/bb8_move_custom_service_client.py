#! /usr/bin/env python

import rospkg
import rospy
from exercise_43.srv import exercise_43_ServiceMessage, exercise_43_ServiceMessageRequest

rospy.init_node('service_move_bb8_in_circle_custom_client')     # Initialise a ROS node with the name service_client
rospy.wait_for_service('/move_bb8_in_circle_custom')            # Wait for the service client /move_bb8_in_circle_custom to be running
move_bb8_circle_service_client = rospy.ServiceProxy('/move_bb8_in_circle_custom', exercise_43_ServiceMessage)   # Create the connection to service
move_bb8_circle_request_object = exercise_43_ServiceMessageRequest()    # Create an object of type EmptyRequest

"""
# BB8CustomServiceMessage
float64 side       # The distance of each side of the circle
int32 repetitions    # The number of times BB-8 has to execute the circle movement when the service is called
---
bool success         # Did it achieve it?
"""

move_bb8_circle_request_object.duration = 20

rospy.loginfo("Doing Service Call...")
result = move_bb8_circle_service_client(move_bb8_circle_request_object)     # Send through the connection the path to trajectory file to be executed
