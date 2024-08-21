document.addEventListener('DOMContentLoaded', function() {
    // Adicionar e diminuir pontos dos times
    document.addEventListener('click', function(event) {
        if (event.target && event.target.matches('.btn-add-points')) {
            const teamId = event.target.dataset.teamId;
            updateScore(teamId, 1);
        } else if (event.target && event.target.matches('.btn-remove-points')) {
            const teamId = event.target.dataset.teamId;
            updateScore(teamId, -1);
        } else if (event.target && event.target.matches('#toggle-flag-name')) {
            const flagNameElement = document.getElementById('flag-name');
            if (flagNameElement) {
                flagNameElement.classList.toggle('d-none');
                event.target.textContent = flagNameElement.classList.contains('d-none') ? 'Mostrar Nome' : 'Esconder Nome';
            }
        } else if (event.target && event.target.matches('#end-game-btn')) {
            saveGameResults();
        }
    });

    function updateScore(teamId, delta) {
        const scoreElement = document.getElementById(`score-${teamId}`);
        if (scoreElement) {
            let currentScore = parseInt(scoreElement.textContent, 10);
            currentScore = Math.max(0, currentScore + delta);
            scoreElement.textContent = currentScore;
        }
    }

    function saveGameResults() {
        const scores = Array.from(document.querySelectorAll('.score')).map(scoreElement => ({
            teamId: scoreElement.id.split('-')[1],
            points: parseInt(scoreElement.textContent, 10)
        }));

        fetch('/save-game-results', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                scores: scores,
                gameId: document.querySelector('meta[name="game-id"]').content
            })
        })
        .then(response => response.json())
        .then(data => {
            alert(`O time vencedor é: ${data.winningTeam}`);
            window.location.href = '/'; // Redirecionar para a tela inicial
        })
        .catch(error => {
            console.error('Error saving game results:', error);
        });
    }
});
