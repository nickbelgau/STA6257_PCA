# Initialize PCA, reducing to 2 components for visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
