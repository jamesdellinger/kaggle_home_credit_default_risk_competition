#Visualization module for Udacity Machine Learning Engineer
# Nanodegree Capstone Project

# Suppress matplotlib user warnings
# Necessary for newer version of matplotlib
import warnings
warnings.filterwarnings("ignore", category = UserWarning, module = "matplotlib")

# Import libraries necessary for this file.
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# Display inline matplotlib plots with IPython
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')
# Set dpi of plots displayed inline
mpl.rcParams['figure.dpi'] = 100
# Configure style of plots
plt.style.use('fivethirtyeight')
# Make plots smaller
sns.set_context('paper')

# For plotting ROC curves of classifiers
from sklearn.metrics import roc_curve, roc_auc_score, auc

def plot_feature_distributions(data, title, figsize, num_cols):
    """
    Plot distributions of a dataset's continuous features as histograms.

    Parameters:
        data: Pandas dataframe containing the features
        title: String, title of the figure
        figsize: Tuple, the dimensions in inches of the
                 figure that gets plotted.
        num_cols: Int, number of columns desired for the
                  figure
    """
    # Get list of dataframe's column names (the features)
    column_names = list(data.columns.values)

    # Get the number of features that will be plotted
    number_of_features = len(column_names)

    # Create a figure with 4 columns
    num_cols = num_cols

    # Ensure that there will be enough rows to
    # display each plot
    num_rows = int(np.ceil(number_of_features*1./num_cols))

    # Create the figure
    fig = plt.figure(dpi=300, figsize = figsize)

    # Plot the distribution of each feature
    for i, feature in enumerate(column_names):
        # Filter the feature's data for NaN values
        feature_data = data[feature]
        filtered_feature_data = feature_data[~np.isnan(feature_data)]
        # Add a new subplot for each feature, filling out a
        # grid that is num_rows x num_cols in dimensions.
        # Subplot index begins at 1.
        ax = fig.add_subplot(num_rows, num_cols, i+1)
        ax.hist(filtered_feature_data, bins = 25)
        ax.set_title("'%s' Distribution"%(feature), fontsize = 12)
        ax.set_xlabel("Value")
        ax.set_ylabel("Number of Borrowers")

    # Plot aesthetics
    fig.suptitle(title, fontsize = 16, y = 1.03)

    # Display the plot
    fig.tight_layout()
    fig.show()

    # Save the plot to a png file
    fig.savefig('{}.png'.format(title))

def plot_roc_curves(y_test, y_score_list, clf_label_list, title):
    """
    Plots ROC curves of a various classifiers' prediction probabilities.
    Also plots the mean ROC curve of all classifiers' curves.

    Parameters:
        y_test: The target values
        y_score_list: A list containing sets of prediction probabilities
                      on the target values made by various classifiers.
        clf_label_list: List of strings. Each string is a name of a classifier.
                        The order of this list corresponds to the order of the
                        prediction sets in y_score_list.
        tite: String, the title of the plot
    """
    # Set the size and dpi of the plot
    plt.figure(figsize = (10,10), dpi=300)

    # Lists to store the true positive rates and roc auc scores
    # for each classifier
    tprs = []
    roc_aucs = []
    # Mean true positive rate of all classifiers
    mean_fpr = np.linspace(0, 1, 100)

    i=0
    # Calculate the roc score and plot the roc curve for each
    # set of prediction probabilities in y_score_list. Use the
    # corresponding labels in clf_label_list to identify which
    # ROC curve belongs to which classifier.
    for y_score in y_score_list:
        clf_label = clf_label_list[i]
        i += 1
        fpr, tpr, thresholds = roc_curve(y_test, y_score)
        tprs.append(np.interp(mean_fpr, fpr, tpr))
        tprs[-1][0] = 0.0
        roc_auc = roc_auc_score(y_test, y_score)
        roc_aucs.append(roc_auc)
        plt.plot(fpr, tpr, lw=3, alpha=0.8, label='{} ROC (AUC = %0.6f)'.format(clf_label) % roc_auc)

    # Plot the ROC curve of a random classifier
    plt.plot([0, 1], [0, 1], linestyle='--', lw=2, color='r', label='Luck (AUC = 0.500000)', alpha=.8)

    # Calculate the mean true positive rate and plot it
    mean_tpr = np.mean(tprs, axis=0)
    mean_tpr[-1] = 1.0
    mean_auc = auc(mean_fpr, mean_tpr)
    std_auc = np.std(roc_aucs)
    plt.plot(mean_fpr, mean_tpr, color='b', label=r'Mean ROC all classifiers (AUC = %0.2f $\pm$ %0.2f)' % (mean_auc, std_auc), lw=2, alpha=.3)

    # Set the properties of the plot's axes and labels
    plt.xlim([-0.05, 1.05])
    plt.ylim([-0.05, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(title)
    plt.legend(loc="lower right")
    # Save the plot to a png file
    plt.savefig('{}.png'.format(title))
    # Display the plot
    plt.show()
