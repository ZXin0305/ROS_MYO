1.create ros pkg in your workspace
2.add "install(PROGRAMS {Your code files} DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})" in CMakeLists.txt
  add "catkin_python_setup()" in CMakeLists.txt for building ros node by "catkin_make"
3.build "setup.py" for "catkin_make" && "rosmyo_node" for buiding ros node through "rospy"
4.create launch file to execute multi myo nodes through different MYO device serial ports and device names ..
5.compile  --> "catkin_make" ,, "catkin_make install"
