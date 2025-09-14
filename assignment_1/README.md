# E-commerce Marketing Analytics Dashboard

A Streamlit dashboard that transforms raw e-commerce business and marketing data into actionable insights for decision-makers.

### My Solution Approach
1. **Join & aggregate** datasets by date for unified view
2. **Derive meaningful metrics** from raw data columns
3. **Focus on business impact** rather than technical metrics
4. **Provide tactical recommendations** based on data patterns

## Setup & Usage

### Run Dashboard
```bash
cd assignment_1
pip install -r requirements.txt
streamlit run main.py
```

## Key Derivations & Metrics

### From Raw Data to Strategic Metrics

| **Raw Columns** | **Derived Metric** | **Business Value** |
|---|---|---|
| `attributed_revenue ÷ spend` | **ROAS** | Channel efficiency & budget allocation |
| `clicks ÷ impressions` | **CTR** | Creative performance & audience targeting |
| `spend ÷ clicks` | **CPC** | Cost efficiency by channel |
| `total_revenue ÷ no_of_orders` | **AOV** | Customer value optimization |
| `gross_profit ÷ total_revenue` | **Gross Margin** | Profitability trends |
| `new_customers ÷ no_of_orders` | **New Customer Rate** | Acquisition efficiency |

### Cross-Dataset Integration
- **Business + Marketing Join**: Daily performance unified view
- **Channel Aggregation**: Multi-platform marketing performance
- **Time-based Analysis**: Trend identification and growth metrics

## 📈 Dashboard Structure & Relevance

### 1. Executive Summary
**Relevance**: C-level needs high-level business health at a glance
- **Metrics**: Total Revenue, Marketing ROAS, AOV, Gross Margin
- **Value**: Quick decision support for budget and strategy

### 2. Performance Trends
**Relevance**: Identify patterns between marketing activity and business results
- **Visualization**: Multi-panel time series (Revenue vs Spend, Orders, Customer Acquisition)
- **Insight**: Marketing impact correlation with business performance

### 3. Channel Analysis
**Relevance**: Optimize marketing budget allocation across platforms
- **Key Views**: ROAS by channel, spend allocation, performance comparison
- **Action**: Identify best-performing channels for budget reallocation

### 4. Profitability Analysis
**Relevance**: Understand true marketing ROI beyond just revenue
- **Analysis**: Gross margin trends, marketing efficiency scatter plots
- **Decision Support**: ROI optimization and cost management

### 5. Campaign Details
**Relevance**: Tactical campaign management and optimization
- **Features**: Top/bottom performers, tactic-level analysis
- **Actionable**: Immediate campaign pause/scale decisions


