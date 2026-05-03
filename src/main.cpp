#include <iostream>
#include <nlohmann/json.hpp>
#include <print>
#include <vector>

void use_json() {
  nlohmann::json data;
  data["project"] = "modern_cpp_demo";
  data["compiler"] = "clang++-21";
  data["cpp"] = "23";

  std::print("{}", data.dump(4));
}

auto main() -> int {
  std::cout << "Hello C++23 with Clang-21 + CMake + Ninja!\n";

  [[maybe_unused]] const int result = 1;

  std::print("current cpp version: {}\n", __cplusplus);

  std::vector<int> val{1, 2, 3, 4, 5};

  for (auto& tmp : val) {
    std::print("value = {}\n", tmp);
  }

  use_json();

  return 0;
}
