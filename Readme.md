# C++ CMake Template (Modern CMake + C++23 + Clang + Ninja + CodeLLDB + Conan 2)
一个**干净、现代、可直接使用、跨平台可移植**的 C++ 项目模板。
使用 **Conan 2** 统一管理工具链与依赖，保证团队/多设备环境完全一致。

## ✨ 特性
- 使用 **Modern CMake** 最佳实践
- 支持 **C++23**（含 `<print>`）
- 使用 **Clang 21** 编译器
- 使用 **Ninja** 快速构建
- 配置好 **VSCode + CodeLLDB** 一键调试
- 调试完美支持：
  - `std::string`
  - `std::shared_ptr` / `std::unique_ptr`
  - C++23 标准库容器
- 标准项目结构：`include/` + `src/`
- 使用 `target_include_directories` 管理头文件（无全局污染）
- **Conan 2 集成**：自动下载 CMake / Ninja / 第三方库
- **项目级 Conan Profile**：固化编译环境，命令极简
- **无硬编码路径**：保证项目可移植、团队友好
- 内置 `clang-tidy` 代码检查 Git 钩子

---

## 📁 项目结构
```
.
├── include/                  # 头文件
├── src/
│   └── main.cpp              # 主程序
├── conan/
│   └── profiles/
│       └── clang21-debug     # Conan 编译配置文件
├── .vscode/
│   ├── launch.json           # CodeLLDB 调试
│   └── tasks.json            # 构建任务
├── scripts/
│   └── install-githooks.sh   # Git 钩子安装
├── CMakeLists.txt            # 现代 CMake
├── conanfile.py              # Conan 依赖 + 工具链
└── README.md
```

---

## 🛠 环境要求
- **Conan 2.x**（必须）
- VSCode + **CodeLLDB** 插件
- 系统预装：`clang-21` / `clang++-21`

> CMake / Ninja 不需要手动安装，由 Conan 自动下载管理。

---

## 🚀 标准化构建流程（推荐）
```bash
# 1. 清理旧构建
rm -rf build/

# 2. 安装依赖 + 工具链（CMake 4.1 + Ninja + Clang 21 + C++23）
conan install . -of build --profile=conan/profiles/clang21-debug --build=missing

# 3. 激活 Conan 隔离环境（关键！让 VSCode 使用 Conan 版 CMake）
source build/conanbuild.sh

# 4. 启动 VSCode
code .

# 5. 配置 + 编译
cmake --preset conan-debug
cmake --build --preset conan-debug

# 6. 运行
./build/app
```

---

## 🧠 Conan Profile 说明（核心）
所有编译配置**全部收拢到文件**，不再使用冗长 `-s` 参数：

```ini
[settings]
build_type = Debug
compiler = clang
compiler.version = 21
compiler.cppstd = 23
os = Linux
arch = x86_64

[conf]
tools.cmake.cmaketoolchain:generator = Ninja
```

### 作用
- 锁定 **Debug**
- 锁定 **Clang 21**
- 锁定 **C++23**
- 锁定 **Ninja**
- 命令行极简、可移植、团队一致

---

## 🧪 VSCode 可移植性说明
**不配置 `cmake.cmakePath` 硬编码路径！**
通过 `source conanbuild.sh` 注入环境，保证：
- 跨设备可用
- 团队可用
- 模板可直接开源

```json
// .vscode/settings.json 示例
{
    "clangd.arguments": ["--compile-commands-dir=${workspaceFolder}/build"],
    "C_Cpp.intelliSenseEngine": "disabled"
}
```

---

## 🐛 调试（F5 一键）
- 自动编译
- 终端输出
- 无 SIGSEGV
- 条件断点正常
- C++23 容器正常显示

---

## 📌 已解决的关键问题
- **`<print>` 找不到**：确保 Clang 21 + C++23
- **使用系统 GCC 而非 Clang**：必须 `source conanbuild.sh`
- **VSCode CMake 路径不可移植**：不硬编码，使用环境注入
- **SIGSEGV 崩溃**：`stopOnEntry: false`
- **条件断点失效**：`expressions: native`
- **超长命令行易出错**：全部放入 Conan Profile

---

## 🧹 代码静态检查（Clang-Tidy）
```bash
./scripts/install-githooks.sh
```
提交代码自动检查，保证代码质量。

---

## 🎯 适用场景
- C++ 初学者
- Modern CMake 学习
- Clang + C++23 开发
- **工业级可移植项目**
- 团队协作、多设备同步开发
- 课程作业 / Demo / 小型项目

---

## 📄 License
MIT

---

# 我帮你改了哪些关键东西？
✅ 去掉了旧的 `CMakePresets.json` 手动配置（Conan 自动生成）
✅ 修正了项目结构（加入 `conanfile.py`）
✅ 明确：**CMake/Ninja 由 Conan 安装，不用预装**
✅ 强调：**不硬编码路径，保证可移植**
✅ 把所有 `-s` 参数解释清楚
✅ 把 `source conanbuild.sh` 标为**必须步骤**
✅ 统一术语、专业、简洁、可开源
✅ 修复所有不清晰、矛盾、遗漏的内容
