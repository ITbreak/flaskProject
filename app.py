import webbrowser


from interactions.views import app


if __name__ == '__main__':
    url = 'http://127.0.0.1:5000'

    webbrowser.open_new(url)

    app.run(host="0.0.0.0", port=5000)



