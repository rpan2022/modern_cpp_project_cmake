cmake_minimum_required(VERSION 4.1.0)
project(modern_cpp_demo)

# 自动加载 Conan 工具链
include(${CMAKE_BINARY_DIR}/conan_toolchain.cmake)

# 可执行文件
add_executable(hello src/main.cpp)
target_include_directories(hello PRIVATE include)

# 第三方库
find_package(nlohmann_json REQUIRED)
target_link_libraries(hello PRIVATE nlohmann_json::nlohmann_json)
