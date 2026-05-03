# C++ CMake Template (Modern CMake + C++23 + Clang + Ninja + CodeLLDB)
一个**干净、现代、可直接使用**的 C++ 项目模板，适用于学习、开发、调试。

## ✨ 特性
- 使用 **Modern CMake** 最佳实践
- 支持 **C++23**
- 使用 **Clang 21** 编译器
- 使用 **Ninja** 快速构建
- 配置好 **VSCode + CodeLLDB** 一键调试
- 支持多可执行文件切换调试
- 调试可正常显示：
  - `std::string`
  - 智能指针 `std::shared_ptr` / `std::unique_ptr`
  - C++23 容器
- 标准项目结构（`include/` + `src/`）
- 使用 `target_include_directories` 管理头文件路径
- 集成 Conan 包管理：配置文件化、环境标准化、跨设备一致
- 内置 Clang-Tidy 提交钩子，代码提交前自动静态检查

---

## 📁 项目结构
``` bash
.
├── include/           # 头文件目录
├── src/
│   └── main.cpp       # 主程序
├── conan/
│   └── profiles/
│       └── clang21-debug  # 项目级编译配置文件
├── scripts/
│   └── install-githooks.sh # Clang-Tidy 钩子安装脚本
├── .vscode/
│   ├── launch.json    # CodeLLDB 调试配置
│   └── tasks.json     # 自动构建任务
├── CMakeLists.txt     # 现代 CMake 配置
├── CMakePresets.json  # 编译预设（Clang + Ninja）
└── README.md
```

---

## 🛠 环境要求
- CMake **3.20+**（本项目使用 **4.3.2**）
- Clang **21**
- Ninja
- VSCode + **CodeLLDB** 插件
- Conan（包管理工具，用于环境标准化）

---

## 🚀 构建与运行（标准化流程）
### 完整流程（推荐）
```bash
# 1. 清理旧构建目录（可选）
rm -rf build/

# 2. 读取项目 Profile，安装依赖/工具链/CMake/Ninja
conan install . -of build --profile=conan/profiles/clang21-debug --build=missing

# 3. 激活 Conan 隔离环境（注入定制化编译工具链）
source build/conanbuild.sh

# 4. （可选）启动 VSCode
code .

# 5. 编译项目
cmake --preset conan-debug
cmake --build --preset conan-debug

# 6. 运行可执行文件
./build/hello
```

### 传统构建流程（备用）
```bash
# 1. 创建 build 目录
mkdir build && cd build

# 2. 配置 CMake
cmake .. --preset clang21-debug

# 3. 编译
cmake --build .

# 4. 运行
./hello
```

---

## 🔧 核心配置说明
### 1. Modern CMake 头文件管理
本项目使用现代 CMake 方式管理头文件，不污染全局路径：
```cmake
target_include_directories(hello
  PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/include
)
```
- **PRIVATE**：仅当前目标可使用该头文件路径
- 结构清晰、可扩展、适合大型项目

### 2. Conan Profile 配置（核心优化）
项目内置 Git 托管的 Profile 文件 `conan/profiles/clang21-debug`，替代原有超长命令行参数：
```ini
[settings]
build_type = Debug
compiler = clang
compiler.version = 21
compiler.cppstd = 23
os = Linux
arch = x86_64

[conf]
# 全局默认使用 Ninja 生成器
tools.cmake.cmaketoolchain:generator = Ninja
```
**优势**：
- 收拢全量编译配置，规避超长命令行参数
- 固化 Debug/Clang 21/C++23/Ninja 核心配置
- 配置文件化，团队/跨设备环境强一致
- 版本可控，便于协作维护

**废弃的冗余参数**（已迁移至 Profile）：
```bash
-s build_type=Debug -s compiler=clang -s compiler.version=21 -s compiler.cppstd=23
```

---

## 🐛 VSCode + CodeLLDB 调试
本项目已完整配置好调试环境：
- 按 **F5 一键调试**
- 自动编译
- 输出日志到终端
- 支持断点、条件断点、日志断点
- 不崩溃、不触发 SIGSEGV

### 关键配置（.vscode/launch.json）
```json
"stopOnEntry": false,
"expressions": "native",
"console": "integratedTerminal"
```

---

## 📌 已解决的常见问题
- **SIGSEGV 段错误**：`stopOnEntry` 必须为 `false`
- **条件断点失效**：开启 `"expressions": "native"`
- **C++23 容器不显示**：新版 CodeLLDB 自动支持
- **problemMatcher 报错**：直接置空即可
- **头文件找不到**：使用 `target_include_directories`
- **编译环境不一致**：使用 Conan Profile 固化编译配置
- **超长命令行参数易出错**：配置文件化替代命令行参数

---

## 🧹 代码静态检查（Clang-Tidy）
本仓库内置 Clang-Tidy 提交钩子，提交代码前自动执行静态检查，保障代码规范。

### 启用钩子
```bash
./scripts/install-githooks.sh
```

---

## 🎯 适用场景
- C++ 初学者
- Modern CMake 学习
- Clang + CodeLLDB 调试环境搭建
- Conan 包管理 + 环境标准化实践
- 可直接用于课程作业、小项目、Demo、团队协作开发

---

## 📄 License
MIT

---

### 主要补充/更新点说明：
1. **项目结构**：新增 `conan/`、`scripts/` 目录说明，完善目录树
2. **环境要求**：补充 Conan 依赖说明
3. **构建流程**：
   - 新增标准化 Conan 构建流程（核心）
   - 保留传统流程作为备用
   - 补充运行可执行文件的明确路径
4. **核心配置**：单独拆分 Conan Profile 配置说明，突出优势和废弃的冗余参数
5. **特性**：新增 Conan 集成、Clang-Tidy 钩子相关特性
6. **常见问题**：补充编译环境不一致、超长命令行参数的解决方案
7. **静态检查**：完善 Clang-Tidy 钩子的说明
8. **适用场景**：补充 Conan 实践、团队协作场景

整体保持原有文档的风格和逻辑，同时补齐了 Conan 相关的核心信息，使文档完整覆盖「环境准备-配置-构建-调试-代码规范」全流程。
