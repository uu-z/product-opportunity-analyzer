# Product Opportunity Skills

> Professional product opportunity analysis skills for AI coding agents

A comprehensive collection of skills and agents for evaluating product opportunities, validating business models, and generating complete planning documentation.

## Quick Start

```bash
# Install using Vercel Skills CLI
npx skills add https://github.com/uu-z/product-opportunity-skills

# Use in your AI coding agent
/product-opportunity-analyzer "developer tools" "Solo founder, 10 years SaaS experience"
```

## What's Included

### 🤖 Agent Plugins (Complete Workflows)

| Agent | Description | Use Case |
|-------|-------------|----------|
| **product-opportunity-analyzer** | End-to-end opportunity analysis | Evaluate ideas, generate docs |

### ⚡ Vertical Plugins (Core Skills)

| Skill | Description | Use Case |
|-------|-------------|----------|
| **product-analysis** | YC-style scoring framework | Score and prioritize opportunities |
| **document-generation** | Professional doc templates | Generate PRD, strategy, roadmap |
| **prototype-generation** | Interactive HTML prototypes | Visualize concepts, test with users |

### 📚 Examples

| Example | Description |
|---------|-------------|
| **saas-product-analysis** | Complete B2B SaaS analysis walkthrough |

## Features

- ✅ **YC-Style Evaluation** - 10-dimension scoring framework (0-10 scale)
- ✅ **Four-Quadrant Analysis** - Value vs. Difficulty prioritization
- ✅ **Business Model Validation** - Revenue, pricing, unit economics
- ✅ **Complete Documentation** - Strategy, PRD, architecture, GTM, roadmap
- ✅ **Interactive Prototypes** - HTML prototypes for web/mobile/dashboard/landing pages
- ✅ **Multiple Depth Levels** - Quick (30min), Standard (90min), Deep (3-4hr)
- ✅ **Universal Compatibility** - Works with 55+ AI coding agents

## Installation

### Option 1: Vercel Skills CLI (Recommended)

```bash
npx skills add https://github.com/uu-z/product-opportunity-skills
```

This automatically installs for all detected AI coding agents.

### Option 2: Manual Installation

#### For Claude Code
```bash
mkdir -p ~/.claude/skills
curl -o ~/.claude/skills/product-opportunity-analyzer.md \
  https://raw.githubusercontent.com/uu-z/product-opportunity-skills/main/agent-plugins/product-opportunity-analyzer/AGENT.md
```

#### For Cursor
```bash
mkdir -p ~/.cursor/skills
curl -o ~/.cursor/skills/product-opportunity-analyzer.md \
  https://raw.githubusercontent.com/uu-z/product-opportunity-skills/main/agent-plugins/product-opportunity-analyzer/AGENT.md
```

## Usage

### Basic Usage

```bash
/product-opportunity-analyzer [domain] [context]
```

### Examples

**Startup Founder**:
```bash
/product-opportunity-analyzer "fintech" \
  "Context: Solo founder, 10 years in banking, $500K seed round, \
   looking for B2B SaaS with <$50K CAC"
```

**Corporate Innovation**:
```bash
/product-opportunity-analyzer "enterprise AI" \
  "Context: Fortune 500, 50-person team, $10M budget, \
   6-month timeline, regulatory compliance required"
```

**Product Manager**:
```bash
/product-opportunity-analyzer "developer tools" \
  "Context: 100-person SaaS company, $50M ARR, 10K customers, \
   evaluating adjacent product opportunities"
```

## Output

### Quick Analysis (30 minutes)
- 10-15 product ideas
- YC scoring matrix
- Top 3 recommendations
- Business model summary

### Standard Analysis (90 minutes)
- Quick analysis content
- **+ Complete documentation for Top 1 idea**:
  - Product Strategy
  - PRD
  - Technical Architecture
  - Go-to-Market Plan
  - 12-Month Roadmap

### Deep Analysis (3-4 hours)
- Standard analysis content
- **+ Documentation for Top 3 ideas**
- **+ Interactive prototype for Top 1 idea** (web/mobile/dashboard/landing page)
- **+ Comparative analysis**
- **+ Execution priorities**

## Evaluation Framework

### YC Scoring Dimensions (0-10 scale)

1. **Problem Clarity** - Is the problem well-defined and painful?
2. **Market Size** - TAM > $1B? Growing market?
3. **Solution Fit** - 10x better than alternatives?
4. **Unfair Advantage** - What moat do you have?
5. **Go-to-Market** - Clear acquisition channel?
6. **Business Model** - Recurring revenue? High margins?
7. **Team Fit** - Domain expertise? Technical capability?
8. **Timing** - Why now? Market tailwinds?
9. **Traction** - Revenue? User growth? PMF proof?
10. **Vision** - Billion-dollar outcome possible?

### Scoring Tiers

- 🏆 **S-tier (8.5+)**: Exceptional, top 1% opportunity
- 🥇 **A-tier (8.0-8.4)**: Strong, worth pursuing
- 🥈 **B-tier (7.0-7.9)**: Decent, needs refinement
- 📋 **C-tier (<7.0)**: Weak, reconsider or pivot

## Architecture

Following [Anthropic's financial-services](https://github.com/anthropics/financial-services) structure:

```
product-opportunity-skills/
├── agent-plugins/              # Complete workflow agents
│   └── product-opportunity-analyzer/
│       └── AGENT.md
│
├── vertical-plugins/           # Reusable core skills
│   ├── product-analysis/
│   │   └── SKILL.md
│   └── document-generation/
│       └── SKILL.md
│
├── examples/                   # Real-world examples
│   └── saas-product-analysis/
│       └── README.md
│
└── scripts/                    # Automation tools
    └── validate.py
```

## Supported AI Agents

Works with 55+ AI coding agents including:

- ✅ Claude Code
- ✅ Cursor
- ✅ Windsurf
- ✅ Cline
- ✅ Continue
- ✅ GitHub Copilot
- ✅ Goose
- ✅ Roo Code
- ✅ And 47 more...

See [full list](https://github.com/vercel-labs/skills#supported-agents)

## Best Practices

### 1. Provide Rich Context

❌ **Bad**:
```bash
/product-opportunity-analyzer "fintech"
```

✅ **Good**:
```bash
/product-opportunity-analyzer "fintech lending" \
  "Context: 2 founders (ex-banking + tech), $500K raised, \
   100 beta users, $50K MRR, access to credit bureau data, \
   seeking $2M seed round, need to reach $1M ARR in 18 months"
```

### 2. Be Specific About Domain

- ✅ "AI-powered medical imaging for radiology"
- ❌ "healthcare"

### 3. Include Constraints

- Budget: "$500K seed round"
- Timeline: "Launch in 6 months"
- Team: "2 engineers, no sales experience"
- Regulatory: "HIPAA compliance required"

### 4. State Your Advantages

- "10 years domain expertise"
- "Access to proprietary data"
- "Existing customer base of 1000 users"
- "Partnership with major player"

## Use Cases

### 🚀 Startup Founders
- Find product-market fit
- Validate business model
- Prepare YC application
- Create investor materials

### 💼 Product Managers
- Evaluate new opportunities
- Prioritize roadmap
- Write PRDs
- Competitive analysis

### 💰 Investors
- Due diligence
- Market assessment
- Founder-market fit evaluation
- Risk identification

### 🏢 Corporate Innovation
- Internal incubation
- Strategic planning
- Market entry analysis
- Build vs. buy decisions

## Examples

See [`examples/saas-product-analysis/`](examples/saas-product-analysis/) for a complete walkthrough:

- Input: Developer tools domain, solo founder context
- Output: 10 ideas → YC scoring → Top 3 analysis → Complete docs
- Result: Clear recommendation with $1M ARR path

## Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Follow the [Anthropic financial-services](https://github.com/anthropics/financial-services) structure
4. Submit a pull request

### Adding New Skills

```bash
# Create new vertical skill
mkdir -p vertical-plugins/your-skill
# Add SKILL.md with frontmatter

# Or create new agent
mkdir -p agent-plugins/your-agent
# Add AGENT.md with skill references
```

## Validation

Run validation checks:

```bash
python3 scripts/validate.py
```

Checks:
- ✅ Frontmatter format
- ✅ Skill references
- ✅ File structure
- ✅ Documentation completeness

## License

MIT

## Acknowledgments

- Inspired by [YC's evaluation framework](https://www.ycombinator.com/)
- Structure based on [Anthropic's financial-services](https://github.com/anthropics/financial-services)
- Built on [Vercel Skills](https://github.com/vercel-labs/skills) standard
- Powered by Claude Opus 4.6

## Support

- 📖 [Documentation](https://github.com/uu-z/product-opportunity-skills)
- 🐛 [Issues](https://github.com/uu-z/product-opportunity-skills/issues)
- 💬 [Discussions](https://github.com/uu-z/product-opportunity-skills/discussions)

---

**Make product opportunity analysis as simple as writing code** 🚀
