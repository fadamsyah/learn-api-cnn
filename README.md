# learn-api-cnn

## Explanation
### app.py
Main `streamlit` web app script using `port 8080`.

### cnn-api.py 
-   port : `5000`
-   extension: `/predict`
-   method: `POST`
-   argument: `files = {'image_bytes': <bytes>}`
-   response: `{'class_id': <int>, 'class_name': <str>, 'probability': <float>}`

### test-cnn-api.py
A script to test `cnn-api.py`.

## Tools
- Pytorch
- Flask
- PIL

## How To Use
I use `Ubuntu 20.04` to develop this repository.
### Install
```
# Clone this repository
git clone https://github.com/fadamsyah/learn-api-cnn.git

# Change directory to the cloned repo

# Install miniconda https://conda.io/miniconda.html
conda install -c conda-forge mamba

# Create an environment
mamba env create -f environment.yml

# Grant run.sh the permission to run
chmod +x run.sh
```

### Run
```
bash -i run.sh
```

## References
- [DEPLOYING PYTORCH IN PYTHON VIA A REST API WITH FLASK
](https://pytorch.org/tutorials/intermediate/flask_rest_api_tutorial.html)

## Sources:
- [`assets/orange.jpg`](https://indonesian.alibaba.com/product-detail/Fresh-valencia-orange-supply-62469562306.html)
- [`assets/icecream.jpg`](https://www.thepioneerwoman.com/food-cooking/recipes/a39979824/blueberry-ice-cream-recipe/)