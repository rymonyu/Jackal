# Realsense on Linux

* Follow guide for librealsense installation on Linux [tutorial](https://github.com/IntelRealSense/librealsense/blob/master/doc/distribution_linux.md)

* To setup ROS usage of Realsense [tutorial](https://github.com/IntelRealSense/realsense-ros)

<br>

- Issues:

> *RGBD_launch* package missing while launching rgbd_launch

- Solved:

> Direct into `src` directory and include *rgbd_launch* package

```shell
$ git clone https://github.com/ros-drivers/rgbd_launch.git
$ cd ..
$ catkin_make 
```
<br>
<br>

# Realsense on TX2

- Check Kernel Version
- 
> Only some kernel versions are supported by librealsense, check on website whether your version is being supported [Link](https://github.com/IntelRealSense/librealsense/blob/master/doc/installation.md)

```shell
$ uname -r
```

> In order for librealsense to work properly, the kernel image must be rebuilt and patches are needed to support extra features.
> Open up new terminal and `git clone` required files

```shell
$ git clone https://github.com/Tengyun-Mo/buildLibrealsense2TX2
```

- Build patched kernel
-

```shell
$ ./buildPatchedKernel.sh
```

- Replace Kernel Image
- 
> Back up original kernel image, located at `/boot`. File is called `Image`
> Replace new kernel image 

```shell
$ sudo cp ./image/Image /boot
```

> Remove unwanted files generated while building patched kernel

```shell
$ ./removeAllKernelSources.sh
```

- Reboot Device
- 

```shell
$ reboot
```

- Install `librealsense2` 
- 
> this may take a long time !

```shell
$ ./installLibrealsense.sh
```