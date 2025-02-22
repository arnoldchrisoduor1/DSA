cmake_minimum_required(VERSION 3.10)
project(NumberSumProject)

set(CMAKE_CXX_STANDARD 11)

# Add the executable for the main program
add_executable(number_sum_main main.cpp number_sum.cpp)

# Google Test
include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/609281088cfefc76f9d0ce82e1ff6c30cc3591e5.zip
)
FetchContent_MakeAvailable(googletest)

# Add the test executable
add_executable(number_sum_test test_number_sum.cpp number_sum.cpp)
target_link_libraries(number_sum_test gtest_main)

include(GoogleTest)
gtest_discover_tests(number_sum_test)