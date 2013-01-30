from matplotlib.pyplot import *

def plot_summary(num_balls, means, stds, game_name):
    figure(figsize=(15,5))
    subplot(121)
    plot(num_balls, means,'ro')
    xlabel("# balls each color")
    ylabel("avg. # draws")
    title(game_name + " - average")
    subplot(122)
    plot(num_balls, stds,'bo')
    xlabel("# balls each color")
    ylabel("# draws")
    title(game_name + " standard deviation")

def plot_histograms(results, num_balls, n_bins = 25, legend_title= "# balls each", game_name=''):
    figure(figsize=(18,5))
    title(game_name + " # draws histogram")
    subplot(131)
    for i,dataset in enumerate(results[0:3,]):
        hist(dataset, bins=n_bins, label=str(num_balls[i]))
    legend(title=legend_title)
    xlabel("# draws")
    ylabel("frequency")
    subplot(132)
    for i,dataset in enumerate(results[3:6,]):
        hist(dataset, bins=n_bins, label=str(num_balls[i+3]))
    legend(title=legend_title)
    xlabel("# draws")
    subplot(133)
    for i,dataset in enumerate(results[6:,]):
        hist(dataset, bins=n_bins, label=str(num_balls[i+6]))
    legend(title=legend_title)
    xlabel("# draws")

def plot_mutation_load(time_series, mu, s, plot_title):
    figure(figsize=(10,6))
    plot(range(len(time_series)), time_series, 'k')
    axhline(y=mu/s)
    xlabel("generations")
    ylabel("mutation load")
    title(plot_title)