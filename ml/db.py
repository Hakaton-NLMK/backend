import clickhouse_connect
from langchain_community.vectorstores import Clickhouse, ClickhouseSettings
from langchain_community.embeddings.yandex import YandexGPTEmbeddings
from .variables import CA, VERIFY, SECURE, USER, PASSWORD, HOST, PORT, folder
from .auth import generateToken

def connectDataBase():
    with clickhouse_connect.get_client(
                host=HOST, port=PORT, username=USER,
                password=PASSWORD, secure=SECURE, verify=VERIFY, ca_cert=CA) as ch_client:
            print(ch_client.command('SELECT version()'))


embeddings = YandexGPTEmbeddings(iam_token=generateToken(), folder_id=folder)
ch_config = ClickhouseSettings(host=HOST, port=PORT, username=USER, password=PASSWORD)
docsearch = Clickhouse(embedding=embeddings, config=ch_config, verify=VERIFY, ca_cert=CA)

