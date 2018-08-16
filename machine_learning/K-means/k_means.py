import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets.samples_generator import make_blobs

n_clusters = 4
X, y = make_blobs(n_samples=400, n_features=2, centers=n_clusters,cluster_std=5)
fig = plt.figure(figsize=(9,3))

init = np.array([[-0.1, -0.1], [0, 0], [0.1, 0.1],[0.2, 0.2]],  np.float64)
plot_data = {'X': X, 'init': init, 'n_clusters':n_clusters}

class kmeans_plot:

    def __init__(self,plot_data):
        self.cid = fig.canvas.mpl_connect('button_press_event',self)

        ax = fig.add_subplot(1,1,1)
        ax.set_title('k_means')
        ax.axis('equal')
        self.plot_data = plot_data


        X = self.plot_data['X']
        init = self.plot_data['init']
        n_clusters = self.plot_data['n_clusters']
        kmeans = KMeans(n_clusters=n_clusters, random_state=0, init=init, max_iter=1)
        labels = kmeans.fit(X).predict(X)
        ax.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', zorder=2)

        self.plot_data['init']=kmeans.cluster_centers_

        self.ax = axans = KMeans(n_clusters=n_clusters, random_state=0, init=init, max_iter=1)

        def __call__(self, event):
            ax = event.inaxes
            if ax.get_title() == 'k-means':
                X = self.plot_data['X']
                init = self.plot_data['init']
                n_clusters = self.plot_data['n_clusters']

                kmeans = KMeans(n_clusters=n_clusters, random_state=0, init=init, max_iter=1)
                labels = kmeans.fit(X).predict(X)

                self.ax.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', zorder=2)

                self.plot_data['init'] = kmeans.cluster_centers_

kmeans_plot(plot_data)
plt.show()