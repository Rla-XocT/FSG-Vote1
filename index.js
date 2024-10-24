const functions = require('firebase-functions');
const express = require('express');
const cors = require('cors');

// Express 앱 초기화
const app = express();

// CORS 설정 (모든 출처 허용)
app.use(cors({ origin: true }));

// JSON 바디 파서 추가
app.use(express.json());

// 투표 결과를 저장할 객체
const votes = { A: 0, B: 0, C: 0 };

// 투표 받기
app.post('/vote', (req, res) => {
  const team = req.body.team;
  if (team in votes) {
    votes[team] += 1;
    res.status(200).json({ message: '투표가 성공적으로 등록되었습니다.', votes });
  } else {
    res.status(400).json({ error: '잘못된 팀 이름입니다.' });
  }
});

// 결과 반환
app.get('/results', (req, res) => {
  res.json(votes);
});

// Firebase Function으로 exports
exports.api = functions.https.onRequest(app);
