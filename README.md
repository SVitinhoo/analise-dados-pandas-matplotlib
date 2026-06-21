<h1>📊 Pipeline FAPESP</h1>
<img src="https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Pandas-Data_Analysis-150458?logo=pandas&logoColor=white"/>
<img src="https://img.shields.io/badge/Matplotlib-DataViz-11557c"/>
<hr>

<h2>ℹ️ Sobre</h2>
<p>
Solução automatizada de ponta a ponta para <strong>ETL (Extract, Transform, Load)</strong> e análise estatística baseada em dados públicos de fomento à pesquisa da FAPESP.<br>
O script foi desenvolvido para substituir processos manuais de manipulação de planilhas por um fluxo de execução ágil, otimizado e escalável, gerando relatórios analíticos e gráficos de forma 100% programática.
</p>

<h3>🛠️ Tecnologias</h3>
<ul>
    <li><strong>Python 3.12</strong> — Linguagem base do projeto</li>
    <li><strong>Pandas</strong> — Manipulação eficiente, limpeza e cruzamento de grandes volumes de dados</li>
    <li><strong>Matplotlib</strong> — Renderização e exportação automatizada de gráficos estatísticos</li>
    <li><strong>Pathlib & Dateutil</strong> — Gerenciamento seguro de caminhos de arquivos e manipulação cronológica avançada</li>
</ul>
<hr>

<h2>🚀 Funcionalidades da Automação</h2>
<ul>
    <li><strong>Consolidação Inteligente (ETL):</strong> Varre dinamicamente a pasta de dados brutos, identifica os arquivos disponíveis e os unifica em uma única base de dados consolidada (<code>final.csv</code>), tratando redundâncias de cabeçalho automaticamente.</li>
    <li><strong>Tratamento de Dados com Regex (Data Cleaning):</strong> Identifica e remove inconsistências de strings e erros de concatenação na coluna de localização usando expressões regulares.</li>
    <li><strong>Feature Engineering Cronológica:</strong> Realiza o <em>parsing</em> de strings de data e calcula dinamicamente o tempo médio de fomento em meses através de uma função personalizada.</li>
    <li><strong>Geração Automática de Artefatos:</strong> Exporta automaticamente os resultados processados em novos arquivos CSV estruturados e gera plots gráficos (<code>.jpg</code>) formatados para tomada de decisão.</li>
</ul>

<hr>
<h2>⬇️ Instalação e Execução</h2>
<p>Tenha o <strong>Python 3.12</strong> instalado no seu sistema, clone o repositório e acesse a pasta do projeto:</p>
<pre><code>git clone https://github.com/SVitinhoo/analise-dados-pandas-matplotlib.git
cd analise-dados-pandas-matplotlib</code></pre>

<p>Instale as dependências do projeto contidas no <code>requirements.txt</code>:</p>
<pre><code>pip install -r requirements.txt</code></pre>

<p>Certifique-se de que os arquivos <code>.csv</code> brutos estejam dentro da pasta <code>csv/</code> e execute o script principal:</p>
<pre><code>python main.py</code></pre>

<p>O script irá automaticamente processar os dados brutos, consolidar a base e gerar a pasta <code>resultado/</code> com todas as tabelas e gráficos prontos.</p>
<hr>

<h2>📁 Estrutura do Repositório</h2>
<pre><code>analise-dados-pandas-matplotlib
├── csv/                   — Diretório de entrada com os dados brutos
├── resultado/             — Outputs gerados automaticamente pelo script (*.csv e *.jpg)
├── .gitignore             — Filtro para evitar o upload de dados pesados e temporários
├── LICENSE                — Licença do repositório
├── main.py                — Script principal da automação
├── README.md              — Documentação do projeto
└── requirements.txt       — Dependências de bibliotecas do projeto
</code></pre>
<hr>

<h2>⚠️ Observações</h2>
<ul>
    <li>O arquivo <code>final.csv</code> e a pasta <code>resultado/</code> são criados automaticamente se não existirem.</li>
    <li>Certifique-se de manter os nomes das colunas originais nos arquivos contidos em <code>csv/</code> para evitar quebras no mapeamento do Pandas.</li>
</ul>
