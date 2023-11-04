
# GameTalks 🎮

## Passo a passo da instalação

1. Clone o repositório:
   ```
   git clone https://github.com/limarich/GameTalks.git
   ```

2. Inicie o ambiente virtual na pasta do projeto. Use um dos comandos a seguir, dependendo da versão do Python que você está usando:

   - Python 2.x:
     ```
     python -m virtualenv venv
     ```
   - Python 3.x:
     ```
     python3 -m venv venv
     ```

3. Ative o ambiente virtual:
   - No Windows:
     ```
     .\venv\Scripts\activate
     ```
   - No macOS e Linux:
     ```
     source venv/bin/activate
     ```

4. Utilize o `pip` para instalar as dependências do projeto a partir do arquivo requirements.txt:
   ```
   pip install -r requirements.txt
   ```

5. Tente executar o projeto Django com o seguinte comando:
   ```
   python manage.py runserver
   ```

Isso deve iniciar o servidor de desenvolvimento do Django, e você poderá acessar seu projeto no navegador em `http://localhost:8000/`. Certifique-se de que o ambiente virtual esteja ativado sempre que você trabalhar no projeto Django.
