# Quick Start Guide

## Installation

```bash
npx skills add https://github.com/uu-z/product-opportunity-analyzer
```

This will install all 3 vertical skills + 1 agent plugin to your AI coding environment.

## Usage

### Option 1: Use Individual Skills

**Product Analysis:**
```
Use the product-analysis skill to evaluate this idea:
"A CI/CD cost optimizer that analyzes GitHub Actions usage and suggests optimizations"
```

**Document Generation:**
```
Use the document-generation skill to create a PRD for the CI/CD optimizer
```

**Prototype Generation:**
```
Use the prototype-generation skill to create an interactive dashboard prototype for the CI/CD optimizer
```

### Option 2: Use Complete Agent Workflow

**Quick Analysis (30 min):**
```
Use the product-opportunity-analyzer agent in quick mode to evaluate:
"A CI/CD cost optimizer for engineering teams"
```

**Standard Analysis (90 min):**
```
Use the product-opportunity-analyzer agent to analyze this opportunity:

Idea: CI/CD Cost Optimizer
Context: Series A startup, 15 engineers, $2M ARR, expertise in DevOps automation,
looking for B2B SaaS with <$10K CAC, need to reach $5M ARR in 12 months
```

**Deep Analysis with Prototype (3-4 hours):**
```
Use the product-opportunity-analyzer agent in deep mode with prototype generation:

Idea: AI-powered financial research assistant
Target: Hedge funds and asset managers
Context: Pre-seed, 2 founders (ML + finance), access to proprietary trading data,
looking for B2B with $20K+ ACV
```

## What You'll Get

### From Individual Skills:
- **product-analysis**: YC-style scoring (10 dimensions), four-quadrant analysis, prioritization
- **document-generation**: 5 professional documents (Strategy, PRD, Architecture, GTM, Roadmap)
- **prototype-generation**: Interactive HTML prototype with your chosen design system

### From Complete Agent:
1. **Discovery Phase**: Market research, competitive analysis, user insights
2. **Scoring Phase**: YC-style 10-dimension evaluation
3. **Prioritization Phase**: Four-quadrant analysis, opportunity ranking
4. **Validation Phase**: Business model validation, risk assessment
5. **Documentation Phase**: Complete document package (5 files)
6. **Prototyping Phase** (optional): Interactive visual prototype

## Output Structure

```
your-product-name/
├── 01-Product-Strategy.md
├── 02-PRD.md
├── 03-Tech-Architecture.md
├── 04-GTM-Plan.md
├── 05-12-Month-Roadmap.md
└── prototype/
    └── index.html (interactive prototype)
```

## Supported AI Tools

Works with 55+ AI coding agents including:
- Claude Code
- Cursor
- Windsurf
- Cline
- Zed AI
- Continue
- And more...

## Examples

See `examples/` directory for:
- Complete SaaS product analysis walkthrough
- Interactive dashboard prototype (CI/CD optimizer)

## Tips

1. **Provide context**: The more context you provide (team size, expertise, constraints), the better the analysis
2. **Start with quick mode**: Test the waters with a 30-min quick analysis before committing to deep mode
3. **Use prototypes for validation**: Visual prototypes help validate ideas with stakeholders faster
4. **Iterate**: Use the skills independently to refine specific aspects (e.g., just regenerate the GTM plan)

## Need Help?

- Check `examples/saas-product-analysis/README.md` for a detailed walkthrough
- Open an issue at https://github.com/uu-z/product-opportunity-analyzer/issues
- Review the skill documentation in `vertical-plugins/*/SKILL.md`
