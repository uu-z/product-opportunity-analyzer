---
name: product-opportunity-analyzer
description: Complete product opportunity analysis workflow - from idea evaluation to full documentation package
version: 1.0.0
author: Product Opportunity Skills
skills:
  - product-analysis
  - document-generation
  - prototype-generation
---

# Product Opportunity Analyzer Agent

End-to-end workflow for analyzing product opportunities and generating complete planning documentation with optional interactive prototypes.

## What This Agent Does

Executes a comprehensive 5-6 phase analysis:

1. **Opportunity Discovery** - Generate 10-15 product ideas based on domain and context
2. **YC-Style Scoring** - Evaluate each idea across 10 dimensions (0-10 scale)
3. **Prioritization** - Rank opportunities using four-quadrant analysis
4. **Business Validation** - Validate business model, pricing, unit economics
5. **Documentation** - Generate complete planning docs for top opportunities
6. **Prototype Generation** (Optional) - Create interactive HTML prototypes for visualization

## When to Use

- Exploring new product directions
- Evaluating multiple opportunities
- Preparing for investor pitches
- Strategic planning sessions
- YC application preparation

## Usage

```bash
/product-opportunity-analyzer [domain] [context]
```

### Parameters

- `domain` (required): Target market or industry (e.g., "developer tools", "fintech", "healthcare AI")
- `context` (optional): Background information about your situation, resources, and constraints

### Examples

```bash
# Startup founder exploring opportunities
/product-opportunity-analyzer "developer tools" \
  "Context: Solo technical founder, 10 years SaaS experience, $0 budget, \
   looking for bootstrappable B2B opportunity"

# Corporate innovation team
/product-opportunity-analyzer "enterprise AI" \
  "Context: Fortune 500 company, 50-person team, $10M budget, \
   6-month timeline, regulatory compliance required"

# Pre-seed startup
/product-opportunity-analyzer "climate tech" \
  "Context: 2 technical founders, $500K runway, ML expertise, \
   access to carbon credit data"
```

## Workflow

### Phase 1: Opportunity Discovery (10 min)

**Input**: Domain + Context

**Process**:
1. Analyze market trends and pain points
2. Identify underserved segments
3. Generate 10-15 product ideas
4. For each idea, define:
   - One-line description
   - Target customer
   - Core value proposition
   - Why now?

**Output**: Opportunity pool table

```markdown
| # | Product Idea | Target Customer | Value Prop | Why Now |
|---|--------------|-----------------|------------|---------|
| 1 | [Name] | [Who] | [What] | [Timing] |
```

### Phase 2: YC-Style Scoring (15 min)

**Process**:
Uses the `product-analysis` skill to score each idea:

```
Problem Clarity (0-10)
Market Size (0-10)
Solution Fit (0-10)
Unfair Advantage (0-10)
Go-to-Market (0-10)
Business Model (0-10)
Team Fit (0-10)
Timing (0-10)
Traction (0-10)
Vision (0-10)
```

**Output**: Scoring matrix

```markdown
| Product | Problem | Market | Solution | ... | Total | Tier |
|---------|---------|--------|----------|-----|-------|------|
| Idea 1 | 9 | 8 | 9 | ... | 8.5 | S |
| Idea 2 | 8 | 9 | 7 | ... | 8.2 | A |
```

**Tiers**:
- 🏆 S-tier (8.5+): Exceptional, execute immediately
- 🥇 A-tier (8.0-8.4): Strong, high priority
- 🥈 B-tier (7.0-7.9): Solid, needs refinement
- 📋 C-tier (<7.0): Pass or revisit later

### Phase 3: Prioritization (5 min)

**Process**:
Map top ideas to four-quadrant matrix:

```
High Value
│
│  Quick Wins        Strategic Bets
│  (Do First)        (Plan Carefully)
│ ─────────────────────────────────
│  Fill-ins          Money Pits
│  (If Time)         (Avoid)
│
└──────────────────────────────────> High Difficulty
         Low Difficulty
```

**Output**: Prioritized recommendations

### Phase 4: Business Validation (20 min)

**For Top 3 Ideas**, analyze:

**Supply & Demand**:
- Who pays? (Specific persona, not "users")
- How much? (Actual dollar amounts)
- Why buy? (ROI calculation)
- Purchase process? (Decision makers, timeline)

**Business Model**:
- Revenue streams (subscription, transaction, etc.)
- Pricing tiers (Free/Pro/Enterprise)
- Unit economics (LTV, CAC, payback period)
- Path to profitability

**Competitive Moat**:
- Network effects?
- Data advantages?
- Switching costs?
- Regulatory barriers?

**Output**: Business model canvas for each

### Phase 5: Documentation (30 min)

**For Top 1 Idea** (or Top 3 if requested), generate:

Uses the `document-generation` skill to create:

```
[product-name]/
├── 01-product-strategy.md
│   ├── Vision & positioning
│   ├── Competitive analysis
│   ├── Business model
│   └── Success metrics
│
├── 02-prd.md
│   ├── User personas
│   ├── Feature requirements (P0/P1/P2)
│   ├── User stories
│   └── Acceptance criteria
│
├── 03-technical-architecture.md
│   ├── System design
│   ├── Tech stack
│   ├── Data models
│   └── Deployment plan
│
├── 04-gtm-plan.md
│   ├── Target market
│   ├── Marketing strategy
│   ├── Sales process
│   └── Launch plan
│
├── 05-roadmap-12m.md
│   ├── Quarterly milestones
│   ├── Resource plan
│   ├── Budget allocation
│   └── Risk management
│
└── README.md
    └── Executive summary + links
```

### Phase 6: Prototype Generation (Optional, 20 min)

**For Top 1 Idea**, optionally generate an interactive prototype:

Uses the `prototype-generation` skill to create:

**Choose Prototype Type**:
- **Web App**: SaaS dashboard, admin panel, data tool
- **Mobile App**: iOS/Android app flow with device frames
- **Landing Page**: Marketing page for product launch
- **Dashboard**: Data visualization and analytics interface

**Output**:
```
[product-name]-prototype/
├── index.html              # Interactive prototype
├── README.md               # Usage instructions
└── assets/                 # Optional: images, icons
```

**Benefits**:
- ✅ Visualize concepts for stakeholders
- ✅ Test with users before development
- ✅ Use in investor pitches
- ✅ Validate UX assumptions
- ✅ Share via simple HTML file

**When to Generate Prototype**:
- After completing documentation
- When you need visual validation
- For investor/stakeholder presentations
- Before committing to development

## Output Depth Options

### Quick Analysis (30 min)
- Opportunity pool (10-15 ideas)
- YC scoring matrix
- Top 3 recommendations
- Business model summary

### Standard Analysis (90 min)
- Quick analysis content
- **+ Full documentation for Top 1 idea**

### Deep Analysis (3-4 hours)
- Standard analysis content
- **+ Full documentation for Top 3 ideas**
- **+ Interactive prototype for Top 1 idea**
- **+ Comparative analysis**
- **+ Execution priorities**

## Best Practices

### Provide Rich Context

The more context you provide, the better the analysis:

✅ **Good Context**:
```
"Context: Pre-seed startup, 2 technical founders (ML + full-stack),
$500K runway (12 months), expertise in fintech and AI, access to
proprietary trading data from previous company, looking for B2B SaaS
with <$50K CAC, need to reach $1M ARR in 18 months"
```

❌ **Poor Context**:
```
"Context: Startup looking for ideas"
```

### Be Specific About Domain

- ✅ "AI-powered medical imaging for radiology departments"
- ❌ "healthcare"

### Include Constraints

- Budget: "$500K seed round, need to be profitable in 24 months"
- Timeline: "Must launch MVP in 6 months"
- Team: "2 engineers, no sales/marketing experience"
- Regulatory: "Must be HIPAA compliant, FDA clearance required"
- Market: "US-only initially, expand to EU in Year 2"

### State Your Advantages

- "10 years domain expertise in X"
- "Access to proprietary dataset Y"
- "Existing customer base of 1000 users"
- "Partnership with major player Z"
- "Patent pending on technology W"

## Success Metrics

After using this agent, you should have:

- ✅ Clear understanding of opportunity landscape
- ✅ Data-driven prioritization (not gut feel)
- ✅ Validated business model
- ✅ Complete planning documentation
- ✅ Actionable next steps

## Common Use Cases

### 1. Startup Founder - Finding Direction

**Situation**: Technical founder with domain expertise, unsure what to build

**Input**:
```bash
/product-opportunity-analyzer "developer tools" \
  "Context: 10 years as senior engineer at FAANG, expertise in DevOps and CI/CD, \
   frustrated with current tooling, $0 budget, need bootstrappable B2B SaaS"
```

**Output**: 10 ideas → Top 3 scored → Full docs for #1

### 2. Product Manager - Evaluating Features

**Situation**: PM at established company, evaluating new product lines

**Input**:
```bash
/product-opportunity-analyzer "enterprise collaboration" \
  "Context: 100-person SaaS company, $50M ARR, 10K enterprise customers, \
   looking to expand product suite, $2M budget, 12-month timeline"
```

**Output**: Adjacent opportunities → Prioritization → Business cases

### 3. Investor - Due Diligence

**Situation**: VC evaluating startup pitch

**Input**:
```bash
/product-opportunity-analyzer "fintech lending" \
  "Context: Evaluating seed-stage startup, 2 founders (ex-banking + tech), \
   $500K raised, 100 beta users, $50K MRR, seeking $2M seed round"
```

**Output**: Market analysis → Competitive positioning → Risk assessment

### 4. Corporate Innovation - New Ventures

**Situation**: Innovation team at Fortune 500

**Input**:
```bash
/product-opportunity-analyzer "AI for supply chain" \
  "Context: $10B manufacturing company, 50-person innovation team, \
   $10M budget, access to 20 years of supply chain data, \
   need to launch in 6 months, regulatory compliance required"
```

**Output**: Internal vs. external opportunities → Build vs. buy analysis

## Related Commands

- `/market-research [product]` - Deep dive into market sizing
- `/competitive-analysis [product]` - Benchmark against competitors
- `/financial-model [product]` - Build revenue projections
- `/pitch-deck [product]` - Create investor presentation

## Tips

1. **Start Broad, Then Narrow**: Begin with a broader domain, then drill into specific niches
2. **Validate Assumptions**: Use output to identify key assumptions to test with users
3. **Iterate on Scoring**: If scores seem off, provide more context and re-run
4. **Focus on Moats**: Pay special attention to defensibility - it's often the deciding factor
5. **Consider Timing**: A great idea at the wrong time is a bad idea
6. **Talk to Users**: Use this as a starting point, not the final answer

## Limitations

This agent provides analysis and documentation, but cannot:
- ❌ Replace talking to real customers
- ❌ Guarantee product-market fit
- ❌ Execute the plan for you
- ❌ Predict market changes
- ❌ Replace domain expertise

Use this as a structured thinking tool, not a crystal ball.

## Version History

- **1.0.0** (2026-05-08): Initial release
  - YC-style scoring framework
  - Four-quadrant prioritization
  - Complete documentation generation
  - Support for 3 depth levels

## Feedback

Found this useful? Have suggestions? Open an issue or PR!
