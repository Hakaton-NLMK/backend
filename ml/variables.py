CA = './CA.pem' # если вы не меняли путь при скачивании сертификата
VERIFY = True
SECURE = True
USER = 'admin'
PASSWORD = '5U?H.5,F-@D$p2b'
HOST = "rc1d-3lv6d1bous4laj3t.mdb.yandexcloud.net" # адрес Clickhouse
PORT = 8443


folder = 'b1gkt5jnf1leugqln1r2'
service_account_id = "ajeun4aue16or4mk4lta"
key_id = "ajeefvp6s70c4aipdr84"
model_uri = f'gpt://{folder}/yandexgpt/latest'

key_api = 'sk-kllZ7MZAyhbzNJVpWfT7SPxDtI2jkJXi'

grid_description = 'Grid\n\nОписание:\nКомпонент Grid представляет собой универсальный контейнер, используемый для позиционирования внутренних компонентов/элементов: горизонтальный или вертикальный. Он обладает различными пропсами, что делает Grid инструментом для создания структурированного и адаптивного интерфейса.\nПеренос колонок\n\nКод:\nimport { Grid, Box } from \'@nlmk/ds-2.0\';\n\nconst App = () => (\n    <Grid borderRadius="var(--4-border)">\n      <Grid.Row borderRadius="var(--4-border)" background="var(--error-red-100)">\n        <Grid.Column borderRadius="var(--4-border)" background="var(--primary-blue-400)" width="75%">\n          <Box\n            st={{ flex: \'1\' }}\n            px="var(--8-space)"\n            py="var(--16-space)"\n            borderRadius="var(--4-border)"\n            background="var(--primary-blue-400)"\n          >\n            .col-9\n          </Box>\n        </Grid.Column>\n        <Grid.Column borderRadius="var(--4-border)" background="var(--primary-blue-400)" width="33.33%">\n          <Box\n            st={{ flex: \'1\' }}\n            px="var(--8-space)"\n            py="var(--16-space)"\n            borderRadius="var(--4-border)"\n            background="var(--primary-blue-400)"\n          >\n            .col-4\n          </Box>\n          <br />\n          <Box\n            st={{ flex: \'1\' }}\n            px="var(--8-space)"\n            py="var(--16-space)"\n            borderRadius="var(--4-border)"\n            background="var(--primary-blue-400)"\n          >\n            Поскольку 9 + 4 = 13 &gt; 12, этот div шириной 4 колонки переносится на новую строку как единое целое.\n          </Box>\n        </Grid.Column>\n        <Grid.Column borderRadius="var(--4-border)" background="var(--primary-blue-400)" width="50%">\n          <Box\n            st={{ flex: \'1\' }}\n            px="var(--8-space)"\n            py="var(--16-space)"\n            borderRadius="var(--4-border)"\n            background="var(--primary-blue-400)"\n          >\n            .col-6\n          </Box>\n          <br />\n          <Box\n            st={{ flex: \'1\' }}\n            px="var(--8-space)"\n            py="var(--16-space)"\n            borderRadius="var(--4-border)"\n            background="var(--primary-blue-400)"\n          >\n            Последующие колонки продолжаются на новой строке.\n          </Box>\n        </Grid.Column>\n      </Grid.Row>\n    </Grid>\n);\nexport default App;\n\n\n'
