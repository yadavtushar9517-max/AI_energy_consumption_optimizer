import plotly.express as px

def energy_vs_hour(df):
    fig = px.line(
        df,
        x="hour",
        y="energy_consumption",
        markers=True,
        title="Energy Consumption vs Hour"
    )
    return fig

def temperature_energy(df):
    fig = px.scatter(
        df,
        x="temperature",
        y="energy_consumption",
        color="occupancy",
        title="Temperature vs Energy Consumption"
    )
    return fig

def energy_distribution(df):
    fig = px.histogram(
        df,
        x="energy_consumption",
        nbins=20,
        title="Energy Consumption Distribution"
    )
    return fig