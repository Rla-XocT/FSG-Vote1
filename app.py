from flask import Flask, request, jsonify
from collections import defaultdict
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

# 투표 결과를 저장할 딕셔너리, 기본값을 0으로 설정
votes = defaultdict(int)

@app.route('/vote', methods=['POST'])
def vote():
    """
    팀 투표를 처리하는 함수입니다.
    POST 요청으로 팀 이름을 받아 투표 결과를 업데이트합니다.
    """
    data = request.get_json()
    team = data.get('team')
    if team in ['A', 'B', 'C']:
        votes[team] += 1
        return jsonify({"message": "투표가 성공적으로 등록되었습니다.", "votes": dict(votes)}), 200
    else:
        return jsonify({"error": "잘못된 팀 이름입니다."}), 400

@app.route('/results', methods=['GET'])
def results():
    """
    현재까지의 투표 결과를 JSON 형식으로 반환하는 함수입니다.
    """
    return jsonify(dict(votes))

if __name__ == '__main__':
    app.run(debug=True)
