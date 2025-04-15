#!/bin/bash

# 获取当前文件夹名作为环境名
project_name=$(basename "$PWD")

# 替换 env.yml 中的 name
sed "s/{{project_name}}/$project_name/" env.yml > temp_env.yml

echo "Creating conda environment: $project_name"
conda env create -f temp_env.yml

echo "Activating environment: $project_name"
conda activate $project_name

rm temp_env.yml

# 初始化项目文件
touch main.py README.md
echo ".ipynb_checkpoints/" >> .gitignore

echo "Opening in VSCode..."
code .
