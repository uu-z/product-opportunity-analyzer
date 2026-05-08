# End-to-End Testing Guide

Complete testing workflow to validate all skills and agent functionality.

## Prerequisites

```bash
# 1. Install the skills
npx skills add https://github.com/uu-z/product-opportunity-analyzer

# 2. Verify installation
ls ~/.claude/skills/  # Should see product-opportunity-analyzer files
# OR
ls ~/.cursor/skills/  # Depending on your AI tool
```

## Test Suite

### Test 1: Validation Script ✓

**Purpose**: Verify repository structure and file integrity

```bash
cd /path/to/product-opportunity-skills
python3 scripts/validate.py
```

**Expected Output**:
```
✓ Directory structure valid
✓ Found 3 skills: document-generation, product-analysis, prototype-generation
✓ All validation checks passed!
```

**Pass Criteria**: Exit code 0, no errors

---

### Test 2: Individual Skill - Product Analysis

**Purpose**: Test YC-style scoring framework

**Input**:
```
Use the product-analysis skill to evaluate this product idea:

Product: AI-powered code review assistant
Domain: Developer tools
Context: Startup with 2 technical founders, expertise in ML and DevOps,
$500K seed funding, targeting engineering teams at Series A-C startups
```

**Expected Output**:
- 10-dimension scoring table (Problem Clarity, Market Size, etc.)
- Each dimension scored 0-10
- Overall score and tier (S/A/B/C)
- Four-quadrant positioning
- Business model recommendations

**Pass Criteria**:
- ✓ All 10 dimensions evaluated
- ✓ Scores are numeric (0-10)
- ✓ Tier assignment is logical
- ✓ Recommendations are specific

---

### Test 3: Individual Skill - Document Generation

**Purpose**: Test document template generation

**Input**:
```
Use the document-generation skill to create a PRD for:

Product: TaskFlow - Team task management tool
Features: Task assignment, Time tracking, Team collaboration
Target: Remote teams (10-50 people)
```

**Expected Output**:
```
taskflow/
├── 01-product-strategy.md
├── 02-prd.md
├── 03-technical-architecture.md
├── 04-gtm-plan.md
└── 05-roadmap-12m.md
```

**Pass Criteria**:
- ✓ All 5 documents generated
- ✓ Each document follows template structure
- ✓ Content is specific (not generic placeholders)
- ✓ Cross-references between docs are consistent

**Validation Commands**:
```bash
# Check all files exist
ls taskflow/*.md | wc -l  # Should be 5

# Check content quality
grep -c "TODO\|PLACEHOLDER\|XXX" taskflow/*.md  # Should be 0

# Check file sizes (should have substantial content)
wc -l taskflow/*.md  # Each should be >100 lines
```

---

### Test 4: Individual Skill - Prototype Generation

**Purpose**: Test interactive prototype creation

**Input**:
```
Use the prototype-generation skill to create a web app prototype for:

Product: TaskFlow
Type: Web App (SaaS Dashboard)
Features: Task list, Team members, Time tracking dashboard
Design System: Modern Minimal
Brand Colors: #3b82f6 (primary), #8b5cf6 (accent)
```

**Expected Output**:
```
taskflow-prototype/
├── index.html
└── README.md
```

**Pass Criteria**:
- ✓ HTML file is valid and complete
- ✓ Includes CSS (inline or embedded)
- ✓ Has interactive elements (buttons, forms)
- ✓ Responsive design (mobile-friendly)
- ✓ Uses specified brand colors

**Validation Commands**:
```bash
# Check HTML validity
grep -q "<!DOCTYPE html>" taskflow-prototype/index.html && echo "✓ Valid HTML"

# Check for interactivity
grep -q "<script>" taskflow-prototype/index.html && echo "✓ Has JavaScript"

# Check for brand colors
grep -q "#3b82f6" taskflow-prototype/index.html && echo "✓ Uses brand colors"

# Open in browser for visual inspection
open taskflow-prototype/index.html  # macOS
# OR
xdg-open taskflow-prototype/index.html  # Linux
```

**Manual Checks**:
- [ ] Opens in browser without errors
- [ ] Layout looks professional
- [ ] Buttons are clickable
- [ ] Responsive on mobile (resize browser)

---

### Test 5: Complete Agent Workflow - Quick Mode

**Purpose**: Test 30-minute quick analysis

**Input**:
```
Use the product-opportunity-analyzer agent in quick mode:

Domain: Fintech
Context: Solo founder, 10 years in banking, $0 budget,
looking for bootstrappable B2B SaaS opportunity
```

**Expected Output**:
1. Opportunity pool (10-15 ideas)
2. YC scoring matrix
3. Top 3 recommendations
4. Business model summary for each

**Pass Criteria**:
- ✓ Generates 10-15 distinct ideas
- ✓ Each idea has YC score
- ✓ Top 3 are clearly identified
- ✓ Business models are specific (pricing, CAC, LTV)
- ✓ Completes in ~30 minutes

**Timing Test**:
```bash
# Start timer
start_time=$(date +%s)

# Run analysis (in your AI tool)
# ...

# End timer
end_time=$(date +%s)
duration=$((end_time - start_time))
echo "Duration: $((duration / 60)) minutes"

# Should be ~30 minutes (±10 minutes acceptable)
```

---

### Test 6: Complete Agent Workflow - Standard Mode

**Purpose**: Test 90-minute standard analysis with full documentation

**Input**:
```
Use the product-opportunity-analyzer agent in standard mode:

Domain: Developer tools
Context: Pre-seed startup, 2 technical founders (ML + full-stack),
$500K runway, expertise in DevOps and CI/CD, looking for B2B SaaS
with <$50K CAC, need to reach $1M ARR in 18 months
```

**Expected Output**:
1. Quick analysis content (from Test 5)
2. **+ Full documentation for Top 1 idea**:
   - 01-product-strategy.md
   - 02-prd.md
   - 03-technical-architecture.md
   - 04-gtm-plan.md
   - 05-roadmap-12m.md
   - README.md

**Pass Criteria**:
- ✓ All quick mode outputs present
- ✓ All 5 documents generated for Top 1 idea
- ✓ Documents are interconnected (consistent naming, cross-references)
- ✓ Includes specific numbers (pricing, timeline, metrics)
- ✓ Completes in ~90 minutes

**Validation Script**:
```bash
#!/bin/bash
# validate-standard-output.sh

OUTPUT_DIR="$1"  # e.g., "ci-cd-optimizer"

echo "Validating standard mode output..."

# Check directory exists
if [ ! -d "$OUTPUT_DIR" ]; then
    echo "✗ Output directory not found"
    exit 1
fi

# Check all required files
required_files=(
    "01-product-strategy.md"
    "02-prd.md"
    "03-technical-architecture.md"
    "04-gtm-plan.md"
    "05-roadmap-12m.md"
    "README.md"
)

for file in "${required_files[@]}"; do
    if [ -f "$OUTPUT_DIR/$file" ]; then
        lines=$(wc -l < "$OUTPUT_DIR/$file")
        if [ $lines -gt 50 ]; then
            echo "✓ $file ($lines lines)"
        else
            echo "✗ $file too short ($lines lines)"
        fi
    else
        echo "✗ $file missing"
    fi
done

# Check for specific content markers
echo ""
echo "Content quality checks:"

grep -q "Market Size" "$OUTPUT_DIR/01-product-strategy.md" && echo "✓ Strategy has market sizing"
grep -q "User Stories" "$OUTPUT_DIR/02-prd.md" && echo "✓ PRD has user stories"
grep -q "Tech Stack" "$OUTPUT_DIR/03-technical-architecture.md" && echo "✓ Architecture has tech stack"
grep -q "Marketing Strategy" "$OUTPUT_DIR/04-gtm-plan.md" && echo "✓ GTM has marketing strategy"
grep -q "Month 1-3" "$OUTPUT_DIR/05-roadmap-12m.md" && echo "✓ Roadmap has monthly milestones"

echo ""
echo "Validation complete!"
```

**Usage**:
```bash
chmod +x validate-standard-output.sh
./validate-standard-output.sh ci-cd-optimizer
```

---

### Test 7: Complete Agent Workflow - Deep Mode with Prototype

**Purpose**: Test 3-4 hour deep analysis with prototype

**Input**:
```
Use the product-opportunity-analyzer agent in deep mode with prototype generation:

Domain: Healthcare AI
Context: Series A startup, 20-person team, $5M raised,
expertise in medical imaging and ML, FDA clearance in progress,
targeting radiology departments at hospitals, need $10M ARR in 24 months
```

**Expected Output**:
1. Standard mode outputs
2. **+ Documentation for Top 3 ideas** (not just Top 1)
3. **+ Interactive prototype for Top 1 idea**
4. **+ Comparative analysis** (Top 3 comparison table)
5. **+ Execution priorities** (what to do first)

**Pass Criteria**:
- ✓ 3 complete document sets (15 files total)
- ✓ 1 interactive prototype (HTML)
- ✓ Comparative analysis table
- ✓ Prioritized action plan
- ✓ Completes in 3-4 hours

**Validation Script**:
```bash
#!/bin/bash
# validate-deep-output.sh

echo "Validating deep mode output..."

# Check for 3 product directories
product_dirs=$(find . -maxdepth 1 -type d -name "*-product-*" | wc -l)
if [ $product_dirs -ge 3 ]; then
    echo "✓ Found $product_dirs product directories"
else
    echo "✗ Expected 3+ product directories, found $product_dirs"
fi

# Check for prototype
if [ -f "*/prototype/index.html" ] || [ -f "*-prototype/index.html" ]; then
    echo "✓ Prototype found"

    # Validate prototype
    prototype=$(find . -name "index.html" -path "*/prototype/*" | head -1)
    if grep -q "<!DOCTYPE html>" "$prototype"; then
        echo "  ✓ Valid HTML"
    fi
    if grep -q "<script>" "$prototype"; then
        echo "  ✓ Has interactivity"
    fi
else
    echo "✗ Prototype not found"
fi

# Check for comparative analysis
if grep -rq "Comparative Analysis\|Comparison Table" .; then
    echo "✓ Comparative analysis found"
else
    echo "✗ Comparative analysis missing"
fi

# Check for execution priorities
if grep -rq "Execution Priorities\|Action Plan\|Next Steps" .; then
    echo "✓ Execution priorities found"
else
    echo "✗ Execution priorities missing"
fi

echo ""
echo "Deep mode validation complete!"
```

---

### Test 8: Cross-Tool Compatibility

**Purpose**: Verify skills work across different AI coding tools

**Test Matrix**:

| Tool | Installation | Skill Invocation | Output Quality |
|------|--------------|------------------|----------------|
| Claude Code | ✓ | ✓ | ✓ |
| Cursor | ? | ? | ? |
| Windsurf | ? | ? | ? |
| Cline | ? | ? | ? |

**Test Procedure** (for each tool):

1. Install skills:
   ```bash
   npx skills add https://github.com/uu-z/product-opportunity-analyzer
   ```

2. Verify installation:
   ```bash
   # Check tool-specific directory
   ls ~/.claude/skills/     # Claude Code
   ls ~/.cursor/skills/     # Cursor
   ls ~/.windsurf/skills/   # Windsurf
   ```

3. Run simple test:
   ```
   Use the product-analysis skill to score this idea:
   "A simple todo app for developers"
   ```

4. Check output quality:
   - [ ] Skill executes without errors
   - [ ] Output format is correct
   - [ ] Content is relevant

---

### Test 9: Error Handling

**Purpose**: Test graceful failure and error messages

**Test Cases**:

**9.1 Missing Required Parameters**
```
Use the product-opportunity-analyzer agent with no context
```
**Expected**: Clear error message requesting required parameters

**9.2 Invalid Input**
```
Use the prototype-generation skill with:
Type: InvalidType
```
**Expected**: Error message listing valid types

**9.3 Conflicting Requirements**
```
Use the document-generation skill for a product with:
- Must be HIPAA compliant
- Must launch in 2 weeks
- $0 budget
```
**Expected**: Warning about conflicting constraints

---

### Test 10: Performance Benchmarks

**Purpose**: Measure execution time and resource usage

**Benchmarks**:

| Test | Expected Time | Acceptable Range |
|------|---------------|------------------|
| Product Analysis | 5 min | 3-10 min |
| Document Generation | 10 min | 5-15 min |
| Prototype Generation | 5 min | 3-10 min |
| Quick Mode (Agent) | 30 min | 20-40 min |
| Standard Mode (Agent) | 90 min | 60-120 min |
| Deep Mode (Agent) | 3-4 hours | 2.5-5 hours |

**Timing Script**:
```bash
#!/bin/bash
# benchmark.sh

test_name="$1"
start_time=$(date +%s)

echo "Starting benchmark: $test_name"
echo "Start time: $(date)"

# Run your test here
# ...

end_time=$(date +%s)
duration=$((end_time - start_time))
minutes=$((duration / 60))
seconds=$((duration % 60))

echo ""
echo "Benchmark complete: $test_name"
echo "Duration: ${minutes}m ${seconds}s"
echo "End time: $(date)"
```

---

## Complete Test Checklist

Run all tests in sequence:

```bash
# 1. Validation
[ ] python3 scripts/validate.py

# 2. Individual Skills
[ ] Test product-analysis skill
[ ] Test document-generation skill
[ ] Test prototype-generation skill

# 3. Agent Workflows
[ ] Test quick mode (30 min)
[ ] Test standard mode (90 min)
[ ] Test deep mode (3-4 hours)

# 4. Quality Checks
[ ] Run validation scripts
[ ] Manual review of outputs
[ ] Cross-tool compatibility

# 5. Edge Cases
[ ] Error handling
[ ] Performance benchmarks
```

## Automated Test Suite

Create a master test script:

```bash
#!/bin/bash
# run-all-tests.sh

echo "========================================="
echo "Product Opportunity Skills - Test Suite"
echo "========================================="
echo ""

# Test 1: Validation
echo "Test 1: Repository Validation"
python3 scripts/validate.py
if [ $? -eq 0 ]; then
    echo "✓ PASS"
else
    echo "✗ FAIL"
    exit 1
fi
echo ""

# Test 2-4: Individual skills (manual)
echo "Test 2-4: Individual Skills"
echo "⚠ Manual testing required"
echo "  - Run product-analysis skill"
echo "  - Run document-generation skill"
echo "  - Run prototype-generation skill"
echo ""

# Test 5-7: Agent workflows (manual)
echo "Test 5-7: Agent Workflows"
echo "⚠ Manual testing required"
echo "  - Run quick mode"
echo "  - Run standard mode"
echo "  - Run deep mode"
echo ""

# Test 8: Cross-tool compatibility (manual)
echo "Test 8: Cross-Tool Compatibility"
echo "⚠ Manual testing required"
echo ""

# Test 9: Error handling (manual)
echo "Test 9: Error Handling"
echo "⚠ Manual testing required"
echo ""

# Test 10: Performance benchmarks (manual)
echo "Test 10: Performance Benchmarks"
echo "⚠ Manual testing required"
echo ""

echo "========================================="
echo "Test suite complete!"
echo "========================================="
```

## Success Criteria

**Minimum Viable**:
- ✓ All validation checks pass
- ✓ At least 1 skill works end-to-end
- ✓ Quick mode agent completes successfully

**Production Ready**:
- ✓ All 3 skills work independently
- ✓ All 3 agent modes complete successfully
- ✓ Works on at least 2 different AI tools
- ✓ All validation scripts pass
- ✓ Performance within acceptable ranges

**Excellent**:
- ✓ All tests pass
- ✓ Works on 3+ AI tools
- ✓ Performance at or better than expected
- ✓ No errors in edge cases
- ✓ User feedback is positive

## Reporting Issues

If tests fail, report with:
1. Test number and name
2. Input provided
3. Expected output
4. Actual output
5. Error messages
6. Environment (OS, AI tool, version)

Open issues at: https://github.com/uu-z/product-opportunity-analyzer/issues
