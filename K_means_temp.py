
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

def euclidean_distance(x1,x2):
    return np.sqrt(np.sum((x1-x2)**2))

class KMeans:
    def __init__(self, K = 5, max_iters = 100, plot_steps = False):
        self.K = K
        self.max_iters = max_iters
        self.plot_steps = plot_steps

        # list of sample indices for each cluster
        self.clusters = [[] for _ in range(self.K)]
        # mean feature vector for each cluster
        self.centroids = []

    def predict(self,X):
        self.X = X
        self.n_samples, self.n_features = X.shape

        # initialize centroids
        # replace = False because we don't want to pick the same indicate twice
        # this will be an array have size = size.K and for each entry, it will pick a random choice
        # between 0 and self.sample
        random_sample_idx = np.random.choice(self.n_samples, self.K, replace = False)
        self.centroids = [self.X[idx] for idx in random_sample_idx]

        # opzimization
        for _ in range(self.max_iters):
            # update cluster
            self.clusters = self._create_clusters(self.centroids)
            if self.plot_steps:
                self.plot()

            # update centroids
            centroids_old = self.centroids
            self.centroids = self._get_centroids(self.clusters)
            if self.plot_steps:
                self.plot()

            # check if converged (kiểm tra sự hội tụ)
            if self._is_converged(centroids_old, self.centroids):
                break

        #return cluster labels
        return self._get_cluster_labels(self.clusters)

    def _get_cluster_labels(self, clusters):
        labels = np.empty(self.n_samples)
        for cluster_idx, cluster in enumerate(clusters):
            for sample_idx in cluster:
                labels[sample_idx] = cluster_idx
        return labels

    def _create_clusters(self, centroids):
        clusters = [[] for _ in range(self.K)]
        for idx, sample in enumerate(self.X):
            centroid_index = self._closet_centroid(sample,centroids)
            clusters[centroid_index].append(idx)
        return clusters

    def _closet_centroid(self, sample, centroids):
        distances = [euclidean_distance(sample,point) for point in centroids]
        closet_idx = np.argmin(distances)
        return closet_idx

    def _get_centroids(self, clusters):
        centroids = np.zeros((self.K, self.n_features))
        for clusters_idx, cluster in enumerate(clusters):
            cluster_mean = np.mean(self.X[cluster],axis = 0)
            centroids[clusters_idx] = cluster_mean
        return centroids

    def _is_converged(self,centroids_old,centroids):
        distances = [euclidean_distance(centroids_old[i],centroids[i]) for i in range(self.K)]
        return sum(distances) == 0

    def plot(self):
        fig, ax = plt.subplots(figsize = (12,8))

        for i, index in enumerate(self.clusters):
            point = self.X[index].T
            ax.scatter(*point)

        for point in self.centroids:
            ax.scatter(*point, marker = "x", color = "black", linewidth = 2)

        plt.show()

if __name__ == "__main__":
    from sklearn.datasets import make_blobs

    X, y = make_blobs(
        centers=3, n_samples=500, n_features=2, shuffle=True, random_state=40
    )
    print(X.shape)

    clusters = len(np.unique(y))
    print(clusters)

    k = KMeans(K=clusters, max_iters=150, plot_steps=True)
    y_pred = k.predict(X)

    k.plot()