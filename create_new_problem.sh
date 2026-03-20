#!/bin/bash

# Get the latest problem number
latest_problem=$(ls -d problems/problem_* 2>/dev/null | sed 's/.*problem_//' | sort -n | tail -1 | sed 's/^0//')

if [ -z "$latest_problem" ]; then
    echo "No problems found. Creating problem_01..."
    next_num=1
else
    next_num=$((latest_problem + 1))
fi

# Format with leading zeros (e.g., problem_01, problem_02, etc.)
next_dir=$(printf "problem_%02d" $next_num)
next_path="problems/$next_dir"
problem_num=$(printf "%02d" $next_num)

# Create the new problem directory
mkdir -p "$next_path"

# Create __init__.py (empty)
touch "$next_path/__init__.py"

# Create problem.py from template
sed "s/NUMBER/$problem_num/g" templates/problem_template.txt > "$next_path/problem.py"

# Create problem_statement.md from template
sed "s/NUMBER/$problem_num/g" templates/problem_statement_template.txt > "$next_path/problem_statement.md"

# Create test file in tests directory
test_file="tests/test_$problem_num.py"
sed "s/NUMBER/$problem_num/g" templates/problem_test_template.txt > "$test_file"

echo "Created $next_path/"
echo "Files created:"
ls -la "$next_path/"
echo ""
echo "Created $test_file"
ls -la "$test_file"
