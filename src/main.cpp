#include <iostream>
#include <print>
#include <vector>

auto main() -> int {
  std::cout << "Hello C++23 with Clang-21 + CMake + Ninja!" << std::endl;

  std::print("current cpp version: {}\n", __cplusplus);

  std::vector<int> val{1, 2, 3, 4, 5};

  for (auto& v : val) {
    std::print("value = {}\n", v);
  }

  return 0;
}
