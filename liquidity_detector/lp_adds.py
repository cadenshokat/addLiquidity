import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def helius_webhook():
    try:
        data = request.get_json(force=True)
        for d in data:
            if d.get('type') == "ADD_LIQUIDITY":
                print("Received data from Helius webhook:")
                print(f"ID: {d.get('signature')}")
                print(data)
        return jsonify({'status': 'success'}), 200
    except Exception as e:
        print("Error processing webhook:", e)
        return jsonify({'status': 'error', 'message': str(e)}), 400

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 3001))
    app.run(host='0.0.0.0', port=port, debug=True)
