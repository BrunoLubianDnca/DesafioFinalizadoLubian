# Bot de Navegação no YouTube

Este é um projeto Python que utiliza o framework Selenium para criar um bot que automatiza a navegação no YouTube. O bot é capaz de buscar por um canal específico, selecionar um vídeo aleatório desse canal e extrair informações como visualizações, descrição e hashtags.

## Pré-requisitos

- Python 3.x instalado
- Bibliotecas necessárias (instaladas via pip):


## Como Usar

1. Clone ou faça o download deste repositório.
2. Certifique-se de ter os pré-requisitos instalados.
3. Execute o arquivo `main.py` com Python.

## Funcionalidades

### 1. `configurar_driver()`

Esta função configura o navegador Chrome para ser utilizado pelo bot.

### 2. `acessar_youtube(driver)`

Esta função abre a página inicial do YouTube no navegador.

### 3. `buscar_canal(driver, nome_canal)`

Esta função realiza uma busca pelo canal especificado no YouTube.

### 4. `abrir_video(driver)`

Esta função seleciona um vídeo aleatório do canal e o abre para visualização.

### 5. `extrair_informacoes(driver)`

Esta função extrai informações do vídeo em exibição, incluindo o número de visualizações, a descrição e as hashtags utilizadas.
