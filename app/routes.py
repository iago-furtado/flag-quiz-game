from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.database import db
from app.models import Game, Team, Score
from datetime import datetime

#from app.models import Test

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/start-game', methods=['POST'])
def start_game():
    # Capturar os dados do formulário
    num_teams = int(request.form['numTeams'])
    difficulty = request.form['difficulty']
    
    # Criar um novo jogo
    new_game = Game(start_time=datetime.utcnow(), difficulty=difficulty)
    db.session.add(new_game)
    db.session.commit()

    # Adicionar times ao jogo
    for i in range(1, num_teams + 1):
        team_name = request.form[f'team{i}Name']
        team_color = request.form[f'team{i}Color']
        new_team = Team(game_id=new_game.id, name=team_name, color=team_color)
        db.session.add(new_team)
        db.session.commit()  # Commitar após adicionar o time para garantir que o ID do time esteja disponível

        # Adicionar um registro de score inicial com 0 pontos
        new_score = Score(game_id=new_game.id, team_id=new_team.id, score=0)
        db.session.add(new_score)
    
    db.session.commit()

    # Redirecionar para a página do jogo
    return redirect(url_for('main.game', game_id=new_game.id))



@main.route('/game/<int:game_id>')
def game(game_id):
    game = Game.query.get_or_404(game_id)  # Obtém o jogo pelo ID
    teams = Team.query.filter_by(game_id=game_id).all() # Obtém os times associados ao jogo
    return render_template('game.html', game=game, teams=teams)


@main.route('/save-game-results', methods=['POST'])
def save_game_results():
    data = request.json
    scores = data.get('scores', [])
    game_id = data.get('gameId')

    try:
        # Limpar scores antigos
        Score.query.filter_by(game_id=game_id).delete()

        # Salva os scores no banco de dados
        for score_data in scores:
            team_id = score_data['teamId']
            points = score_data['points']
            
            # Adicionar ou atualizar o score
            score = Score.query.filter_by(team_id=team_id, game_id=game_id).first()
            if score:
                score.score = points
            else:
                score = Score(game_id=game_id, team_id=team_id, score=points)
                db.session.add(score)
        
        db.session.commit()

        # Encontrar o time vencedor
        winning_team = Team.query.join(Score).filter_by(game_id=game_id).group_by(Team.id).order_by(db.func.sum(Score.score).desc()).first()

        return jsonify({'message': 'Scores saved successfully!', 'winningTeam': winning_team.name if winning_team else 'Nenhum time'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 500


'''
Test to database connection

@main.route('/test_db')
def test_db():
    try:
        # Testa se a conexão ao banco de dados está funcionando
        db.create_all()  # Cria as tabelas se não existirem
        test_entry = Test(name="Test")
        db.session.add(test_entry)
        db.session.commit()
        return jsonify({'message': 'Database connection is working!'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500
'''