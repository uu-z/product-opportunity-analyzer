---
name: document-generation
description: Generate standardized product planning documents - PRD, technical specs, GTM plans, and roadmaps
version: 1.0.0
author: Product Opportunity Skills
---

# Document Generation Skill

Automated generation of professional product planning documents following industry best practices.

## What This Skill Does

Generates five core document types:
1. **Product Strategy** - Vision, positioning, competitive analysis
2. **PRD (Product Requirements Document)** - Features, user stories, acceptance criteria
3. **Technical Architecture** - System design, tech stack, deployment
4. **Go-to-Market Plan** - Marketing, sales, distribution strategy
5. **12-Month Roadmap** - Milestones, resources, risk management

## When to Use

- After completing product opportunity analysis
- When you need standardized planning documents
- For investor presentations and pitches
- Internal strategic planning
- Product launch preparation

## Document Templates

### 1. Product Strategy Document

```markdown
# [Product Name] - Product Strategy

## Vision & Mission
**Vision**: [Aspirational future state]
**Mission**: [What you do and for whom]

## Market Opportunity
- **TAM**: $X billion
- **SAM**: $X million
- **SOM (Year 1)**: $X million

## Target Customer
### Primary Persona
- **Who**: [Role/demographic]
- **Pain Point**: [Core problem]
- **Current Solution**: [What they use today]
- **Why Switch**: [Your advantage]

## Competitive Landscape
| Competitor | Strength | Weakness | Our Advantage |
|------------|----------|----------|---------------|
| [Name] | ... | ... | ... |

## Business Model
- **Revenue Model**: [Subscription/Transaction/Freemium]
- **Pricing**: [Tiers and prices]
- **Unit Economics**: LTV $X, CAC $Y, Ratio X:1

## Success Metrics
- **North Star**: [Primary metric]
- **Year 1 Goals**: [Specific targets]

## Strategic Risks
1. [Risk] - Mitigation: [Strategy]
```

### 2. PRD Template

```markdown
# [Feature Name] - Product Requirements Document

## Overview
**Problem**: [What problem does this solve?]
**Solution**: [High-level approach]
**Success Criteria**: [How do we measure success?]

## User Stories
### P0 (Must-Have)
- As a [user type], I want to [action] so that [benefit]

### P1 (Should-Have)
- ...

### P2 (Nice-to-Have)
- ...

## Functional Requirements
### Core Features
1. **[Feature Name]**
   - Description: [What it does]
   - Acceptance Criteria:
     - [ ] [Testable criterion]
     - [ ] [Testable criterion]

## Non-Functional Requirements
- **Performance**: [Response time, throughput]
- **Security**: [Authentication, authorization]
- **Scalability**: [Expected load]

## User Flow
```
[User Journey Diagram]
```

## Design Mockups
[Link to Figma/wireframes]

## Technical Considerations
- **Dependencies**: [External services, APIs]
- **Data Model**: [Key entities]
- **Edge Cases**: [Error scenarios]

## Launch Plan
- **Alpha**: [Internal testing, date]
- **Beta**: [Limited release, date]
- **GA**: [General availability, date]
```

### 3. Technical Architecture Template

```markdown
# [Product Name] - Technical Architecture

## System Overview
[High-level architecture diagram]

## Tech Stack
### Frontend
- **Framework**: [React/Vue/Next.js]
- **State Management**: [Redux/Zustand]
- **UI Library**: [Tailwind/MUI]

### Backend
- **Runtime**: [Node.js/Python/Go]
- **Framework**: [Express/FastAPI/Gin]
- **Database**: [PostgreSQL/MongoDB]

### Infrastructure
- **Hosting**: [Vercel/AWS/GCP]
- **CDN**: [Cloudflare]
- **Monitoring**: [Datadog/Sentry]

## Core Services
### Service 1: [Name]
- **Purpose**: [What it does]
- **API Endpoints**:
  - `GET /api/v1/[resource]`
  - `POST /api/v1/[resource]`
- **Data Model**: [Schema]

## Data Flow
```
User → Frontend → API Gateway → Service → Database
```

## Security
- **Authentication**: [JWT/OAuth2]
- **Authorization**: [RBAC model]
- **Data Encryption**: [At rest, in transit]

## Scalability
- **Horizontal Scaling**: [Load balancing strategy]
- **Caching**: [Redis/CDN]
- **Database**: [Read replicas, sharding]

## Deployment
- **CI/CD**: [GitHub Actions/CircleCI]
- **Environments**: Dev → Staging → Production
- **Rollback Strategy**: [Blue-green/Canary]
```

### 4. Go-to-Market Plan Template

```markdown
# [Product Name] - Go-to-Market Plan

## Target Market
- **ICP (Ideal Customer Profile)**: [Description]
- **Market Size**: [TAM/SAM/SOM]
- **Beachhead Market**: [Initial focus]

## Positioning
- **Category**: [How you're categorized]
- **Tagline**: [One-line pitch]
- **Key Differentiators**: [3 unique advantages]

## Marketing Strategy
### Content Marketing
- **Blog**: [Topics, frequency]
- **SEO**: [Target keywords]
- **Social**: [Platforms, strategy]

### Paid Acquisition
- **Channels**: [Google Ads, LinkedIn, etc.]
- **Budget**: $X/month
- **Target CAC**: $Y

### Partnerships
- **Integration Partners**: [Complementary products]
- **Referral Program**: [Incentive structure]

## Sales Strategy
### Sales Motion
- **Model**: [Self-serve/Sales-led/Hybrid]
- **Sales Cycle**: [X days/weeks]
- **ACV**: $X

### Sales Process
1. **Lead Generation**: [Sources]
2. **Qualification**: [BANT criteria]
3. **Demo**: [Key talking points]
4. **Negotiation**: [Common objections]
5. **Close**: [Contract terms]

## Launch Plan
### Pre-Launch (Weeks -4 to 0)
- [ ] Beta user recruitment
- [ ] Press kit preparation
- [ ] Landing page optimization

### Launch Week
- [ ] Product Hunt launch
- [ ] Press release distribution
- [ ] Social media campaign

### Post-Launch (Weeks 1-4)
- [ ] User feedback collection
- [ ] Iteration based on data
- [ ] Case study development

## Metrics
- **Acquisition**: [Traffic, signups]
- **Activation**: [Onboarding completion]
- **Revenue**: [MRR, ARR]
- **Retention**: [Churn rate]
```

### 5. 12-Month Roadmap Template

```markdown
# [Product Name] - 12-Month Roadmap

## Quarterly Themes
- **Q1**: [Focus area]
- **Q2**: [Focus area]
- **Q3**: [Focus area]
- **Q4**: [Focus area]

## Month-by-Month Milestones

### Month 1-3: Foundation
**Goals**: MVP launch, initial traction
- Week 1-2: [Milestone]
- Week 3-4: [Milestone]
- ...

**Key Metrics**:
- Users: [Target]
- Revenue: [Target]

**Resources**:
- Team: [Headcount]
- Budget: $X

### Month 4-6: Growth
**Goals**: Product-market fit validation
- [Milestones]

### Month 7-9: Scale
**Goals**: Expand market reach
- [Milestones]

### Month 10-12: Optimize
**Goals**: Profitability path
- [Milestones]

## Risk Management
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| [Risk 1] | High | High | [Strategy] |

## Resource Plan
| Role | Q1 | Q2 | Q3 | Q4 |
|------|----|----|----|----|
| Engineering | 2 | 3 | 4 | 5 |
| Product | 1 | 1 | 2 | 2 |
| Marketing | 1 | 2 | 2 | 3 |

## Budget Allocation
- **Engineering**: 50%
- **Marketing**: 30%
- **Operations**: 20%
```

## Output Structure

When generating documents, create this folder structure:

```
[product-name]/
├── 01-product-strategy.md
├── 02-prd.md
├── 03-technical-architecture.md
├── 04-gtm-plan.md
├── 05-roadmap-12m.md
└── README.md (summary + links)
```

## Best Practices

1. **Be Specific**: Use real numbers, not placeholders
2. **Stay Consistent**: Cross-reference between documents
3. **Make Actionable**: Include clear next steps
4. **Version Control**: Date all documents
5. **Iterate**: Update as you learn

## Related Skills

- `product-analysis` - Opportunity evaluation
- `market-research` - Market sizing
- `financial-modeling` - Revenue projections

## Examples

See `/examples/saas-product-docs/` for complete document sets.
