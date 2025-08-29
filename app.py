from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def bfhl():
    try:
        # Check if 'data' key exists in the request JSON
        if 'data' not in request.json:
            raise ValueError("Invalid input: 'data' key is missing")
        
        input_data = request.json['data']
        if not isinstance(input_data, list):
            raise ValueError("Invalid input: 'data' must be a list")

        even_numbers = []
        odd_numbers = []
        alphabets = []
        special_characters = []
        total_sum = 0
        alpha_string = ''

        for item in input_data:
            if not isinstance(item, str):
                continue  # Skip non-string items gracefully

            if item.isdigit():
                n = int(item)
                total_sum += n
                if n % 2 == 0:
                    even_numbers.append(item)
                else:
                    odd_numbers.append(item)
            elif item.isalpha():
                upper_item = item.upper()
                alphabets.append(upper_item)
                alpha_string += upper_item
            else:
                special_characters.append(item)

        # Build the concatenated string: reverse alpha_string and alternate cases
        rev_alpha = alpha_string[::-1]
        concat_str = ''
        for i, char in enumerate(rev_alpha):
            if i % 2 == 0:
                concat_str += char.upper()
            else:
                concat_str += char.lower()

        response = {
            "is_success": True,
            "user_id": "aravind_m_12122003",
            "email": "aravind.m2022a@vitstudent.ac.in",
            "roll_number": "22BCT0024",
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(total_sum),
            "concat_string": concat_str
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({
            "is_success": False,
            "error": str(e)
        }), 400

if __name__ == '__main__':
    app.run(debug=True)