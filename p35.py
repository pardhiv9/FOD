import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load and preprocess the data
data = pd.read_csv('transaction_data.csv')  # Replace with your data source

# Select features for clustering
selected_features = ['total_amount_spent', 'frequency_of_visits']
X = data[selected_features]

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Choosing the number of clusters using the Elbow Method
inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

# Plot the Elbow Method graph
plt.plot(range(1, 11), inertia, marker='o')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method')
plt.show()

# Based on the Elbow Method, choose a suitable number of clusters and apply K-means
num_clusters = 3  # You can adjust this based on the elbow method graph
kmeans = KMeans(n_clusters=num_clusters, random_state=0)
cluster_labels = kmeans.fit_predict(X_scaled)

# Add the cluster labels to the original data
data['cluster'] = cluster_labels

# Analyze and interpret the clusters
for cluster in range(num_clusters):
    cluster_data = data[data['cluster'] == cluster]
    print(f"Cluster {cluster}:\n{cluster_data.describe()}")
