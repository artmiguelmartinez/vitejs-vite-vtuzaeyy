import kagglehub

# Download latest version
path = kagglehub.dataset_download("duartepereiradacruz/euromillions-historical-data")

print("Path to dataset files:", path)
