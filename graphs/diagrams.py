import matplotlib.pyplot as plt
import seaborn as sns


def plot_bar(df, column):
    plt.figure(figsize = (5,4))
    sns.set_palette('dark')
    sns.set_style('darkgrid')
    unique = df[column].value_counts()
    plt.barh(unique.index , width = 0.2)
    plt.title(f'barchart for {column}', size = 18, color = 'orange')
    plt.xlabel(f"{column}", size = 15, color = 'brown')
    plt.ylabel('frequency', size = 15, color = 'brown')
    plt.xticks(rotation = 45)
    plt.show()



# pie chart for the nominal categorical columns
def plot_pie(df, column):
        plt.figure(figsize = (5,4))
        top_10 = df['column'].value_counts().nlargest(10)
        top_10.plot.pie(autopct='%1.1f%%', startangle=90)
        plt.title('Pie Chart', size = 20, color = 'brown')


# histogram for the numerical continuous columns
def plot_hist(df, column):
    plt.figure(figsize = (5,4))
    sns.set_style('dark')
    sns.set_palette('dark')
    unique = df[column].value_counts()
    sns.histplot(unique,bins = 20, kde = True)
    plt.title(f'histogram for {column}', size = 18, color = 'orange')
    plt.xlabel(f"{column}", size = 15, color = 'brown')
    plt.ylabel('frequency', size = 15, color = 'brown')
    plt.xticks(rotation = 45)
    plt.show()


# density plot for the numerical discrete columns
def plot_kde(df, column):
    plt.figure(figsize = (5,4))
    sns.set_style('dark')
    sns.set_palette('dark')
    sns.kdeplot(df[column], color = 'k')
    plt.title(f'kde plot  for {column}', size = 18, color = 'orange')
    plt.xlabel(f"{column}", size = 15, color = 'brown')
    plt.ylabel('frequency', size = 15, color = 'brown')
    plt.xticks(rotation = 45)
    plt.show()