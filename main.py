from typing import List, Optional
from pydantic import BaseModel
from joblib import load
from fastapi import FastAPI


class ScoringData(BaseModel):
    feature_vector: List[float] = []
    score: Optional[bool] = False


app = FastAPI()

model = load('model.joblib')


@app.post("/prediction")
def update_item(scoringData: ScoringData):
    response = {}
    feature = scoringData.feature_vector
    print(feature)
    is_inliner = int(model.predict([feature])[0])
    response['is_inliner'] = is_inliner
    if scoringData.score:
        score = model.score_samples([feature])[0]
        response['score'] = score
    return response

@app.get("/model_information")
async def get_model_information():
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
