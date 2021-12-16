#!/usr/bin/env python
# coding: utf-8

import rospy
from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint


def send_trajectory(publisher, trajectory):
    msg = JointTrajectory()
    msg.header.stamp = rospy.Time.now()

    msg.joint_names = [x[0] for x in trajectory]
    point = JointTrajectoryPoint()
    point.positions = [x[1] for x in trajectory]
    point.time_from_start = rospy.Duration(1)
    msg.points = [point]

    publisher.publish(msg)


def main():
    rospy.init_node("initial_traj_node")
    right_arm_home_pose = [('r_arm_joint1', -0.3574), ('r_arm_joint2', -1.5707), ('r_arm_joint3', 0.0),
                           ('r_arm_joint4', 2.67), ('r_arm_joint5', 0.0), ('r_arm_joint6', -1.1554),
                           ('r_arm_joint7', 0.0)]
    left_arm_home_pose = [('l_arm_joint1', 0.3574), ('l_arm_joint2', 1.5707), ('l_arm_joint3', 0.0),
                          ('l_arm_joint4', -2.67), ('l_arm_joint5', 0.0), ('l_arm_joint6', 1.1554),
                          ('l_arm_joint7', 0.0)]

    right_arm_joint_trajectory_publisher = rospy.Publisher('/sciurus17/controller1/right_arm_controller/command',
                                                           JointTrajectory, queue_size=10)
    left_arm_joint_trajectory_publisher = rospy.Publisher('/sciurus17/controller2/left_arm_controller/command',
                                                          JointTrajectory, queue_size=10)

    rospy.sleep(3.0)

    send_trajectory(right_arm_joint_trajectory_publisher, right_arm_home_pose)
    send_trajectory(left_arm_joint_trajectory_publisher, left_arm_home_pose)


if __name__ == '__main__':
    try:
        if not rospy.is_shutdown():
            main()
    except rospy.ROSInterruptException:
        pass
