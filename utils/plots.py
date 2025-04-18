import matplotlib.pyplot as plt
import seaborn as sns

def plot_predictions(predictions):
    # Extract job titles and scores from the predictions
    jobs, scores = zip(*predictions)
    
    # Set up the plot with Seaborn for better style and color scheme
    sns.set(style="whitegrid", palette="coolwarm")
    
    # Create a figure and axis for the plot with a larger size
    fig, ax = plt.subplots(figsize=(12, 7))  # Adjust the size to fit larger screens if needed
    
    # Create a horizontal bar chart with color gradient based on scores
    bars = ax.barh(jobs, scores, color=sns.color_palette("coolwarm", len(scores)))  # Gradient color based on scores

    # Labeling the axes and the title with custom styles
    ax.set_xlabel('Match Percentage', fontsize=14, fontweight='bold')  # Custom font size and weight for labels
    ax.set_title('Top Career Matches', fontsize=16, fontweight='bold', color='darkblue')  # Title with different style
    ax.set_xlim(0, 100)  # Set the x-axis limit to 100 for clarity of percentage values

    # Add tooltips (text on bars showing match percentage)
    for bar in bars:
        width = bar.get_width()
        ax.text(width + 1, bar.get_y() + bar.get_height() / 2,
                f'{width}%', va='center', ha='left', fontsize=12, color='black', fontweight='bold')

    # Add gridlines for clarity
    ax.grid(axis='x', linestyle='--', alpha=0.7)

    # Customize tick label sizes for better readability
    ax.tick_params(axis='y', labelsize=12)
    ax.tick_params(axis='x', labelsize=12)

    # Tight layout for better spacing and visualization
    plt.tight_layout()
    
    # Return the figure for embedding in the Streamlit app or saving
    return fig
