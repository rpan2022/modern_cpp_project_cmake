#!/bin/bash
# 配置 Git 使用项目内 .githooks 作为钩子目录
git config core.hooksPath .githooks
echo -e "\033[32m✅ Git 钩子配置完成，提交自动运行 Clang-Tidy\033[0m"
