# Jackal User Manual

## Jackal's Basic Information

- System Architecture
> * x86 PC + Ubuntu 14.04, 32-bit MCU
>
> * Full speed USB connection between MCU and PC
>
> * Communication protocol being used is rosserial and an instance of the rosserial_server serial node is embedded in the jackal_base node.

- Hardware Architecture
> * Jackal includes a standard internal PC, as well as basic IMU and GPS
>
> * PC: Intel Core i5 4570T, Dual core, 2.9GHz, 4GB RAM, 128GB Hard Drive, WIFI Adapter
>
> * Speed performance: Max speed 2.0 m/s (6.6 ft/s), Drive power: 500W 

<br>
<br>

## Use Jackal

<br>

### To install Jackal package in ROS Kinetic

- Install Dependencies
- 
> If want to use `rosdep`, skip this step

```shell
sudo apt-get install ros-kinetic-robot-localization ros-kinetic-controller-manager ros-kinetic-joint-state-controller ros-kinetic-diff-drive-controller ros-kinetic-gazebo-ros ros-kinetic-gazebo-ros-control ros-kinetic-gazebo-plugins             ros-kinetic-lms1xx ros-kinetic-pointgrey-camera-description ros-kinetic-roslint ros-kinetic-amcl ros-kinetic-gmapping      ros-kinetic-map-server ros-kinetic-move-base ros-kinetic-urdf ros-kinetic-xacro ros-kinetic-message-runtime ros-kinetic-topic-tools ros-kinetic-teleop-twist-joy
```
- Create workspace and clone sources
- 
```shell
$ mkdir -p jackal_ws/src; cd jackal_ws/src; catkin_init_workspace
$ git clone https://github.com/jackal/jackal.git
$ git clone https://github.com/jackal/jackal_simulator.git
$ git clone https://github.com/jackal/jackal_desktop.git
$ git clone https://github.com/ros-visualization/interactive_marker_twist_server.git
```
- Install depedencies with rosdep
-
```shell
$ cd jackal_ws
$ rosdep install --from-paths . --ignore-src --rosdistro=kinetic
```

- Build and source 
- 
```shell
$ cd jackal_ws
$ catkin_make
$ source devel/setup.bash
```
<br>
<br>

### Simulation with Gazebo and Rviz

- Start simulating in gazebo environment
- 
> Gazebo not only simulates the physical presence of the laser scanner, it also provides simulated data which reflects the robot's surroundings in its simulated world.

```shell
$ roslaunch jackal_gazebo jackal_world.launch

If want to add front laser config
$ roslaunch jackal_gazebo jackal_world.launch config:=laser 
```

- To visualize simulated data in Rviz
- 
> By moving the jackal's interactive markers, the robot should move around in the gazebo world / real world if driving real jackal
> 
> To visualize more sensor data, simply Add By Topic in the Rviz tool bar

```shell
$ roslaunch jackal_viz view_robot.launch
```
<br>
<br>

### Navigation

- Launch navigation demo
-
> Jackal contains basic IMU and GPU for navigation purpose but not lidar

```shell
$ roslaunch jackal_navigation odom_navigation_demo.launch
```

- Visualize with Rviz
- 
> You should be able to set 2D navigation goals from selecting the 2D Nav Goal tool from the top toolbar. Click anywhere to set the position

```shell
$ roslaunch jackal_viz view_robot.launch config:=navigation
```

<br>
<br>

### Launch File
- The launch file is located in /etc/ros/indigo
- 
> This launch file gets sourced by Jackal's background launch job on login session. This launch file can be considered as the "global" setup file for Jackal's ROS installation

<br>
<br>

### Docker Image
- The docker image is on `registry.sensetime.com/robot-env/`
- Environment
- 
> * Ubuntu 16.04.6 LTS <br>
> * ROS kinetic <br>
> * CUDA 10.0 <br>
> * CUDNN 7.501 <br>
> * TensorRT-5.0.2.6 <br>
> * Pytorch 1.1.0 <br>
> * realsense camera sdk <br>
> * mynt eye sdk <br>

- When building container, remember to include usb device and internet access
- 
```shell
--privileged -v /dev:/dev
--network host 
```

<br>
<br>

### Other Usage
> * See [RealSense Setup](RealSense.md)
>
> * See [Jetson TX2 Setup](TX2.md)
> 
> * See [MYNT Camera Setup](MYNT.md)
>
> * See [Human detection + Following](detection_following)



