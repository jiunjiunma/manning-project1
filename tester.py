import pandas as pd
import requests


def main():
    df_test = pd.read_csv('test.csv')
    values = df_test.values
    count = 0
    for value in values:
        count += 1

        payload = {
            'feature_vector': list(value),
            'score': ((count % 4) == 0)
        }

        requests.post('http://127.0.0.1:8000/prediction', json=payload)

    response = requests.get('http://127.0.0.1:8000/model_information')
    print(response.text)

    return


if __name__ == "__main__":
    main()

