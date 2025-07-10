
Automacoes com Python 02/03/2021

# Projeto: Dashboard Interativo de Controle de Despesas 


Script disponível no arquivo: **`pipeline_despesas.py`

Este projeto tem como objetivo principal transformar dados brutos de um Google Sheet de controle de despesas em insights financeiros acionáveis, utilizando Python e Streamlit para criar um dashboard interativo e automatizado.

---

O arquivo `pipeline_despesas.py` é o script central responsável por toda a **automação do processo ETL (Extração, Transformação e Carregamento)** dos dados. Ele garante que os dados da sua planilha sejam coletados, limpos, processados e preparados para serem visualizados no dashboard.

### **Bibliotecas Utilizadas para Automação**

Para realizar todas as etapas do nosso pipeline de dados, contamos com as seguintes bibliotecas Python robustas e eficientes:

* **`gspread`**: Essencial para a **interação com o Google Sheets**. Permite que o script acesse e extraia os dados diretamente da sua planilha, atuando como uma ponte segura entre seu código Python e a API do Google Sheets.
* **`pandas`**: A ferramenta fundamental para **manipulação e análise de dados**. Com `pandas`, os dados brutos da planilha são transformados em `DataFrames`, que facilitam operações de limpeza, filtragem, agregação e criação de novas colunas.
* **`os`**: Utilizada para lidar com **variáveis de ambiente e caminhos de arquivo**. Fundamental para o carregamento seguro das credenciais do Google, garantindo que informações sensíveis não sejam expostas diretamente no código ou no controle de versão (Git).
* **`locale`**: Importante para a **configuração regional (idioma e formato)**. Garante que informações como nomes de meses e formatações de data sejam exibidas corretamente no padrão português do Brasil, melhorando a usabilidade.
* **`datetime` (do módulo `datetime`)**: Auxiliar para **operações específicas com objetos de data e hora**. Complementa o `pandas` na manipulação temporal dos dados, permitindo extrair anos, meses e outras informações de tempo de forma precisa.
* **`streamlit` (e `plotly.express`)**: Embora a interface e os gráficos sejam construídos em outro arquivo (`app.py`), essas bibliotecas são mencionadas aqui para contextualizar que os dados processados por `pipeline_despesas.py` servirão de base para a criação de **dashboards interativos**. `streamlit` é o framework web e `plotly.express` facilita a criação de visualizações dinâmicas.

### **Algoritmo de Processamento de Dados (Passo a Passo)**

O `pipeline_despesas.py` executa uma sequência lógica de passos para garantir que seus dados estejam prontos para análise:

1.  **Conexão Segura com o Google Sheets:**
    * **Objetivo:** Estabelecer uma comunicação autenticada e autorizada com a planilha Google Sheets.
    * **Detalhes:** Utiliza as credenciais de uma **Conta de Serviço do Google Cloud Platform (GCP)** (arquivo JSON) para acessar a planilha nomeada. O script verifica se a conexão foi bem-sucedida e se a planilha foi encontrada.

2.  **Extração dos Dados Brutos:**
    * **Objetivo:** Coletar todas as informações da planilha.
    * **Detalhes:** Os dados são lidos linha a linha e convertidos em um `DataFrame` do `pandas`, que é a estrutura padrão para manipulação.

3.  **Validação e Pré-processamento Inicial (Fase de Transformação - ETL):**
    * **Objetivo:** Limpar, padronizar e enriquecer os dados para garantir sua qualidade e usabilidade.
    * **Detalhes:**
        * **Verificação de Colunas:** Confere se as colunas essenciais (`Data`, `Categoria`, `Valor`, etc.) estão presentes.
        * **Tratamento da Coluna 'Data':** Converte a coluna de data para o formato `datetime` do pandas, tratando possíveis erros e removendo registros inválidos. O `locale` é configurado para garantir a formatação correta em português.
        * **Tratamento da Coluna 'Valor':** Limpa a coluna de valores (removendo símbolos de moeda, pontos de milhar, substituindo vírgulas por pontos decimais) e converte para tipo numérico (`float`).
        * **Criação de Colunas Auxiliares:** Gera novas colunas como `Ano`, `Mês` (número) e `Nome do Mês` (em português) a partir da coluna `Data`, facilitando as análises futuras.

4.  **Preparação para Análise:**
    * **Objetivo:** Deixar o `DataFrame` no formato ideal para as visualizações e análises no Streamlit.
    * **Detalhes:** Após todas as transformações, o script confirma que os dados estão prontos,


