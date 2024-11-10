cmake_minimum_required(VERSION 3.10)

project(XTEALTHCompiler)

set(CMAKE_CXX_STANDARD 11)

include_directories(include)

add_executable(xtealthc src/main.cpp)
target_link_libraries(xtealthc llvm)
