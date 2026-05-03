cmake_minimum_required(VERSION 4.3.2 FATAL_ERROR)
project(HelloCMake CXX)

# 警告选项（可选）
add_compile_options(-Wall -Wextra -Werror)

# 生成可执行文件
add_executable(hello src/main.cpp)
