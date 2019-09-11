# Crosscompiling on TX2

## Nsight Eclipse Edition
- This is an application that provides direct local cross-compiling on TX2 or remote cross-compiling 
- No need to write makefile or cmake files on TX2 

<br>
<br>

## OpenCV + CUDA test example
- Make sure local system and TX2 has same version of opencv
- 
```shell
$ pkg-config --modversion opencv
```

- Use Nsight
- 
> * Select workspace and create new `CUDA C/C++ Project`
>
> * Name project `test` and select toolchain `CUDA Toolkit`
>
> * Use default basic settings 
>
> * Cancel Local System and add remote connection by selecting `Manage`
>> * Host name: 172.20.8.246 (Check IP on TX2)
>>
>> * User name: nvidia
>>
>> * Password: nvidia
>>
>> * CPU Architecture: AArch64
>>
> * Project Path (Workspace diretory on TX2 ! Not on host)
> 
> * Toolkit may be empty, select `Manage` and `Detect`.
>

<br>
<br>

## Create workspace  
- Create a `src` folder under `test` workspace 
> * Write a `test.cpp` file to read image with opencv
> 
> * Write a CUDA file `hello.cu` 

<br>
<br>

## Add opencv libraries 
- Go to Project -> Properties
- 
> * Go to Build -> Settings -> Tool Settings
>
> * Under Include paths (-l), add opencv diretory.
> * opencv directory can be checked with
```shell
$ pkg-config --cflags opencv
```
>
> * Go to NVCC-linker -> Libraries
> * opencv libraries that needs to be added can be checked with
```shell
$ pkg-config --libs opencv
```
> * Manually add all opencv libraries into `Libraries`
>
> * And Library search path if there exists one. In this case `/usr/lib`
>

- Press Ok and now it should be able to compile 
- 

<br>
<br>

## Run on TX2
- You should be able to locate the test folder on TX2 that contains `Debug` and `src`
-
> * Save an image in the `Debug` folder and test executable
>
```shell
$ cd test
$ cd Debug/
$ ./test image.jpg
```
> * WORKS !

<br>
<br>

More information:
<br>
[CUDA Development for Jetson with NVIDIA Nsight Eclipse Edition](https://devblogs.nvidia.com/cuda-jetson-nvidia-nsight-eclipse-edition/)
<br>
[CSDN Tutorial](https://blog.csdn.net/coldsun1982/article/details/77524668)
<br>
[CMake crosscompile](http://zhixinliu.com/2016/02/01/2016-02-01-cmake-cross-compile/)
