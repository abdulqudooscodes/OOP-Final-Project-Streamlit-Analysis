# OOP Final Term Project
### Object-Oriented Analysis of the Streamlit Library

---

## 👥 Group Members

| # | Name | Roll Number |
|:---:|:---|:---|
| 1 | Abdul Qudoos | 2046 |
| 2 | Ali Hassan | 2065 |
| 3 | Ahmed Hassan | 2062 |

---

## 📚 Library Chosen — Streamlit

**Streamlit** is an open-source Python library that allows developers and data scientists to build interactive web applications entirely in Python — without writing any HTML, CSS, or JavaScript.

| Detail | Info |
|---|---|
| **Created by** | Adrien Treuille, Amanda Kelly, Thiago Teixeira |
| **First Released** | October 2019 |
| **Maintained by** | Snowflake Inc. (acquired 2022) |
| **Install** | `pip install streamlit` |

---

## 📋 Project Description

This project performs a complete **Object-Oriented Analysis of the Streamlit Python library**. We studied Streamlit's internal class architecture and built a custom **Monthly Sales Dashboard** to demonstrate all four OOP principles in a real working application.

| Principle | How We Applied It |
|---|---|
| 🔒 **Encapsulation** | Private variables `_title`, `_data`, `_generator` hidden inside classes |
| 🧬 **Inheritance** | `SalesDashboard` inherits from `StreamlitApp`, which inherits from `ABC` |
| 🔄 **Polymorphism** | `render()` and `render_header()` overridden with different behavior in child class |
| 🎭 **Abstraction** | `@abstractmethod` forces all child classes to implement `render()` |

---

## ▶️ How to Run

```bash
pip install streamlit pandas
streamlit run code.py
```

App opens in browser at: `http://localhost:8501`

---

## 🔗 References

1. [Streamlit Official Documentation](https://docs.streamlit.io)
2. [Streamlit GitHub Repository](https://github.com/streamlit/streamlit)
3. [Python ABC Module](https://docs.python.org/3/library/abc.html)
4. [Streamlit DeltaGenerator Source Code](https://github.com/streamlit/streamlit/blob/develop/lib/streamlit/delta_generator.py)
5. [Dash by Plotly Documentation](https://dash.plotly.com)
6. [Python OOP Documentation](https://docs.python.org/3/tutorial/classes.html)
7. [Snowflake Acquires Streamlit (2022)](https://www.snowflake.com/blog/snowflake-to-acquire-streamlit)
