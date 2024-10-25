// AJAXリクエストでデータを取得
const sentenceId = document.getElementById('sentence_id').textContent.trim(); // sentence_idのIDを持つ要素から値を取得
fetch(`/api/sentence/${sentenceId}`)
    .then(response => response.json())
    .then(data => {
        // デバッグ用に全データを表示
        console.log(data);
        
        // レーダーチャートの作成
        createRadarChart(data);
    })
    .catch(error => console.error('Error:', error));

// レーダーチャートを作成する関数
function createRadarChart(data) {
    const ctx = document.getElementById('radarChart').getContext('2d');

    // 感情の値を取得
    const chartData = {
        labels: ['喜び', '悲しみ', '期待', '驚き', '怒り', '恐れ', '嫌悪', '信頼'],
        datasets: [{
            label: '感情の強度',
            data: [
                data.avg_readers_joy,
                data.avg_readers_sadness,
                data.avg_readers_anticipation,
                data.avg_readers_surprise,
                data.avg_readers_anger,
                data.avg_readers_fear,
                data.avg_readers_disgust,
                data.avg_readers_trust
            ],
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 1
        }]
    };

    const config = {
        type: 'radar',
        data: chartData, // 修正したデータ変数をここに使用
        options: {
            responsive: false,
            scales: {
                r: {
                    beginAtZero: true,
                    min: -1,             // スケールの最小値を0に固定
                    max: 3,             // スケールの最大値を4に固定
                    ticks: {
                        stepSize: 1,      // 目盛りのステップサイズを1に設定
                        callback: function(value) {
                            // 原点の値（最小値）を非表示にする
                            return value === -1 ? '' : value;
                        }
                    },
                    pointLabels: {
                        color: 'red'
                    }
                }
            }
        }
    };

    new Chart(ctx, config);
}