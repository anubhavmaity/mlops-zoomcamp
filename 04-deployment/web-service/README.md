## Deploying model as a web-service

- Creating a virtual env with Pipenv
- Creating a script for predicting
- Putting the script into flask app
- Packaging app to Docker

```bash
docker build -t ride-duration-prediction-service:v1 .
```

```bash
docker run -it --rm -p 9696:9696 ride-duration-prediction-service:v1
```