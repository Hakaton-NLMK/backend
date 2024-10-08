from langchain_community.llms import YandexGPT
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from .model import API_Model_GPT
from .variables import grid_description
from .db import docsearch
from .auth import generateToken

iam_token = generateToken()

retriever = docsearch.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"k": 3, "score_threshold": 0.1},
)


def create_component(request):
    question = request

    template = """
    Ты ассистент, который разделяет входящий запрос на несколько подзапросов.
    В основном входящий запрос будет требовать сгенерировать веб-интерфейс по описанию.
    Разбей запрос на набор подзадач генерации отдельных высокоуровневых веб-компонент.
    Каждая подзадача должна соответствовать одной единственной веб-компоненте.
    Если в запросе указано название компоненты, то обязательно сохрани его.
    Если в запросе указано относительное положение компненты, то обязательно сохрани его и продублируй название компоненты относительно которой она будет располагаться.
    Сгенерируй несколько подзапросов для запроса: {question}.

    Обязательно соблюдай правила форматирования ответа:
    - Ничего кроме самих подзапросов писать не нужно.
    - Один подзапрос - одно предложение.
    - Подзапросы должны быть разделены символом перевода строки '\n'.
    - Не должно быть 2 '\n' подряд!

    Пример:
    Запрос пользователя - создай кнопку, слевой от неё текст люблю щенят
    Твой ответ:
    1.Создай первый элемент кнопка 'Button'
    2.Добавь слево (c помощью greed) от первого элемента(кнопки) второй элемент input c тестом "люблю щенят"
    """
    prompt_decomposition = ChatPromptTemplate.from_template(template)

    # stupid = YandexGPT(iam_token=iam_token, model_uri=model_uri, tempreture=0)
    stupid = API_Model_GPT()

    generate_queries_decomposition = (
                prompt_decomposition | stupid | StrOutputParser() | (lambda x: x.replace('\n\n', '\n')))

    # Run
    question = generate_queries_decomposition.invoke({"question": question})

    template = """
        Ты - генератор интерфейсов по запросу пользователя на естественном языке.
        Твой ответ должен содержать только код и не должен содержать описания или другого постороннего текста.
        Ты обязан использовать дизайн компоненты системы НЛМК.
        Учитывай, что твой вывод должен быть валидным React.js кодом, который можно запускать без ошибок.
        Не забывай импортировать элементы. Обрати внимание, что некоторые элементы cостоят из 2 <> : <Button></>,  а некоторые из 1 <Input />.
        Не пиши React.js или javascript в начале кода!!
        Не ставь многоточие, чтоб пропустить элементы. Каждый элемент должен быть прописан (написано 9 кнопок - 9 элементов должны быть )
        Будь очень внимателен к расположению элементов относительно друг друга. Все элементы должны быть видны.
        Ответь на вопрос, используя следующие элементы.Если можно использовать элемент - обязательно используй:
        {context}

        Используй Grid для позиционирования элементов.
        Используй его обязательно, урежем зп а то.

        Вопрос: {question}
    """

    prompt = ChatPromptTemplate.from_template(template)
    # llm = YandexGPT(iam_token=iam_token, model_uri=model_uri, tempreture=0.35)
    llm = API_Model_GPT()

    chain = prompt | llm
    results = docsearch.similarity_search(query=question, k=9)
    context = results[0].page_content + results[1].page_content + results[2].page_content + results[3].page_content + \
              results[4].page_content + results[5].page_content + results[6].page_content + results[7].page_content + \
              results[8].page_content + grid_description

    ans = chain.invoke({'question': question, 'context': context})
    ans =  clean_ans (ans)
    return ans


def clean_ans (ans):
    if '```' in ans:
        ans = ans.split('```')[1]
    parts = ans.split('\n')
    if len(parts) > 1 and ('javascript' in parts[0] or 'jsx' in parts[0]):
        ans = '\n'.join(parts[1:])
    if len(parts) > 2 and ('javascript' in parts[1] or 'jsx' in parts[1]):
        ans = '\n'.join(parts[2:])
    return ans

