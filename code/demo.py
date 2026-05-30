
# File: demo.py
# Description: This file runs the actual Streamlit dashboard.
#              It imports our classes from code.py,
#              creates a SalesDashboard object, and calls render().
#
# Run this file with:
#   streamlit run demo.py


import pandas as pd
from code import SalesDashboard
# we import our own class from code.py
# both files must be in the same folder



# SAMPLE DATA
# (12 months of sales figures for the demo)


data = pd.DataFrame({
    "sales": [
        150000, 230000, 180000, 290000, 310000, 270000,
        380000, 410000, 360000, 490000, 520000, 480000
    ],
    "month": [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]
})

data = data.set_index("month")



# CREATE OBJECT


# OBJECT
# app is a real instance (object) created from SalesDashboard class
# SalesDashboard is the blueprint, app is the actual thing
# INHERITANCE - app also has all methods from StreamlitApp automatically
app = SalesDashboard(
    title = "Monthly Sales Dashboard",
    data  = data
)

# ABSTRACTION
# we just call render() - one line
# everything else happens automatically inside the class
app.render()