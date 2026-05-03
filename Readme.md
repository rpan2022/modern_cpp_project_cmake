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

---

## 📁 项目结构
```
.
├── include/           # 头文件目录
├── src/
│   └── main.cpp       # 主程序
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

---

## 🚀 构建与运行
### 1. 创建 build 目录
```bash
mkdir build && cd build
```

### 2. 配置 CMake
```bash
cmake .. --preset clang21-debug
```

### 3. 编译
```bash
cmake --build .
```

### 4. 运行
```bash
./hello
```

---

## 🔧 CMake 核心说明（Modern CMake）
本项目使用现代 CMake 方式管理头文件：
```cmake
target_include_directories(hello
  PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/include
)
```
- **PRIVATE**：仅当前目标可使用该头文件路径
- 不污染全局
- 结构清晰、可扩展、适合大型项目

---

## 🐛 VSCode + CodeLLDB 调试
本项目已完整配置好调试环境：
- 按 **F5 一键调试**
- 自动编译
- 输出日志到终端
- 支持断点、条件断点、日志断点
- 不崩溃、不触发 SIGSEGV

### 关键配置
```json
"stopOnEntry": false
"expressions": "native"
"console": "integratedTerminal"
```

---

## 📌 已解决的常见问题
- **SIGSEGV 段错误**：`stopOnEntry` 必须为 `false`
- **条件断点失效**：开启 `"expressions": "native"`
- **C++23 容器不显示**：新版 CodeLLDB 自动支持
- **problemMatcher 报错**：直接置空即可
- **头文件找不到**：使用 `target_include_directories`

---

## 🎯 适用场景
- C++ 初学者
- Modern CMake 学习
- Clang + CodeLLDB 调试环境
- 可直接用于课程作业、小项目、Demo

---

## 📄 License
MIT
