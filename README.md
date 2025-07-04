# Bimer API Integration

## Visão Geral
Este projeto é uma aplicação web para gerenciamento de PCP (Planejamento e Controle da Produção) integrado com o sistema ERP Alterdata Bimer, permitindo navegação entre diferentes ferramentas como Dashboard, Ordens de Serviço e Requisições de Material.

## Instalação
1. **Clone o repositório:**
   ```bash
   git clone <url-do-repositorio>
   cd bimer-api-integration
   ```
2. **Instale o [mise](https://mise.jdx.dev/) para gerenciar versões do Python (opcional, mas recomendado).**
3. **Instale a versão recomendada do Python:**
   ```bash
   mise install python@3.10
   mise use python@3.10
   ```
4. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
5. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

## Execução
Para rodar a aplicação, execute:
```bash
python main.py
```
Acesse a interface via navegador no endereço exibido no terminal (por padrão, http://127.0.0.1:8050).

## Dependências Principais
- Dash
- Flask
- Pandas
- Numpy
- Plotly
- dash-bootstrap-components

Consulte o arquivo `requirements.txt` para a lista completa.

## Observações
- Caso não deseje conectar ao banco de dados SQL Server, a aplicação pode ser executada em modo "mock", retornando dados vazios.
- Para conectar ao banco, configure as variáveis de ambiente necessárias no arquivo `.env`.