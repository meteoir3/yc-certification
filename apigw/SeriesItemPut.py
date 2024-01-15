from pprint import pprint
import boto3

def put_serie(series_id, title, release_date, series_info):
    ydb_docapi_client = boto3.resource('dynamodb', endpoint_url = "https://docapi.serverless.yandexcloud.net/ru-central1/b1g79flr7bn2j3cae2nq/etnem3afffakje339c4m")

    table = ydb_docapi_client.Table('docapitest/series')
    response = table.put_item(
      Item = {
            'series_id': series_id,
            'title': title,
            'info': {
                'release_date': release_date,
                'series_info': series_info
            }
        }
    )
    return response

if __name__ == '__main__':
    serie_resp = put_serie(3, "Supernatural", "2015-09-13",
                          "Supernatural is an American television series created by Eric Kripke")
    print("Сериал успешно добавлен:")
    pprint(serie_resp, sort_dicts = False)
