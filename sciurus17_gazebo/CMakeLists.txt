cmake_minimum_required(VERSION 2.8.3)
project(sciurus17_gazebo)

find_package(catkin REQUIRED)

# catkin_python_setup()

###################################
## catkin specific configuration ##
###################################
catkin_package()

###########
## Build ##
###########
link_directories(${GAZEBO_LIBRARY_DIRS})
include_directories(
  ${catkin_INCLUDE_DIRS}
)

install(DIRECTORY launch worlds
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
