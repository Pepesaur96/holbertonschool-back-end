# GENERAL TOPICS

1. What Bash scripting should not be used for:

- Heavy Computational Tasks:
  Bash scripting is not well-suited for computationally intensive tasks. It's better for managing processes, file manipulation, and interacting with the system, rather than complex calculations.
- Cross-platform GUI Applications:
  Bash is primarily a command-line language and is not suitable for developing graphical user interfaces (GUI). Other languages like Python or Java are more appropriate for this purpose.
- Large-scale Software Development:
  While Bash is excellent for scripting and automation, it's not ideal for large-scale software projects. More sophisticated languages like Python, Java, or C++ are better choices for such endeavors.
- Performance-Critical Applications:
  For applications requiring high performance and efficiency, Bash may not be the best choice. Compiled languages like C or Rust are more suitable for scenarios where every bit of performance matters.
- Complex Data Structures:
  Bash has limited support for complex data structures like arrays and associative arrays, making it less suitable for tasks that heavily rely on such structures.

2. What is an API:
   API (Application Programming Interface):

- An API is a set of rules and protocols that allows one software application to interact with another. It defines the methods and data formats that applications can use to request and exchange information. APIs are used to enable the integration of different software systems, allowing them to work together.

3. What is a REST API:
   REST API (Representational State Transfer API):

- REST is an architectural style for designing networked applications. A REST API is an interface that adheres to the principles of REST. It typically uses standard HTTP methods (GET, POST, PUT, DELETE) for communication and relies on stateless communication. REST APIs are commonly used in web development to enable communication between web servers and clients.

3. What are microservices:
   Microservices:

- Microservices is an architectural style that structures an application as a collection of small, independent services. Each service represents a specific business capability and communicates with others through well-defined APIs. Microservices architecture is known for its scalability, flexibility, and the ability to independently develop, deploy, and scale individual services.

4. What is the CSV format:
   CSV (Comma-Separated Values):

- CSV is a simple text format for representing tabular data, where each line of the file corresponds to a row, and values within each row are separated by commas (or other delimiters). It is widely used for data exchange between different applications, especially spreadsheet software.

5. What is the JSON format:
   JSON (JavaScript Object Notation):

- JSON is a lightweight data interchange format. It is easy for humans to read and write and easy for machines to parse and generate. JSON is often used to transmit data between a server and web application, as well as for configuration files and data storage.

6. Pythonic Package and Module Name Style:
   Package Names:
   Short, lowercase names.
   Avoid underscores, use simple, lowercase names.
   Module Names:
   Short, lowercase names.
   Avoid underscores, use simple, lowercase names.

7. Pythonic Class Name Style:
   Class Names:
   Use CamelCase (CapWords) convention.
   Start each word with a capital letter, without underscores.

8. Pythonic Variable Name Style:
   Variable Names:
   Use lowercase letters with underscores between words (snake_case).

9. Pythonic Function Name Style:
   Function Names:
   Use lowercase letters with underscores between words (snake_case).

10. Pythonic Constant Name Style:
    Constant Names:
    Use uppercase letters with underscores between words (CAPITALIZED_WITH_UNDERSCORES).

11. Significance of CapWords or CamelCase in Python:
    Readability and Convention:

- CapWords or CamelCase is a convention in Python for naming classes, and it helps improve readability and consistency in code.
- Following a consistent naming style makes it easier for developers to understand and collaborate on projects.

PEP 8 Compliance:

- PEP 8, the official Python style guide, recommends using CapWords for class names to maintain consistency across Python codebases.
