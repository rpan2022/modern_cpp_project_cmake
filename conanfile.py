from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMakeDeps


class ModernCppProject(ConanFile):
    name = "cpp_project"
    version = "1.0.0"

    # 第三方库（可增删）
    requires = "nlohmann_json/3.12.0"

    # 自动下载 CMake + Ninja
    tool_requires = [
        "cmake/4.1.0",
        "ninja/1.12.1",
    ]

    settings = "os", "compiler", "build_type", "arch"

    def generate(self):
        tc = CMakeToolchain(self)

        # 强制 Clang 21
        tc.cache_variables["CMAKE_C_COMPILER"] = "clang-21"
        tc.cache_variables["CMAKE_CXX_COMPILER"] = "clang++-21"

        # 强制 C++23
        tc.cache_variables["CMAKE_CXX_STANDARD"] = "23"
        tc.cache_variables["CMAKE_CXX_STANDARD_REQUIRED"] = "ON"
        tc.cache_variables["CMAKE_CXX_EXTENSIONS"] = "OFF"

        tc.generator = "Ninja"
        tc.generate()

        deps = CMakeDeps(self)
        deps.generate()
