import webview

from mental_health_demo.flask_app import flask_app

def app():
    webview.create_window('Flask example', flask_app)
    webview.start()
