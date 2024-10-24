const sentiment = parseFloat(document.getElementById('sentiment').textContent.trim());
const joy = parseFloat(document.getElementById('joy').textContent.trim());
const sadness = parseFloat(document.getElementById('sadness').textContent.trim());
const anticipation = parseFloat(document.getElementById('anticipation').textContent.trim());
const surprise = parseFloat(document.getElementById('surprise').textContent.trim());
const anger = parseFloat(document.getElementById('anger').textContent.trim());
const fear = parseFloat(document.getElementById('fear').textContent.trim());
const disgust = parseFloat(document.getElementById('disgust').textContent.trim());
const trust = parseFloat(document.getElementById('trust').textContent.trim());

// レーダーチャートを作成する関数
function createRadarChart() {
    const ctx = document.getElementById('radarChart').getContext('2d');

    // 現在の文に対応する感情の値を取得
    const data = {
        labels: ['喜び', '悲しみ', '期待', '驚き', '怒り', '恐れ', '嫌悪', '信頼'],
        datasets: [{
            label: '感情の強度',
            data: [
                joy,
                sadness,
                anticipation,
                surprise,
                anger,
                fear,
                disgust,
                trust
            ],
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 1
        }]
    };

    const config = {
        type: 'radar',
        data: data,
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

    radarChartInstance = new Chart(ctx, config);
}

createRadarChart()