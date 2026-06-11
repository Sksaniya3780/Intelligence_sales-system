import plotly.express as px


def sales_bar_chart(df):

    sales = (
        df.groupby("product")
        ["sales_amount"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        sales,
        x="product",
        y="sales_amount",
        title="Sales by Product"
    )

    return fig


def inventory_chart(df):

    fig = px.pie(
        df,
        names="product",
        values="inventory"
    )

    return fig