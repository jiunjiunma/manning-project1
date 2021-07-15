# prediction with score == false
```aidl
curl -X 'POST' \
  'http://0.0.0.0:8000/prediction' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "feature_vector": [-0.1579526968207469, -0.1067489828357202],
  "score": false
}'
```
Response
```
{
  "is_inliner": 1
}
```

# prediction with score == true
```
curl -X 'POST' \
  'http://0.0.0.0:8000/prediction' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "feature_vector": [-0.1579526968207469, -0.1067489828357202],
  "score": true
}'
```
Response
```
{
  "is_inliner": 1,
  "score": -0.31314463447153723
}
```

# get model parameters
```
curl -X 'GET' \
  'http://0.0.0.0:8000/model_information' \
  -H 'accept: application/json'
```
Response
```
{
  "bootstrap": false,
  "contamination": 0.001,
  "max_features": 1,
  "max_samples": "auto",
  "n_estimators": 100,
  "n_jobs": null,
  "random_state": 16,
  "verbose": 0,
  "warm_start": false
}
```