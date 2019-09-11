# Set Up Jetson TX2 

## Jetpack 
- Nvidia Jetpack SDK is the comprehensive solution for building AI application and is used to flash Jetson Developer Kit with the latest OS image.
-
> Latest release can be checked out [here](https://developer.nvidia.com/embedded/jetpack)

## Install SDK Manager
- Install the specific version and run sdk manager  
-
```shell
$ sudo apt install sdkmanager_0.9.13-4763_amd64.deb 
```

- Select wanted host and target device and start downloading and installing.

## Problems 
- Install Error
-
> * Manually download the file using the link shown as error message in the SDK manager terminal
>
> * Placed into the download folder 

- Flashing - connection lost 
-
> * Make sure `lsusb` shows `nvidia_corp`
> 
> * Disconnect USB 
> 
> * Unplug power of TX2
>
> * Reconnect USB
>
> * Put TX2 into recovery mode and carry on flashing

## Other Usage
- See Realsense on TX2 [link](RealSense.md)