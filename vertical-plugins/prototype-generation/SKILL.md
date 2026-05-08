---
name: prototype-generation
description: Generate interactive HTML prototypes for product concepts - web apps, mobile apps, dashboards, and landing pages
version: 1.0.0
author: Product Opportunity Skills
---

# Prototype Generation Skill

Rapidly create interactive HTML prototypes to visualize product concepts and validate ideas with stakeholders.

## What This Skill Does

Generates production-quality HTML prototypes in 4 categories:
1. **Web App Prototype** - SaaS dashboards, admin panels, data tools
2. **Mobile App Prototype** - iOS/Android app flows with device frames
3. **Landing Page** - Marketing pages for product launches
4. **Dashboard** - Data visualization and analytics interfaces

## When to Use

- After completing product strategy and PRD
- When you need to visualize concepts for stakeholders
- Before investing in full development
- For user testing and feedback collection
- During investor pitches and demos

## Prototype Types

### 1. Web App Prototype

**Best For**: SaaS products, internal tools, B2B platforms

**Features**:
- Responsive layout (desktop/tablet/mobile)
- Interactive navigation
- Form inputs and buttons
- Modal dialogs and dropdowns
- Realistic data placeholders

**Example Use Cases**:
- Project management tool
- CRM dashboard
- Analytics platform
- Admin panel

**Output**: Single-page HTML with embedded CSS/JS

### 2. Mobile App Prototype

**Best For**: Consumer apps, mobile-first products

**Features**:
- Device frames (iPhone 15 Pro, Pixel 8)
- Multi-screen flows (3-5 screens)
- Touch interactions
- Bottom navigation
- Native-like UI components

**Example Use Cases**:
- Social media app
- E-commerce app
- Fitness tracker
- Food delivery app

**Output**: HTML with device frame + screen transitions

### 3. Landing Page

**Best For**: Product launches, marketing campaigns

**Features**:
- Hero section with CTA
- Feature highlights
- Social proof (testimonials, logos)
- Pricing table
- FAQ section
- Footer with links

**Example Use Cases**:
- SaaS product launch
- Mobile app pre-launch
- Event registration
- Lead generation

**Output**: Full-page marketing site

### 4. Dashboard

**Best For**: Data-heavy products, analytics tools

**Features**:
- Chart visualizations (Chart.js)
- KPI cards
- Data tables
- Filters and date pickers
- Export buttons

**Example Use Cases**:
- Business intelligence tool
- Marketing analytics
- Financial dashboard
- Operations monitoring

**Output**: Interactive dashboard with mock data

## Design Systems

Choose from pre-configured design systems:

### Modern Minimal
- Clean, spacious layouts
- Sans-serif typography (Inter, SF Pro)
- Neutral color palette
- Subtle shadows and borders

### Bold & Vibrant
- High-contrast colors
- Gradient accents
- Large typography
- Energetic feel

### Professional Corporate
- Conservative color scheme
- Structured layouts
- Traditional typography
- Trust-focused design

### Startup Playful
- Rounded corners
- Bright accent colors
- Friendly illustrations
- Casual tone

## Generation Process

### Step 1: Requirements Gathering

Ask the user:
1. **Prototype Type**: Web app / Mobile app / Landing page / Dashboard
2. **Product Name**: What's the product called?
3. **Core Features**: What are the 3-5 key features to showcase?
4. **Target Audience**: Who is this for?
5. **Design System**: Which style? (Modern Minimal / Bold & Vibrant / Professional / Playful)
6. **Brand Colors** (optional): Primary and accent colors

### Step 2: Structure Planning

Based on prototype type, plan the structure:

**Web App**:
```
- Header (logo, navigation, user menu)
- Sidebar (main navigation)
- Main content area (feature showcase)
- Footer
```

**Mobile App**:
```
- Screen 1: Onboarding/Welcome
- Screen 2: Main feature
- Screen 3: Secondary feature
- Screen 4: Profile/Settings
- Bottom navigation
```

**Landing Page**:
```
- Hero section (headline, subheadline, CTA)
- Features (3-4 key features)
- Social proof (testimonials, logos)
- Pricing (3 tiers)
- FAQ (5-7 questions)
- Footer
```

**Dashboard**:
```
- Top bar (filters, date range, export)
- KPI cards (4-6 metrics)
- Charts (2-3 visualizations)
- Data table
```

### Step 3: Content Generation

Create realistic content:
- **Headlines**: Clear, benefit-focused
- **Body Copy**: Concise, action-oriented
- **CTAs**: Specific, compelling
- **Data**: Realistic numbers and trends
- **Images**: Placeholder images with proper dimensions

### Step 4: Code Generation

Generate clean, semantic HTML:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[Product Name]</title>
    <style>
        /* Design system variables */
        :root {
            --primary: #3b82f6;
            --secondary: #8b5cf6;
            --background: #ffffff;
            --text: #1f2937;
            --border: #e5e7eb;
        }

        /* Reset and base styles */
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; }

        /* Component styles */
        /* ... */
    </style>
</head>
<body>
    <!-- Prototype content -->

    <script>
        // Interactive behaviors
    </script>
</body>
</html>
```

### Step 5: Enhancement

Add interactivity:
- Click handlers for buttons
- Form validation
- Modal open/close
- Tab switching
- Dropdown menus
- Smooth scrolling

## Output Structure

```
[product-name]-prototype/
├── index.html              # Main prototype file
├── README.md               # Usage instructions
└── assets/                 # Optional: images, icons
    ├── logo.svg
    └── screenshots/
```

## Best Practices

### Design
1. **Mobile-First**: Start with mobile layout, scale up
2. **Accessibility**: Use semantic HTML, ARIA labels, keyboard navigation
3. **Performance**: Inline critical CSS, minimize JS
4. **Consistency**: Use design tokens (CSS variables)
5. **Whitespace**: Don't cram too much content

### Content
1. **Real Copy**: Avoid "Lorem ipsum", use realistic text
2. **Specific Numbers**: "$99/month" not "$XX/month"
3. **Clear CTAs**: "Start Free Trial" not "Click Here"
4. **Benefit-Focused**: "Save 10 hours/week" not "Feature X"
5. **Social Proof**: Include realistic testimonials

### Technical
1. **Single File**: Keep everything in one HTML file for easy sharing
2. **No Dependencies**: Avoid external libraries when possible
3. **Responsive**: Test on mobile, tablet, desktop
4. **Browser Support**: Modern browsers (Chrome, Safari, Firefox)
5. **Comments**: Document sections clearly

## Integration with Product Analysis

Use this skill after completing:
1. ✅ Product Strategy (know the vision)
2. ✅ PRD (know the features)
3. ✅ Technical Architecture (know the tech stack)

The prototype should reflect:
- **Strategy**: Brand positioning and value prop
- **PRD**: P0 features prominently displayed
- **Architecture**: Realistic data structures

## Example Workflow

```bash
# After generating product docs
/prototype-generation

# Interactive prompts:
> Prototype type: Web App
> Product name: TaskFlow
> Core features: Task management, Team collaboration, Time tracking
> Target audience: Remote teams
> Design system: Modern Minimal
> Brand colors: #3b82f6 (primary), #8b5cf6 (accent)

# Output: taskflow-prototype/index.html
```

## Advanced Features

### Multi-Page Prototypes

For complex products, generate multiple pages:

```
prototype/
├── index.html          # Landing page
├── dashboard.html      # Main app interface
├── settings.html       # Settings page
└── pricing.html        # Pricing page
```

### Interactive States

Show different states:
- Empty state (no data yet)
- Loading state (skeleton screens)
- Error state (error messages)
- Success state (confirmation)

### Data Visualization

For dashboards, include:
- Line charts (trends over time)
- Bar charts (comparisons)
- Pie charts (distributions)
- Tables (detailed data)

Use Chart.js or inline SVG for charts.

### Device Frames

For mobile prototypes, wrap in device frame:

```html
<div class="device-frame iphone-15-pro">
    <div class="screen">
        <!-- App content -->
    </div>
</div>
```

## Limitations

This skill generates static HTML prototypes, not production code:
- ❌ No backend integration
- ❌ No real data persistence
- ❌ No authentication
- ❌ No API calls
- ✅ Visual design and UX flow
- ✅ Interactive elements (click, hover)
- ✅ Responsive layout
- ✅ Realistic content

## Related Skills

- `product-analysis` - Validate opportunity before prototyping
- `document-generation` - Generate specs before building prototype
- `user-testing` - Test prototype with real users
- `design-system` - Create comprehensive design system

## Examples

See `/examples/prototypes/` for:
- `saas-dashboard.html` - B2B SaaS product
- `mobile-app.html` - Consumer mobile app
- `landing-page.html` - Product launch page
- `analytics-dashboard.html` - Data visualization

## Tips

1. **Start Simple**: Don't try to prototype every feature
2. **Focus on Core Flow**: Show the main user journey
3. **Use Real Content**: Makes it more convincing
4. **Test on Devices**: View on actual phones/tablets
5. **Iterate Quickly**: Prototypes are meant to be disposable
6. **Get Feedback Early**: Share with users ASAP

## Version History

- **1.0.0** (2026-05-08): Initial release
  - 4 prototype types
  - 4 design systems
  - Interactive components
  - Responsive layouts
