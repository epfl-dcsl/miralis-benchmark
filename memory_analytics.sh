# Install docker
docker create --name twitter-data cloudsuite/twitter-dataset-graph

# Run analytics benchmark
sudo docker create --name movielens-data cloudsuite/movielens-dataset
sudo docker run --volumes-from movielens-data cloudsuite/in-memory-analytics /data/ml-latest-small /data/myratings.csv

# Run graphs benchmark