import webview
import requests

# Функция для перевода текста с помощью API переводчика
def translate_text(text, target_language):
    # Ваш ключ API и URL для переводчика
    api_key = 'YOUR_API_KEY'
    url = 'https://translation.googleapis.com/language/translate/v2'

    # Параметры запроса
    params = {
        'key': api_key,
        'q': text,
        'target': target_language
    }

    # Отправка запроса на перевод
    response = requests.get(url, params=params)
    translation = response.json()['data']['translations'][0]['translatedText']
    return translation

# Создание пользовательского интерфейса с использованием HTML
html = """
<!DOCTYPE html>
<html>
<head>
    <title>Синхронный переводчик</title>
</head>
<body>
    <h1>Синхронный переводчик</h1>
    <input type="text" id="inputText">
    <button onclick="translate()">Перевести</button>
    <p id="outputText"></p>

    <script>
        function translate() {
            var inputText = document.getElementById('inputText').value;
            // Вызов функции перевода из Python
            var translatedText = pywebview.api.translate_text(inputText, 'en');
            document.getElementById('outputText').innerText = translatedText;
        }
    </script>
</body>
</html>
"""

# Функция для обработки запросов из HTML
def translate_text_from_html(text, target_language):
    return translate_text(text, target_language)

# Создание окна с веб-страницей
webview.create_window("Синхронный переводчик", html=html, js_api=translate_text_from_html)
webview.start()
