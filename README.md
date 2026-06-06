# OOP Final Term Project

### Object-Oriented Analysis of the Streamlit Library

---

## 👥 Group Members

| # | Name         | Roll Number |
| - | ------------ | ----------- |
| 1 | Abdul Qudoos | 2046        |
| 2 | Ali Hassan   | 2065        |
| 3 | Ahmed Hassan | 2062        |

---

## 📚 Library Chosen — Streamlit

**Streamlit** is an open-source Python library that allows developers and data scientists to build interactive web applications entirely in Python without writing HTML, CSS, or JavaScript. It is widely used for creating dashboards, data visualization tools, machine learning applications, and interactive web interfaces quickly and efficiently.

### 🎥 Project Presentation & Demonstration Video

A complete presentation and demonstration of this project is available on YouTube:

**Video Link:** https://youtu.be/7KRZEcELH3k

The video covers:

* Introduction to Streamlit
* Internal Architecture of Streamlit
* Object-Oriented Analysis
* OOP Principles Implementation
* Source Code Walkthrough
* Monthly Sales Dashboard Demonstration
* Project Conclusion

| Detail             | Info                                           |
| ------------------ | ---------------------------------------------- |
| **Created by**     | Adrien Treuille, Amanda Kelly, Thiago Teixeira |
| **First Released** | October 2019                                   |
| **Maintained by**  | Snowflake Inc. (acquired 2022)                 |
| **Install**        | `pip install streamlit`                        |

---

## 📋 Project Description

This project performs a complete Object-Oriented Analysis of the Streamlit Python library. The project examines Streamlit’s internal class structure and architecture to understand how object-oriented concepts are used in a real-world software library.

To demonstrate these concepts practically, we developed a custom Monthly Sales Dashboard using Streamlit and implemented all four major Object-Oriented Programming principles.

| Principle            | How We Applied It                                                                                                 |
| -------------------- | ----------------------------------------------------------------------------------------------------------------- |
| 🔒 **Encapsulation** | Private variables `_title`, `_data`, and `_generator` are hidden inside classes and accessed through methods.     |
| 🧬 **Inheritance**   | `SalesDashboard` inherits from `StreamlitApp`, while `StreamlitApp` inherits from `ABC`.                          |
| 🔄 **Polymorphism**  | Methods such as `render()` and `render_header()` are overridden in derived classes to provide different behavior. |
| 🎭 **Abstraction**   | The `@abstractmethod` decorator ensures that all child classes implement the required `render()` method.          |

---

## 🎯 Project Objectives

* Analyze the object-oriented architecture of Streamlit.
* Identify classes and relationships used within the library.
* Demonstrate Encapsulation, Inheritance, Polymorphism, and Abstraction.
* Develop a practical dashboard application using Streamlit.
* Understand how OOP principles are applied in modern Python libraries.

---

## ▶️ How to Run

```bash
pip install streamlit pandas
streamlit run code.py
```

The application will automatically open in your browser at:

```text
http://localhost:8501
```

---

## ✅ Conclusion

This project successfully demonstrates how the Streamlit library utilizes Object-Oriented Programming concepts in its architecture. Through the development of a Monthly Sales Dashboard, we applied Encapsulation, Inheritance, Polymorphism, and Abstraction in a practical environment. The project helped us understand both the internal design of Streamlit and the real-world application of OOP principles in software development.

---

## 🔗 References

1. Streamlit Official Documentation – https://docs.streamlit.io
2. Streamlit GitHub Repository – https://github.com/streamlit/streamlit
3. Project Presentation Video – https://youtu.be/7KRZEcELH3k
4. Python Official Documentation – https://docs.python.org/3/

2. [Streamlit GitHub Repository](https://github.com/streamlit/streamlit)
3. [Python ABC Module](https://docs.python.org/3/library/abc.html)
4. [Streamlit DeltaGenerator Source Code](https://github.com/streamlit/streamlit/blob/develop/lib/streamlit/delta_generator.py)
5. [Dash by Plotly Documentation](https://dash.plotly.com)
6. [Python OOP Documentation](https://docs.python.org/3/tutorial/classes.html)
7. [Snowflake Acquires Streamlit (2022)](https://www.snowflake.com/blog/snowflake-to-acquire-streamlit)
