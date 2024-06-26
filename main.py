from app import app
import router


if __name__ == '__main__':
    # app.run_server(host='0.0.0.0', port=8050)
    app.run(debug=True)