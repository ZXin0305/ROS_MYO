cmake_minimum_required(VERSION 2.8.3)
project(rosmyo)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
	rospy
	sensor_msgs
	std_msgs
	message_generation
)

catkin_python_setup()

###########
## Build ##
###########

# Generate messages in the 'msg' folder
add_message_files(
    DIRECTORY msg
    FILES
    ClassifierArmSync.msg
    ClassifierLocked.msg
    ClassifierPose.msg
    ClassifierSyncFailed.msg
    Emg.msg
)

# target_link_libraries(
#     ${PROJECT_NAME}
#     /usr/include/python2.7
#     /usr/lib/x86_64-linux-gnu/libpython2.7.so
# )

## Generate added messages and services with any dependencies
generate_messages(DEPENDENCIES std_msgs)

catkin_package(
	CATKIN_DEPENDS message_runtime
)

install(PROGRAMS 
    src/rosmyo/rosmyo_class.py 
    src/rosmyo/bled112.py 
    src/rosmyo/myo_comm.py 
    src/rosmyo/myo.py 
    src/rosmyo/packet_serial.py 
    src/rosmyo/packets.py 
    src/rosmyo/waitables.py 
    src/rosmyo/worker_thread.py 
    
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
