from flask import Flask, request, jsonify

app = Flask(__name__)

def calculate_factorial(n):
    if n >= 0 and n <= 15:
        if n == 0 or n == 1:
            return 1
        else:
            return n * calculate_factorial(n-1)
    else:
        return None

def calculate_fibonacci(n):
    if n >= -15 and n <= 15:
        if n <= 1:
            return n
        else:
            return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)
    else:
        return None

@app.route('/')
@app.route('/index')
def index():
    return jsonify({'mensagem': 'Index'})

@app.route('/myapi', methods=['POST'])
def myapi():
    if request.is_json:
        data = request.get_json()

        factorial_result = calculate_factorial(data.get('fact'))
        fibonacci_result = calculate_fibonacci(data.get('fib'))

        response_data = {'factorial': factorial_result, 'fibonacci': fibonacci_result}
        return jsonify(response_data)
    else:
        return jsonify({'error': 'A solicitação deve ser em JSON'}), 400

if __name__ == '__main__':
    app.run(debug=True)
