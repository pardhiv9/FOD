import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load and preprocess the data
data = pd.read_csv('customer_data.csv')  # Replace with your data source
selected_features = data[['purchase_history', 'browsing_behavior', 'demographics']]
scaled_features = StandardScaler().fit_transform(selected_features)

# Choosing the number of clusters using the Elbow Method
inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit(scaled_features)
    inertia.append(kmeans.inertia_)

# Plot the Elbow Method graph
plt.plot(range(1, 11), inertia, marker='o')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method')
plt.show()

# Based on the Elbow Method, choose a suitable number of clusters and apply K-means
num_clusters = 4  # You can adjust this based on the elbow method graph
kmeans = KMeans(n_clusters=num_clusters, random_state=0)
cluster_labels = kmeans.fit_predict(scaled_features)

# Add the cluster labels to the original data
data['cluster'] = cluster_labels

# Analyze and visualize the clusters
for cluster in range(num_clusters):
    cluster_data = data[data['cluster'] == cluster]
    print(f"Cluster {cluster}:\n{cluster_data.describe()}")

# You can now use the 'cluster' labels for targeted marketing campaigns
