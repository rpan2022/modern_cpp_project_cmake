# C++ CMake Template (Modern CMake + C++23 + Clang + Ninja + CodeLLDB + Conan 2 + GTest)
一个干净、现代、可移植、开箱即用的 C++ 项目模板，适用于学习、开发、团队协作。

<p align="center">
  <img src="https://img.shields.io/badge/C%2B%2B-23-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white" alt="C++23">
  <img src="https://img.shields.io/badge/CMake-4.1-064F8C?style=for-the-badge&logo=cmake&logoColor=white" alt="CMake">
  <img src="https://img.shields.io/badge/Clang-21-30A1DC?style=for-the-badge&logo=llvm&logoColor=white" alt="Clang">
  <img src="https://img.shields.io/badge/Ninja-Build-40B0A0?style=for-the-badge&logo=ninja&logoColor=white" alt="Ninja">
  <img src="https://img.shields.io/badge/Conan-2-6B9E2F?style=for-the-badge&logo=conan&logoColor=white" alt="Conan">
  <img src="https://img.shields.io/badge/GoogleTest-1.15.2-4285F4?style=for-the-badge&logo=googletest&logoColor=white" alt="GTest">
</p>

---

## ✨ 特性
- 遵循 Modern CMake 最佳实践
- 支持 C++23（含 <print>）
- 编译器：Clang 21
- 构建系统：Ninja
- 调试：VSCode + CodeLLDB 一键 F5
- 包管理：Conan 2（自动管理 CMake / Ninja / 第三方库）
- 环境锁定：项目级 Conan Profile，命令极简、可移植
- 无硬编码路径，团队/多设备环境完全一致
- 单元测试：GoogleTest 1.15.2（最新稳定版）
- 代码规范：Clang-Tidy Git 提交钩子
- 标准项目结构：include/ + src/ + test/

---

## 📁 项目结构
```
.
├── include/              # 头文件
├── src/                  # 主程序源码
│   └── main.cpp
├── test/                 # 单元测试
│   └── test_demo.cpp
├── conan/
│   └── profiles/
│       └── clang21-debug # Conan 编译配置
├── .vscode/              # VSCode 调试/任务配置
├── scripts/               # 工具脚本
├── CMakeLists.txt         # CMake 配置
├── conanfile.py           # Conan 依赖&工具链
└── README.md
```

---

## 🛠 环境要求
- **Conan 2.x**（必须）
- VSCode + CodeLLDB 插件
- 系统预装：clang-21 / clang++-21

> CMake、Ninja、GTest、nlohmann_json 均由 Conan 自动安装，无需手动配置。

---

## 🚀 快速开始（3 行跑通）
```bash
rm -rf build
conan install . -of build --profile=conan/profiles/clang21-debug --build=missing
source build/conanbuild.sh && cmake --preset conan-debug && cmake --build --preset conan-debug
```

运行：
```bash
./build/app
```

运行测试：
```bash
cd build && ctest
```

---

## 🧪 完整构建流程
```bash
# 1. 清理旧构建
rm -rf build/

# 2. 安装依赖、工具链、CMake、Ninja、GTest
conan install . -of build --profile=conan/profiles/clang21-debug --build=missing

# 3. 激活 Conan 隔离环境（必须！）
source build/conanbuild.sh

# 4. 启动 VSCode
code .

# 5. 配置 + 编译
cmake --preset conan-debug
cmake --build --preset conan-debug

# 6. 运行程序
./build/app

# 7. 运行单元测试
cd build && ctest
# 或直接运行测试程序
./build/unit_tests
```

---

## 🧠 Conan Profile 作用（核心）
文件：`conan/profiles/clang21-debug`

作用：
- 锁定 Debug 模式
- 锁定 Clang 21
- 锁定 C++23
- 锁定 Ninja 生成器
- 替代所有冗长 `-s` 命令行参数
- 保证项目可移植、团队一致

---

## 🧪 GoogleTest 单元测试
本模板已集成 **GTest 1.15.2**（最新稳定版）。

添加测试：
在 `test/` 目录下新建 cpp 文件即可。

示例测试：
```cpp
#include <gtest/gtest.h>
TEST(DemoTest, Equal) {
    EXPECT_EQ(1 + 1, 2);
}
```

运行测试：
```bash
cd build && ctest
```

---

## 🐛 VSCode 调试（F5 一键）
- 自动编译
- 终端输出
- 无 SIGSEGV 崩溃
- 完美显示 std::string / 智能指针 / C++23 容器

配置原则：
- **不硬编码 CMake 路径**，保证可移植
- 使用 `conanbuild.sh` 注入环境

---

## 🧹 代码静态检查（Clang-Tidy）
启用 Git 提交自动检查：
```bash
./scripts/install-githooks.sh
```

---

## 📌 常见问题（已踩坑全解决）
- **找不到 conan-debug preset**  
  必须用 `conan install` + `clang21-debug` profile
- **编译器变成 GCC**  
  必须先 `source build/conanbuild.sh`
- **CMake 版本不对**  
  使用 Conan 提供的 CMake，不使用系统版本
- **<print> 头文件找不到**  
  确认 Clang 21 + C++23 已启用
- **GTest 链接失败**  
  重新执行 `conan install` 并加载配置
- **VSCode CMake 插件报错**  
  不要配置 `cmake.cmakePath` 硬编码路径

---

## 🎯 适用场景
- C++ 初学者
- Modern CMake 学习
- Clang + C++23 开发
- 工业级可移植项目
- 团队协作、多设备同步开发
- 课程作业 / Demo / 小型项目 / 服务端工具

---

## 📄 License
MIT

---

## 你现在的项目具备：
✅ C++23 + Clang 21  
✅ CMake 4.1（Conan 托管）  
✅ Ninja  
✅ Conan 2 + Profile  
✅ GoogleTest 最新版  
✅ VSCode 可移植无坑配置  
✅ 单元测试  
✅ 代码检查  
✅ 完整规范 README  
✅ 可直接上传 GitHub 做模板仓库
