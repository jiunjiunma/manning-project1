from typing import List, Optional
from pydantic import BaseModel
from joblib import load
from fastapi import FastAPI
from datetime import datetime
import prometheus_client
from prometheus_client import Counter, Histogram, Gauge

class ScoringData(BaseModel):
    feature_vector: List[float] = []
    score: Optional[bool] = False


app = FastAPI()
metrics_app = prometheus_client.make_asgi_app()
app.mount("/metrics", metrics_app)

model = load('model.joblib')
prediction_counter = Counter('prediction', 'Prediction endpoint counter')
model_info_counter = Counter('model_information', 'Model information endpoint counter')
latency_histogram = Histogram('request_latency_histogram', 'Prediction Latency Histogram')
prediction_histogram = Histogram('prediction_score_histogram', 'Prediction Latency Histogram')
score_histogram = Histogram('sample_score_histogram', 'Sample Score Histogram')
g = Gauge('is_inliner', 'Description of gauge')

@app.post("/prediction")
async def update_item(scoringData: ScoringData):
    start_time = datetime.now()
    prediction_counter.inc()
    response = {}
    feature = scoringData.feature_vector
    is_inliner = int(model.predict([feature])[0])
    response['is_inliner'] = is_inliner
    prediction_histogram.observe(is_inliner)
    g.set(is_inliner)
    if scoringData.score:
        score = model.score_samples([feature])[0]
        score_histogram.observe(score)
        response['score'] = score
    end_time = datetime.now()
    latency = end_time - start_time
    latency_histogram.observe(latency.total_seconds())
    return response

@app.get("/model_information")
async def get_model_information():
    model_info_counter.inc()
    return model.get_params()

#if __name__ == "__main__":
#    model = load('../jupyter/model.joblib')
#    value = [-0.1579526968207469, -0.1067489828357202]
#    predictions = model.predict([value])
#    print(predictions)
#
#    data = {
#        'feature_vector': [-0.1579526968207469, -0.1067489828357202]
#    }
#    scoring_data =  ScoringData(**data)
#    assert scoring_data.feature_vector == value
#    print(scoring_data.score)
