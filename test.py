from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from ml.model import API, API_Model_GPT
from ml.variables import grid_description


def test_API():
    api = API()
    text = '''
    Ты  генерируешь интерфейсы из кода. Твой ответ должен быть кодом. 
    \nВот тебе данные элементы из которых ты должен собрать ответ пользователю (а именно код).\nImagePicture обеспечивает гибкую отрисовку изображений с различными соотношениями сторон и радиусами границ. Поддерживает функцию зума при наведении. Базовый ImagePicture. Отображает изображение с заданными параметрами.const App = () => {\n  const path = 'https://images.unsplash.com/photo-1683343946402-85b144e8ecb6?q=80&w=3570&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D';\n\n  return (\n    <ImagePicture src={path} alt=\"Описание изображения\" />\n  )\n};\n\nexport default App; Card\nStable\nможно использовать\nКомпонент Card является функциональным компонентом, который предназначен для отображения карточки с различными элементами интерфейса, такими как изображение, заголовок, описание, значки, селектор и группа кнопок. Card по умолчанию import { Button, Card, Typography, Select } from '@nlmk/ds-2.0';\n\nexport default  App = () => (\n  <>\n    <div style={{\n      backgroundColor: 'var(--steel-20)',\n      width: 'fit-content',\n      padding: '20px'\n  }}>\n    <Card>\n      <div\n        style={{\n          height: '200px',\n          width: '300px',\n          display: 'flex',\n          flexDirection: 'column',\n          gap: '10px'\n        }}\n      >\n        <Typography variant='Heading3'>\n          Заголовок\n        </Typography>\n\n        <Select\n          label=\"Выберите язык программирования\"\n          options={[\n            {\n              label: 'C++',\n              value: 'C++'\n            },\n            {\n              label: 'C#',\n              value: 'C#'\n            }]}\n        />\n\n        <div style={{ display: 'flex', gap: '8px', marginTop: 'auto' }}>\n          <Button>\n            Button\n          </Button>\n          <Button variant=\"secondary\">\n            Button\n          </Button>\n        </div>\n      </div>\n    </Card>\n  </div>\n</>\n)\nCard с разными вариантами ориентации import { Button, Card, Typography, Select } from '@nlmk/ds-2.0';\n\nexport default  App = () => (\n  <div style={{\n    backgroundColor: 'var(--steel-20)',\n    width: 'fit-content',\n    padding: '20px',\n    display: 'flex',\n    gap: '20px'\n  }}>\n    <Card>\n    <div\n        style={{\n          height: '200px',\n          width: '300px',\n          display: 'flex',\n          flexDirection: 'column',\n          gap: '10px'\n        }}\n      >\n        <Typography variant='Heading3'>\n          Заголовок\n        </Typography>\n\n        <Select\n          label=\"Выберите язык программирования\"\n          options={[\n            {\n              label: 'C++',\n              value: 'C++'\n            },\n            {\n              label: 'C#',\n              value: 'C#'\n            }]}\n        />\n\n        <div style={{ display: 'flex', gap: '8px', marginTop: 'auto' }}>\n          <Button>\n            Button\n          </Button>\n          <Button variant=\"secondary\">\n            Button\n          </Button>\n        </div>\n      </div>\n    </Card>\n\n    <Card orientation=\"horizontal\">\n      <div style={{ display: 'flex', flexDirection: 'column', gap: '12px', width: '300px'}}>\n        <Typography variant='Heading3'>\n          Заголовок\n        </Typography>\n\n        <Select\n          label=\"Выберите язык программирования\"\n          options={[\n            {\n              label: 'C++',\n              value: 'C++'\n            },\n            {\n              label: 'C#',\n              value: 'C#'\n            }]}\n        />\n\n        <div style={{ display: 'flex', gap: '8px' }}>\n          <Button>\n            Button\n          </Button>\n          <Button variant=\"secondary\">\n            Button\n          </Button>\n        </div>\n      </div>\n    </Card>\n  </div>\n)\nInput\nStable\nможно использовать\nКомпонент Input позволяет пользователям вводить текстовую информацию.
    Он поддерживает различные варианты, включая лейблы, иконки, многострочный ввод и различные стили. import { Input } from '@nlmk/ds-2.0';\n\nexport default App = () => (\n  <>\n    <Input />\n  </>\n);\nКонец списка элементов для твоего использования, вот  запрос пользователя: Создай карточку продукта с изображением, названием и ценой.  твой ответ должен состоять только из кода , если используються какие-то переменые самостоятельно придумай им значения",
    '''
    response = api.send_message(text)
    print(response)

def full_test():
    def decomposotion(request):
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
        return question
    return decomposotion("Создай панель навигации с логотипом и тремя ссылками: 'Главная', 'О нас',  'Контакты'. ")


def generate_code_test_1():
    question = """1.Создай первый элемент панель навигации 'NavigationPanel'
2.Добавь внутрь первого элемента(панели навигации) второй элемент логотип 'Logo'
3.Добавь внутрь первого элемента(панели навигации) третий элемент ссылку с текстом "Главная" 'HomeLink'
4.Добавь внутрь первого элемента(панели навигации) четвертый элемент ссылку с текстом "О нас" 'AboutLink'
5.Добавь внутрь первого элемента(панели навигации) пятый элемент ссылку с текстом "Контакты" 'ContactLink'"""
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
    llm = API_Model_GPT()

    prompt = ChatPromptTemplate.from_template(template)

    chain = prompt | llm
    context = grid_description


    ans = chain.invoke({'question': question, 'context': context})
    ans = clean_ans(ans)
    return ans

def generate_code_test_2():
    question = """Дай кнопку"""
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
    llm = API_Model_GPT()

    prompt = ChatPromptTemplate.from_template(template)

    chain = prompt | llm
    context = grid_description


    ans = chain.invoke({'question': question, 'context': context})
    ans = clean_ans(ans)
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

def test_clean():
    text= """javascript
import { Grid, Button } from '@nlmk/ds-2.0';

const App = () => (
  <Grid>
    <Grid.Row>
      <Grid.Column>
        <Button> Обычная кнопка </Button>
      </Grid.Column>
    </Grid.Row>
  </Grid>
);

export default App;"""
    return clean_ans(text)




print(generate_code_test_2())