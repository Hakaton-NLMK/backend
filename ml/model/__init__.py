import threading

import requests as requests
from langchain.llms.base import LLM
from typing import Optional, List, Mapping, Any
from langchain_core.callbacks import (
    CallbackManagerForLLMRun,
)
from typing_extensions import ClassVar

from ml.variables import key_api

BASE_URL = 'https://api.proxyapi.ru/openai/v1/chat/completions'  # Базовый URL
API_KEY = key_api
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'Bearer {API_KEY}'
}


class API:
    def init(self):
        self.BASE_URL = BASE_URL
        self.headers = headers

    def send_message(self, text):
        data = {
            "model": "gpt-4-turbo",
            "messages": [{"role": "system","content":"You are generator javascript code, that must use nlmk сomponents. Pay attention to not write jsx/javascript in the beginning of the script, because the user already has it."},{"role": "user", "content": text}]
        }
        path = ""
        print(data)
        return post_request(data, path)



def handle_response(response):
    if response.status_code == 200:
        return response.json()
    else:
        print(response)
        print(response.status_code)
        print(response.json())
        raise Exception('bad ans')

def post_request(data, path, headers=headers, BASE_URL=BASE_URL):
    response = requests.post(BASE_URL + path, headers=headers, json=data)
    print(response)
    response = handle_response(response)
    print(str(response))
    return response


class API_Model(LLM):
    """ send request to api
     conversation_id - """
    def init(self, **kwargs: Any):
        super().init(**kwargs)

    def _call(self,
              prompt: str,
              stop: Optional[List[str]] = None,
              run_manager: Optional[CallbackManagerForLLMRun] = None,
              **kwargs: Any, ) -> str:
        print('api_model_work!')
        message = self.api.send_message(prompt)
        output = message
        return output
    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        return {"name_of_model": self.model_name}
    @property
    def _llm_type(self) -> str:
        return "api_model"



class API_Model_GPT(API_Model):
    """ get ans by api from gpt4  """
    model_name: ClassVar[str] = 'api_gpt'

    def init(self, **kwargs: Any):
        super().init(**kwargs)

    def _call(self,
              prompt: str,
              stop: Optional[List[str]] = None,
              run_manager: Optional[CallbackManagerForLLMRun] = None,
              **kwargs: Any, ) -> str:
        print('api_model_work!')
        print(prompt)
        lock = threading.Lock()
        api = API()
        lock.acquire()
        try:
            message = api.send_message(prompt)

        except Exception as e:
            print(e)
            raise e
        finally:
            lock.release()
        output = message['choices'][0]['message']['content']
        return output
