let currentPage = 1;

function uploadFile() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    if (!file) {
        alert('Please select a file.');
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    // Send file to the server
    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            alert('File uploaded successfully!');
            loadAnnotations(1);
        } else {
            alert('File upload failed.');
        }
    })
    .catch(error => {
        console.error('Error uploading file:', error);
        alert('Error uploading file.');
    });
}

function loadAnnotations(page) {
    if (page < 1) return; // 無効なページ

    fetch(`/annotations?page=${page}`)
        .then(response => response.json())
        .then(data => {
            const tableBody = document.querySelector('#dataTable tbody');
            tableBody.innerHTML = '';  // 既存のテーブル行をクリア

            let rowIndex = (page - 1) * 1000;  // 行数はページごとに加算

            data.annotations.forEach(annotation => {
                rowIndex++;  // 行インデックスをインクリメント
                const row = document.createElement('tr');
                // annotation.idを使ってリンクを生成
                const detailLink = `/sentence/${annotation.id}`;

                // クエリパラメータに各項目を埋め込んでリンクを生成
                //const detailLink = `/details?sentence=${encodeURIComponent(annotation.Sentence)}&id=${annotation.id}&joy=${annotation.Writer_Joy}&sadness=${annotation.Writer_Sadness}&anticipation=${annotation.Writer_Anticipation}&surprise=${annotation.Writer_Surprise}&anger=${annotation.Writer_Anger}&fear=${annotation.Writer_Fear}&disgust=${annotation.Writer_Disgust}&trust=${annotation.Writer_Trust}&sentiment=${annotation.Writer_Sentiment}`;

                row.innerHTML = `
                    <td><a href="${detailLink}">${annotation.id}</a></td>  <!-- 行数にリンクを追加 -->
                    <td>${annotation.Sentence}</td>
                    <td>${annotation.Writer_Joy}</td>
                    <td>${annotation.Writer_Sadness}</td>
                    <td>${annotation.Writer_Anticipation}</td>
                    <td>${annotation.Writer_Surprise}</td>
                    <td>${annotation.Writer_Anger}</td>
                    <td>${annotation.Writer_Fear}</td>
                    <td>${annotation.Writer_Disgust}</td>
                    <td>${annotation.Writer_Trust}</td>
                    <td>${annotation.Writer_Sentiment}</td>
                `;
                tableBody.appendChild(row);
            });

            // ページ情報とボタンの状態を更新
            currentPage = data.current_page;
            document.getElementById('pageInfoTop').innerText = `ページ ${currentPage} / ${data.pages}`;
            document.getElementById('pageInfoBottom').innerText = `ページ ${currentPage} / ${data.pages}`;
            document.getElementById('prevBtnTop').disabled = !data.has_prev;
            document.getElementById('nextBtnTop').disabled = !data.has_next;
            document.getElementById('prevBtnBottom').disabled = !data.has_prev;
            document.getElementById('nextBtnBottom').disabled = !data.has_next;
        })
        .catch(error => {
            console.error('Error fetching annotations:', error);
        });
}

// ページ変更を処理する関数
function changePage(page) {
    loadAnnotations(page);  // 新しいページを読み込む
}

// 最初の読み込み
loadAnnotations(currentPage);
