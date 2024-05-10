cmake_minimum_required(VERSION 3.0)

set(OpenCV_DIR  "C:/opt/opencv/build")
set(CMAKE_C_COMPILER "C:/msys64/ucrt64/bin/gcc.exe")
set(CMAKE_CXX_COMPILER "C:/msys64/ucrt64/bin/gcc.exe")
project(OpenCVExample)

# Find OpenCV package
find_package(OpenCV REQUIRED)

#Include directories  from OpenCV
include_directories(${OpenCV_INCLUDE_DIRS})

# Create an executable
add_executable(OpenCVExample main.cpp)

# Link openCV libs
target_link_libraries(OpenCVExample ${OpenCV_LIBS})