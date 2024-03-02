from db_functions import get_engine

def create_tables(engine):
    # Define schema for each table
    players_schema = """
    CREATE TABLE IF NOT EXISTS Players (
        player_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        team_id INT,
        position VARCHAR(255),
        FOREIGN KEY (team_id) REFERENCES Teams(team_id)
    );
    """

    teams_schema = """
    CREATE TABLE IF NOT EXISTS Teams (
        team_id INT AUTO_INCREMENT PRIMARY KEY,
        team_name VARCHAR(255) NOT NULL,
        city VARCHAR(255), 
        stadium_location DOUBLE
    );
    """

    games_schema = """
    CREATE TABLE IF NOT EXISTS Games (
        game_id INT AUTO_INCREMENT PRIMARY KEY,
        date DATE NOT NULL,
        home_team_id INT,
        away_team_id INT,
        FOREIGN KEY (home_team_id) REFERENCES Teams(team_id),
        FOREIGN KEY (away_team_id) REFERENCES Teams(team_id)
    );
    """

    player_game_stats_schema = """
    CREATE TABLE IF NOT EXISTS PlayerGameStats (
        player_game_stats_id INT AUTO_INCREMENT PRIMARY KEY,
        player_id INT,
        game_id INT,
        is_home BOOLEAN,
        projected_points FLOAT,
        actual_points FLOAT,
        dfs_salary FLOAT,
        FOREIGN KEY (player_id) REFERENCES Players(player_id),
        FOREIGN KEY (game_id) REFERENCES Games(game_id)
    );
    """

    traditional_stats_hitters_schema = """
    CREATE TABLE IF NOT EXISTS TraditionalStatsHitters (
        stats_id INT AUTO_INCREMENT PRIMARY KEY,
        player_game_stats_id INT,
        HR INT,
        RBI INT,
        SB INT,
        FOREIGN KEY (player_game_stats_id) REFERENCES PlayerGameStats(player_game_stats_id)
    );
    """

    traditional_stats_pitchers_schema = """
    CREATE TABLE IF NOT EXISTS TraditionalStatsPitchers (
        stats_id INT AUTO_INCREMENT PRIMARY KEY,
        player_game_stats_id INT,
        W INT,
        SO INT,
        ERA FLOAT,
        FOREIGN KEY (player_game_stats_id) REFERENCES PlayerGameStats(player_game_stats_id)
    );
    """

    # Execute schema creation SQL statements
    with engine.connect() as conn:
        conn.execute(players_schema)
        conn.execute(teams_schema)
        conn.execute(games_schema)
        conn.execute(player_game_stats_schema)
        conn.execute(traditional_stats_hitters_schema)
        conn.execute(traditional_stats_pitchers_schema)

def main():
    # Create a SQLAlchemy engine
    engine = get_engine()
    
    # Call the function to create tables
    create_tables(engine)

if __name__ == "__main__":
    main()

