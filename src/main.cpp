#include <iostream>
#include <print>
#include <vector>

auto main() -> int {
  std::cout << "Hello C++23 with Clang-21 + CMake + Ninja!\n";

  [[maybe_unused]] const int result = 1;

  std::print("current cpp version: {}\n", __cplusplus);

  std::vector<int> val{1, 2, 3, 4, 5};

  for (auto& tmp : val) {
    std::print("value = {}\n", tmp);
  }

  return 0;
}
