#!/usr/bin/env python3

import rospy
from fiducial_msgs.msg import FiducialTransformArray
from visualization_msgs.msg import Marker, MarkerArray

def fiducial_transform_callback(fiducial_transform_array):

    marker_array = MarkerArray()

    for fiducial_transform in fiducial_transform_array.transforms:
        marker = Marker()
        # Populate marker fields based on fiducial_transform data
        # ...

        marker_array.markers.append(marker)

    marker_publisher.publish(marker_array)

if __name__ == '__main__':
    rospy.init_node('fiducial_transform_converter')

    # Subscribe to /fiducial_transforms
    rospy.Subscriber('/fiducial_transforms', FiducialTransformArray, fiducial_transform_callback)

    # Create a new publisher for MarkerArray
    marker_publisher = rospy.Publisher('/fiducial_markers', MarkerArray, queue_size=10)

    rospy.spin()
