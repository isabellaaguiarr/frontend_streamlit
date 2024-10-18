# frontend_streamlit
# 📊 Dashboard de Ações com Magic Formula

Este projeto tem como objetivo criar um dashboard interativo utilizando **Streamlit** para visualização de uma carteira de ações baseada na **Magic Formula**, popularizada por Joel Greenblatt. A ferramenta permite uma análise de dados financeiros com gráficos, tabelas, e seleção de cores personalizada.

## ✨ Funcionalidades

- **Criação de uma carteira de ações**: Baseada na Magic Formula.
- **Visualização interativa**: O projeto permite explorar os dados de forma visual, com gráficos, botões e seleção de cores.
- **Exibição de DataFrame**: Carrega um DataFrame de um arquivo CSV com informações financeiras.
- **Filtragem e Gráfico de Barras**: Exibe um gráfico de retorno sobre o patrimônio líquido (ROE) de empresas selecionadas.

## 📂 Estrutura do Projeto

- **app.py**: Arquivo principal do projeto que contém o código do dashboard.
- **data/planilhao.csv**: Arquivo CSV com os dados financeiros das empresas.

## 🖼️ Interface do Dashboard

O projeto utiliza o **Streamlit** para gerar uma interface web interativa com as seguintes abas:
1. **Botão**: Exibe um botão de exemplo.
2. **Radio**: Permite selecionar cores e exibe mensagens com base na escolha.
3. **DataFrame**: Mostra uma tabela com dados de um arquivo CSV.
4. **Gráfico**: Gera um gráfico de barras com o retorno sobre o patrimônio líquido (ROE) de empresas selecionadas.

## 🛠️ Requisitos

- **Python 3.7 ou superior**
- **Bibliotecas necessárias**:
  - `pandas`
  - `matplotlib`
  - `streamlit`

## 🚀 Instruções de Execução

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu_usuario/seu_projeto.git
   cd seu_projeto
