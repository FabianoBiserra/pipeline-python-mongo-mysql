# Data Pipeline Project

## Description
This project implements a robust data pipeline that extracts data from different APIs, transforms it using Python, and loads it into a MongoDB and MySQL database. It is designed for scalability, reliability, and ease of use in data engineering workflows.

## Features
- Extract data from different APIs and convert it into CVS files
- Transform data using pandas
- Load transformed data into MongoDB collections and MySQL tables each for different proposes
- Modular and reusable codebase
- Logging and error handling

## Technologies Used
| Technology | Purpose |
|------------|---------|
| Python     | Core programming language |
| MongoDB    | Target NoSQL database |
| MySQL      | Target relational database |
| Pandas     | Data manipulation and transformation |

## Getting Started
1. Clone the repository
2. Install dependencies using `pip install -r requirements.txt`
3. Configure MongoDB and MySQL credentials in `config.py`
4. Run the pipeline using `python main.py`

## Workflow
### MongoDB Setup
- Install MongoDB and start the service
- Create a database and insert sample collections

### MySQL Setup
- Install MySQL and start the service
- Create target database and tables

### Data Extraction
- Connect to MongoDB using pymongo
- Read collections into pandas DataFrames

### Data Transformation
- Clean and normalize data
- Apply business logic and formatting

### Data Loading
- Connect to MySQL using SQLAlchemy
- Insert transformed data into target tables

## Example Output
After running the pipeline, the MySQL database will contain cleaned and structured data from MongoDB. Example:
```
+----+------------+-----------+
| ID | Name       | Timestamp |
+----+------------+-----------+
| 1  | Alice      | 2023-08-01|
| 2  | Bob        | 2023-08-02|
+----+------------+-----------+
```

## Project Structure
```
├── config.py
├── extract.py
├── transform.py
├── load.py
├── main.py
├── requirements.txt
└── README.txt
```

## Future Enhancements
- Add support for cloud databases
- Implement data validation and schema enforcement
- Schedule pipeline with Apache Airflow

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License.
