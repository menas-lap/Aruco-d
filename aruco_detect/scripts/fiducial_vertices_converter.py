#!/usr/bin/env python3

import rospy
from fiducial_msgs.msg import FiducialArray
from visualization_msgs.msg import Marker

def fiducial_vertices_callback(fiducial_array):
    for fiducial in fiducial_array.fiducials:
        marker = Marker()
        # Populate marker fields based on fiducial data
        # ...

        marker_publisher.publish(marker)

if __name__ == '__main__':
    rospy.init_node('fiducial_vertices_converter')

    # Subscribe to /fiducial_vertices
    rospy.Subscriber('/fiducial_vertices', FiducialArray, fiducial_vertices_callback)

    # Create a new publisher for Marker
    marker_publisher = rospy.Publisher('/fiducial_vertices_markers', Marker, queue_size=10)

    rospy.spin()
