#!/usr/bin/env python3
"""
Validation script for product-opportunity-skills repository.

Checks:
- Frontmatter format in all SKILL.md and AGENT.md files
- Skill references in agent files
- Directory structure
- Documentation completeness
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Dict, Set

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

def print_success(msg: str):
    print(f"{Colors.GREEN}✓{Colors.END} {msg}")

def print_error(msg: str):
    print(f"{Colors.RED}✗{Colors.END} {msg}")

def print_warning(msg: str):
    print(f"{Colors.YELLOW}⚠{Colors.END} {msg}")

def print_info(msg: str):
    print(f"{Colors.BLUE}ℹ{Colors.END} {msg}")

def extract_frontmatter(content: str) -> Dict[str, str]:
    """Extract YAML frontmatter from markdown content."""
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return {}

    frontmatter = {}
    for line in match.group(1).split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            frontmatter[key.strip()] = value.strip()

    return frontmatter

def validate_skill_file(file_path: Path) -> List[str]:
    """Validate a SKILL.md file."""
    errors = []

    with open(file_path, 'r') as f:
        content = f.read()

    # Check frontmatter
    frontmatter = extract_frontmatter(content)

    required_fields = ['name', 'description', 'version', 'author']
    for field in required_fields:
        if field not in frontmatter:
            errors.append(f"Missing required frontmatter field: {field}")

    # Check content structure
    if '## What This Skill Does' not in content:
        errors.append("Missing '## What This Skill Does' section")

    if '## When to Use' not in content:
        errors.append("Missing '## When to Use' section")

    return errors

def validate_agent_file(file_path: Path, available_skills: Set[str]) -> List[str]:
    """Validate an AGENT.md file."""
    errors = []

    with open(file_path, 'r') as f:
        content = f.read()

    # Check frontmatter
    frontmatter = extract_frontmatter(content)

    required_fields = ['name', 'description', 'version', 'author']
    for field in required_fields:
        if field not in frontmatter:
            errors.append(f"Missing required frontmatter field: {field}")

    # Check skill references in the "Skills Used" section
    skills_section_match = re.search(r'## Skills Used\n\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
    if skills_section_match:
        skills_section = skills_section_match.group(1)
        # Find skill references like "- `skill-name`"
        referenced_skills = re.findall(r'- `([^`]+)`', skills_section)
        for skill in referenced_skills:
            if skill not in available_skills:
                errors.append(f"Referenced skill '{skill}' not found in vertical-plugins/")

    # Check content structure
    if '## What This Agent Does' not in content:
        errors.append("Missing '## What This Agent Does' section")

    if '## Usage' not in content:
        errors.append("Missing '## Usage' section")

    if '## Workflow' not in content:
        errors.append("Missing '## Workflow' section")

    return errors

def validate_directory_structure(repo_root: Path) -> List[str]:
    """Validate repository directory structure."""
    errors = []

    required_dirs = [
        'agent-plugins',
        'vertical-plugins',
        'examples',
        'scripts'
    ]

    for dir_name in required_dirs:
        dir_path = repo_root / dir_name
        if not dir_path.exists():
            errors.append(f"Missing required directory: {dir_name}/")

    # Check README exists
    if not (repo_root / 'README.md').exists():
        errors.append("Missing README.md")

    return errors

def find_all_skills(repo_root: Path) -> Set[str]:
    """Find all available skills in vertical-plugins/."""
    skills = set()
    vertical_dir = repo_root / 'vertical-plugins'

    if vertical_dir.exists():
        for skill_dir in vertical_dir.iterdir():
            if skill_dir.is_dir():
                skills.add(skill_dir.name)

    return skills

def main():
    print_info("Validating product-opportunity-skills repository...\n")

    # Get repository root
    repo_root = Path(__file__).parent.parent

    total_errors = 0

    # 1. Validate directory structure
    print_info("Checking directory structure...")
    structure_errors = validate_directory_structure(repo_root)
    if structure_errors:
        for error in structure_errors:
            print_error(error)
            total_errors += 1
    else:
        print_success("Directory structure valid")
    print()

    # 2. Find all available skills
    available_skills = find_all_skills(repo_root)
    print_info(f"Found {len(available_skills)} skills: {', '.join(sorted(available_skills))}\n")

    # 3. Validate vertical plugins (skills)
    print_info("Validating vertical plugins...")
    vertical_dir = repo_root / 'vertical-plugins'
    if vertical_dir.exists():
        for skill_dir in vertical_dir.iterdir():
            if skill_dir.is_dir():
                skill_file = skill_dir / 'SKILL.md'
                if skill_file.exists():
                    errors = validate_skill_file(skill_file)
                    if errors:
                        print_error(f"{skill_dir.name}/SKILL.md:")
                        for error in errors:
                            print(f"  - {error}")
                            total_errors += 1
                    else:
                        print_success(f"{skill_dir.name}/SKILL.md")
                else:
                    print_error(f"{skill_dir.name}/ missing SKILL.md")
                    total_errors += 1
    print()

    # 4. Validate agent plugins
    print_info("Validating agent plugins...")
    agent_dir = repo_root / 'agent-plugins'
    if agent_dir.exists():
        for agent_subdir in agent_dir.iterdir():
            if agent_subdir.is_dir():
                agent_file = agent_subdir / 'AGENT.md'
                if agent_file.exists():
                    errors = validate_agent_file(agent_file, available_skills)
                    if errors:
                        print_error(f"{agent_subdir.name}/AGENT.md:")
                        for error in errors:
                            print(f"  - {error}")
                            total_errors += 1
                    else:
                        print_success(f"{agent_subdir.name}/AGENT.md")
                else:
                    print_error(f"{agent_subdir.name}/ missing AGENT.md")
                    total_errors += 1
    print()

    # 5. Check examples
    print_info("Checking examples...")
    examples_dir = repo_root / 'examples'
    if examples_dir.exists():
        example_count = len(list(examples_dir.iterdir()))
        if example_count > 0:
            print_success(f"Found {example_count} example(s)")
        else:
            print_warning("No examples found")
    print()

    # Summary
    print("=" * 60)
    if total_errors == 0:
        print_success("All validation checks passed!")
        return 0
    else:
        print_error(f"Validation failed with {total_errors} error(s)")
        return 1

if __name__ == '__main__':
    sys.exit(main())
