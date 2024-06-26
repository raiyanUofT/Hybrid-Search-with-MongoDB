from mongodb_client import get_mongodb_client

# Connect to MongoDB
client = get_mongodb_client()

# Create or connect to a database
db = client['sampledb']

# Create or connect to a collection
collection = db['samplecollection']

# Sample data: 20 examples of book names and descriptions
documents = [
    {"title": "Introduction to Algorithms", "content": "A comprehensive guide to modern algorithm design and analysis."},
    {"title": "Artificial Intelligence: A Modern Approach", "content": "An extensive overview of the principles and techniques of artificial intelligence."},
    {"title": "Deep Learning", "content": "A detailed exploration of deep learning techniques and their applications."},
    {"title": "Machine Learning: A Probabilistic Perspective", "content": "A comprehensive introduction to the concepts and techniques of machine learning."},
    {"title": "Computer Networks", "content": "An in-depth look at the principles and practices of computer networking."},
    {"title": "Database System Concepts", "content": "A detailed examination of database systems, including design and implementation."},
    {"title": "Operating System Concepts", "content": "An overview of the principles and practices of operating system design."},
    {"title": "The Elements of Statistical Learning", "content": "A comprehensive introduction to statistical learning and data mining techniques."},
    {"title": "Pattern Recognition and Machine Learning", "content": "An exploration of pattern recognition and machine learning techniques."},
    {"title": "Computer Vision: Algorithms and Applications", "content": "A detailed look at computer vision algorithms and their practical applications."},
    {"title": "Data Mining: Concepts and Techniques", "content": "An introduction to data mining techniques and their applications."},
    {"title": "Introduction to Information Retrieval", "content": "A comprehensive guide to the principles and techniques of information retrieval."},
    {"title": "Principles of Compiler Design", "content": "An in-depth look at the principles of compiler design and implementation."},
    {"title": "Cryptography and Network Security", "content": "An exploration of cryptographic techniques and their applications in network security."},
    {"title": "Discrete Mathematics and Its Applications", "content": "A detailed introduction to discrete mathematics and its applications in computer science."},
    {"title": "Software Engineering: A Practitioner's Approach", "content": "An overview of the principles and practices of software engineering."},
    {"title": "Computer Graphics: Principles and Practice", "content": "A comprehensive guide to the principles and techniques of computer graphics."},
    {"title": "Parallel Programming: Techniques and Applications", "content": "An introduction to parallel programming techniques and their practical applications."},
    {"title": "Principles of Distributed Database Systems", "content": "A detailed look at the principles and practices of distributed database systems."},
    {"title": "Human-Computer Interaction", "content": "An exploration of the principles and practices of human-computer interaction."}
]
# Insert sample data
collection.insert_many(documents)

print("Sample data inserted into MongoDB.")
