document.addEventListener('DOMContentLoaded', function() {
    const numTeamsSelect = document.getElementById('numTeams');
    const teamsDiv = document.getElementById('teams');

    numTeamsSelect.addEventListener('change', function() {
        teamsDiv.innerHTML = '';
        const numTeams = parseInt(this.value);

        for (let i = 1; i <= numTeams; i++) {
            teamsDiv.innerHTML += `
                <div class="mb-3">
                    <label for="team${i}Name" class="form-label">Nome do Time ${i}</label>
                    <input type="text" class="form-control" id="team${i}Name" name="team${i}Name" placeholder="Nome do Time ${i}" required>
                </div>
                <div class="mb-3">
                    <label for="team${i}Color" class="form-label">Cor do Time ${i}</label>
                    <input type="color" class="form-control form-control-color" id="team${i}Color" name="team${i}Color" value="#000000" required>
                </div>
            `;
        }
    });
});


