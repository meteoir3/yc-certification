import boto3

def delete_serie_table():
    ydb_docapi_client = boto3.resource('dynamodb', endpoint_url = "<Document API эндпоинт>")

    table = ydb_docapi_client.Table('docapitest/series')
    table.delete()

if __name__ == '__main__':
    delete_serie_table()
    print("Таблица Series удалена")
