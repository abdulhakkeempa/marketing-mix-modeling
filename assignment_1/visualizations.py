import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from config import COLORS


def create_performance_trends_chart(combined_df):    
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Revenue Trend', 'Marketing Efficiency', 'Order Volume', 'Customer Acquisition'),
        specs=[[{"secondary_y": True}, {"secondary_y": True}], [{"secondary_y": False}, {"secondary_y": False}]]
    )
    
    fig.add_trace(
        go.Scatter(x=combined_df['date'], y=combined_df['total_revenue'], 
                  name='Revenue', line=dict(color=COLORS['revenue'])), 
        row=1, col=1
    )
    fig.add_trace(
        go.Scatter(x=combined_df['date'], y=combined_df['spend'], 
                  name='Marketing Spend', line=dict(color=COLORS['spend'])), 
        row=1, col=1, secondary_y=True
    )
    
    fig.add_trace(
        go.Scatter(x=combined_df['date'], y=combined_df['marketing_roas'], 
                  name='ROAS', line=dict(color=COLORS['roas'])),
        row=1, col=2
    )
    
    fig.add_trace(
        go.Scatter(x=combined_df['date'], y=combined_df['no_of_orders'], 
                  name='Total Orders', line=dict(color=COLORS['orders'])),
        row=2, col=1
    )
    fig.add_trace(
        go.Scatter(x=combined_df['date'], y=combined_df['no_of_new_orders'], 
                  name='New Orders', line=dict(color=COLORS['new_orders'])),
        row=2, col=1
    )
    
    fig.add_trace(
        go.Scatter(x=combined_df['date'], y=combined_df['new_customers'], 
                  name='New Customers', line=dict(color=COLORS['customers'])),
        row=2, col=2
    )
    
    fig.update_layout(height=600, showlegend=True, title_text="Business Performance Dashboard")
    return fig


def create_channel_roas_chart(channel_performance):    
    fig = px.bar(
        channel_performance, 
        x='channel', 
        y='roas',
        title='Return on Ad Spend by Channel',
        color='roas',
        color_continuous_scale='Viridis'
    )
    fig.update_layout(showlegend=False)
    return fig


def create_spend_allocation_chart(channel_performance):    
    fig = px.pie(
        channel_performance, 
        values='spend', 
        names='channel',
        title='Marketing Spend Allocation'
    )
    return fig


def create_margin_trend_chart(combined_df):    
    fig = px.line(
        combined_df, 
        x='date', 
        y='gross_margin',
        title='Gross Margin Trend',
        labels={'gross_margin': 'Gross Margin (%)', 'date': 'Date'}
    )
    fig.update_traces(line_color=COLORS['revenue'])
    return fig


def create_cost_breakdown_chart(metrics, combined_df):    
    costs_data = {
        'Category': ['Revenue', 'COGS', 'Marketing Spend', 'Gross Profit'],
        'Amount': [
            metrics['total_revenue'],
            combined_df['COGS'].sum(),
            metrics['total_spend'],
            combined_df['gross_profit'].sum()
        ],
        'Type': ['Income', 'Cost', 'Cost', 'Income']
    }
    
    fig = px.bar(
        costs_data, 
        x='Category', 
        y='Amount',
        color='Type',
        title='Revenue & Cost Breakdown',
        color_discrete_map={'Income': COLORS['income'], 'Cost': COLORS['cost']}
    )
    return fig


def create_efficiency_scatter_chart(combined_df):    
    daily_efficiency = combined_df[combined_df['spend'] > 0].copy()
    
    fig = px.scatter(
        daily_efficiency,
        x='spend',
        y='attributed_revenue',
        size='no_of_orders',
        color='marketing_roas',
        title='Marketing Spend vs Attributed Revenue',
        labels={
            'spend': 'Daily Marketing Spend ($)',
            'attributed_revenue': 'Daily Attributed Revenue ($)',
            'marketing_roas': 'ROAS'
        },
        color_continuous_scale='Viridis'
    )
    
    max_spend = daily_efficiency['spend'].max()
    fig.add_trace(
        go.Scatter(
            x=[0, max_spend],
            y=[0, max_spend],
            mode='lines',
            name='Break-even (1x ROAS)',
            line=dict(dash='dash', color='red')
        )
    )
    
    return fig


def create_tactic_performance_chart(tactic_performance):
    fig = px.scatter(
        tactic_performance,
        x='spend',
        y='roas',
        color='channel',
        size='clicks',
        hover_data=['tactic', 'ctr'],
        title='Tactic Performance: Spend vs ROAS',
        labels={'spend': 'Total Spend ($)', 'roas': 'ROAS'}
    )
    
    return fig
