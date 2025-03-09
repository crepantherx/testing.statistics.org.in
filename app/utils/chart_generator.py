import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
from typing import List, Dict


def generate_charts(df: pd.DataFrame, container_width: int = 1200) -> Dict[str, List[str]]:

    charts = {
        "numerical_columns": [],
        "categorical_columns": [],
        "any_columns": []
    }

    # Calculate 33% of container width in pixels
    chart_width_pixels = int(container_width * 0.33)  # 4/12 = 33%

    # Convert pixels to inches (assuming 96 DPI, common for web displays)
    dpi = 96
    chart_width_inches = chart_width_pixels / dpi
    chart_height_inches = chart_width_inches * 0.75  # Maintain a 4:3 aspect ratio (adjustable)

    # Determine column types
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    all_cols = df.columns

    # Helper function to convert Matplotlib figure to base64 HTML img tag
    def fig_to_html(fig):
        buf = io.BytesIO()
        fig.savefig(buf, format='png', bbox_inches='tight', dpi=dpi)
        buf.seek(0)
        img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
        buf.close()
        plt.close(fig)  # Close the figure to free memory
        return f'<img src="data:image/png;base64,{img_base64}" />'

    # Generate charts for numerical columns
    for col in numerical_cols:
        if len(df) > 1:  # Ensure enough data points
            # Bar Chart
            fig, ax = plt.subplots(figsize=(chart_width_inches, chart_height_inches))
            ax.boxplot(df[col].dropna(), vert=True, patch_artist=True, labels=[col])  # Use boxplot instead of bar
            # ax.set_title(f'Box Plot for {col}')
            ax.set_ylabel(col)  # No x-label needed for a single box plot, use y-label for the variable
            ax.legend([col], loc='best')  # Adjust legend to work with boxplot
            charts["numerical_columns"].append(fig_to_html(fig))

    # Generate charts for categorical columns
    for col in categorical_cols:
        if len(df[col].unique()) > 1:  # Ensure some variety
            # Bar Chart (count of categories)
            value_counts = df[col].value_counts()
            fig, ax = plt.subplots(figsize=(chart_width_inches, chart_height_inches))
            ax.bar(value_counts.index, value_counts, label=f'Bar - {col}')
            # ax.set_title(f'Bar Chart for {col}')
            ax.set_xlabel(col)
            ax.set_ylabel('Count')
            ax.legend()
            plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
            charts["categorical_columns"].append(fig_to_html(fig))

    # Generate charts for any columns (e.g., mixed or additional visualization)
    for col in all_cols:
        if len(df) > 1:  # Ensure enough data points
            # Scatter Plot
            fig, ax = plt.subplots(figsize=(chart_width_inches, chart_height_inches))
            ax.scatter(df.index, df[col], label=f'Scatter - {col}')
            # ax.set_title(f'Scatter Plot for {col}')
            # ax.set_xlabel('Index')
            ax.set_ylabel(col)
            ax.legend()
            charts["any_columns"].append(fig_to_html(fig))

    return charts