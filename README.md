# Flag Quiz Game

## Overview

The **Flag Quiz Game** is an interactive web application that allows users to compete in a quiz game about country flags. The application supports team formation, allows color selection for each team, and enables the selection of difficulty levels (Easy, Medium, Hard). The primary goal is to provide a simple yet robust platform that also serves as a case study for data engineering.

## Project Objective

The main focus of this project is to develop and apply data engineering concepts using a MySQL relational database hosted on AWS. The application captures and stores relevant data about the games, such as:

- **Number of games** played
- **Scores** for each team
- **Team details**: names, colors, and location
- **Difficulty level** selected for each game
- **Performance history** of each team

These data are stored in a well-structured database, allowing for efficient queries and detailed analyses, which can provide insights into user performance and game behavior over time.

## Database Structure

The application uses a relational database structure. The main tables include:

- **Teams**: Stores information about each team, such as name, color, and location.
- **Games**: Contains data about each game, including the number of teams, difficulty level, and the date and time of the game.
- **Scores**: Records each team's score in each game, allowing for performance tracking over time.

## Technologies Used

- **Flask**: Used as the web framework to create the backend application.
- **MySQL (AWS RDS)**: Relational database used to store game data.
- **SQLAlchemy**: ORM used to interact with the MySQL database more efficiently and with less SQL code.
- **Bootstrap**: Used to create a responsive and stylized user interface.
- **JavaScript**: Used to dynamically manipulate the user interface and enhance the user experience.

## Data Engineering

### Data Modeling

Data modeling was carried out with a focus on efficiency and scalability. The choice of MySQL as a relational database was due to its robustness and compatibility with various data analysis tools. The use of relationships between tables allows for efficient data management and facilitates insight extraction.

### Data Storage and Processing

The data generated during the games are stored in specific tables and organized in a way that allows post-game analysis. This makes it possible to create dashboards and reports that highlight, for example, the best-performing teams, accuracy patterns at different difficulty levels, and other important metrics.

### Security and Management

To protect credentials and sensitive data, database connection information is managed through environment variables, and access to the database is controlled through best security practices.

## Next Steps

- **ETL Implementation**: Automate data extraction, transformation, and loading to enable more advanced analyses.
- **Data Visualization**: Create dashboards that allow real-time visualization of team performance.
- **Machine Learning**: Explore the possibility of using machine learning techniques to predict team performance based on historical data.

## Conclusion

This project not only offers a functional web application but also serves as a platform for developing and demonstrating data engineering skills. The integration with AWS and the use of advanced data modeling and storage practices make this project a valuable case study for those looking to specialize in the field.
