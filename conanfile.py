from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMakeDeps


class ModernCppProject(ConanFile):
    name = "cpp_project"
    version = "1.0.0"

    # 业务库
    requires = "nlohmann_json/3.12.0"

    # 测试框架：自动拉取最新版 GoogleTest
    test_requires = "gtest/1.17.0"

    # 构建工具链
    tool_requires = [
        "cmake/4.1.0",
        "ninja/1.12.1",
    ]

    settings = "os", "compiler", "build_type", "arch"
    test_type = "explicit"

    def generate(self):
        tc = CMakeToolchain(self)
        tc.cache_variables["CMAKE_C_COMPILER"] = "clang-21"
        tc.cache_variables["CMAKE_CXX_COMPILER"] = "clang++-21"
        tc.cache_variables["CMAKE_CXX_STANDARD"] = "23"
        tc.cache_variables["CMAKE_CXX_STANDARD_REQUIRED"] = "ON"
        tc.cache_variables["CMAKE_CXX_EXTENSIONS"] = "OFF"
        tc.generator = "Ninja"
        tc.generate()

        deps = CMakeDeps(self)
        deps.generate()
