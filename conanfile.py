from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMakeDeps


class ModernCppDemo(ConanFile):
    name = "modern_cpp_demo"
    version = "1.0.0"

    requires = "nlohmann_json/3.12.0"
    settings = "os", "compiler", "build_type", "arch"

    def generate(self):
        tc = CMakeToolchain(self)
        tc.cache_variables["CMAKE_C_COMPILER"] = "clang-21"
        tc.cache_variables["CMAKE_CXX_COMPILER"] = "clang++-21"
        tc.cache_variables["CMAKE_CXX_STANDARD"] = "23"
        tc.cache_variables["CMAKE_CXX_EXTENSIONS"] = "OFF"
        tc.generator = "Ninja"
        tc.generate()

        deps = CMakeDeps(self)
        deps.generate()
