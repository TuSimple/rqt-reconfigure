cmake_minimum_required(VERSION 3.5)
set(CMAKE_VERBOSE_MAKEFILE true)
project(zoro_rqt_reconfigure)

# Default to C11
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 11)
endif()
if(CMAKE_COMPILER_IS_GNUCC OR CMAKE_C_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra)
endif()

set(CMAKE_CXX_STANDARD 14)

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rcl REQUIRED)
find_package(rclcpp REQUIRED)

find_package(python_cmake_module REQUIRED)
find_package(PythonExtra MODULE REQUIRED)
set(_PYTHON_EXECUTABLE "${PYTHON_EXECUTABLE}")

if(WIN32 AND CMAKE_BUILD_TYPE STREQUAL "Debug")
  set(PYTHON_EXECUTABLE "${PYTHON_EXECUTABLE_DEBUG}")
endif()
ament_python_install_package(${PROJECT_NAME})


install(DIRECTORY zoro_rqt_reconfigure DESTINATION ${PYTHON_INSTALL_DIR}/${PROJECT_NAME})
install(DIRECTORY zoro_resource DESTINATION ${PYTHON_INSTALL_DIR}/${PROJECT_NAME})
install(FILES zoro_rqt.py DESTINATION lib/${PROJECT_NAME})
install(files script/zoro_rqt_run  DESTINATION script)

ament_export_include_directories(zoro_resource)
ament_export_include_directories(zoro_rqt_reconfigure)
ament_package()
