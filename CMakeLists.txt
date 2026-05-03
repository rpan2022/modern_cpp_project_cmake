cmake_minimum_required(VERSION 4.1.0)
project(cpp_project)

include(${CMAKE_BINARY_DIR}/conan_toolchain.cmake)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# 主程序
add_executable(app src/main.cpp)
target_include_directories(app PRIVATE include)
find_package(nlohmann_json REQUIRED)
target_link_libraries(app PRIVATE nlohmann_json::nlohmann_json)

# ===================== TESTS =====================
enable_testing()
find_package(GTest REQUIRED)

add_executable(unit_tests
    test/test_demo.cpp
)
target_include_directories(unit_tests PRIVATE include)
target_link_libraries(unit_tests
    PRIVATE
    nlohmann_json::nlohmann_json
    GTest::gtest
    GTest::gtest_main
)

include(GoogleTest)
gtest_discover_tests(unit_tests)
