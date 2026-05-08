---
name: product-analysis
description: Core product opportunity analysis capabilities - YC-style scoring, market validation, and business model design
version: 1.0.0
author: Product Opportunity Skills
---

# Product Analysis Skill

Core analytical capabilities for evaluating product opportunities using YC methodology.

## What This Skill Does

Provides structured frameworks for:
- **YC-Style Scoring**: 10-dimension product evaluation (0-10 scale)
- **Market Validation**: TAM/SAM/SOM analysis, competitive landscape
- **Business Model Design**: Revenue streams, pricing strategy, unit economics
- **Four-Quadrant Analysis**: Value vs. Difficulty mapping

## When to Use

- Evaluating new product ideas
- Assessing market opportunities
- Validating business models
- Prioritizing product initiatives

## Core Frameworks

### 1. YC Product Scoring (10 Dimensions)

```
Problem Clarity (0-10)
- Is the problem well-defined and painful?
- Can you articulate it in one sentence?

Market Size (0-10)
- TAM > $1B? SAM > $100M?
- Growing market vs. shrinking?

Solution Fit (0-10)
- Does the solution directly solve the problem?
- Is it 10x better than alternatives?

Unfair Advantage (0-10)
- What can you do that others can't?
- Network effects? Data moat? Regulatory barriers?

Go-to-Market (0-10)
- Clear customer acquisition channel?
- CAC < LTV/3?

Business Model (0-10)
- Recurring revenue? High margins?
- Path to profitability?

Team Fit (0-10)
- Domain expertise? Technical capability?
- Founder-market fit?

Timing (0-10)
- Why now? Market tailwinds?
- Too early or too late?

Traction (0-10)
- Revenue? User growth? Engagement?
- Proof of product-market fit?

Vision (0-10)
- Billion-dollar outcome possible?
- Clear path to scale?
```

**Scoring Guide**:
- 8.5+: Exceptional, top 1% opportunity
- 7.5-8.4: Strong, worth pursuing
- 6.5-7.4: Decent, needs refinement
- <6.5: Weak, reconsider or pivot

### 2. Four-Quadrant Analysis

```
High Value, Low Difficulty → Quick Wins (do first)
High Value, High Difficulty → Strategic Bets (plan carefully)
Low Value, Low Difficulty → Fill-ins (do if time permits)
Low Value, High Difficulty → Money Pits (avoid)
```

### 3. Business Model Canvas

```
Value Proposition
- What problem are you solving?
- What's your unique solution?

Customer Segments
- Who are your target users?
- Personas and use cases?

Revenue Streams
- How do you make money?
- Pricing tiers and models?

Cost Structure
- Fixed vs. variable costs?
- Unit economics?

Key Metrics
- North Star Metric?
- Leading indicators?
```

## Output Format

When analyzing a product opportunity, structure your response as:

```markdown
# [Product Name] - Opportunity Analysis

## Executive Summary
[2-3 sentence overview]

## YC Score: X.X/10.0
[Brief justification]

## Detailed Scoring
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Problem Clarity | X/10 | ... |
| Market Size | X/10 | ... |
...

## Four-Quadrant Position
[High Value, Low Difficulty] - Quick Win

## Business Model
- Revenue: [model]
- Pricing: [strategy]
- Unit Economics: [LTV/CAC ratio]

## Key Risks
1. [Risk 1]
2. [Risk 2]

## Recommendation
[Go/No-Go with reasoning]
```

## Best Practices

1. **Be Objective**: Score based on evidence, not enthusiasm
2. **Compare Alternatives**: Benchmark against similar products
3. **Validate Assumptions**: Call out what needs to be tested
4. **Think Long-term**: Consider 3-5 year trajectory
5. **Consider Execution**: Great idea + poor execution = failure

## Related Skills

- `market-research` - Deep market analysis
- `competitive-analysis` - Competitor benchmarking
- `financial-modeling` - Revenue projections
- `user-research` - Customer validation

## Examples

See `/examples/saas-product-analysis/` for a complete walkthrough.
