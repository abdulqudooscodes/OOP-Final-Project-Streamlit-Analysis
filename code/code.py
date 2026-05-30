# OOP Final Project - Streamlit Library Analysis


# Description: This file contains our two custom classes.
#              StreamlitApp is the abstract parent class.
#              SalesDashboard is the child class that inherits from it.
#           We use OOP concepts like inheritance, polymorphism, encapsulation, and abstraction

import streamlit as st
import pandas as pd
from abc import ABC, abstractmethod
from streamlit.delta_generator import DeltaGenerator
# DeltaGenerator is the core class inside the Streamlit library
# We imported it directly to use it inside our SalesDashboard class


# BASE CLASS - StreamlitApp
# This is an abstract class - it cannot be used directly
# It can only be used through a child class (inheritance)
#
# OOP Concepts here:
#   - ABSTRACTION   : render() is declared but left empty on purpose
#   - ENCAPSULATION : title is stored privately inside the object

class StreamlitApp(ABC):

    def __init__(self, title: str):
        # ENCAPSULATION
        # title is stored inside the object
        # it cannot be changed directly from outside the class
        self._title = title

    def render_header(self):
        # displays the app title at the top of the page
        # child class can override this method to change behavior
        st.title(self._title)

    @abstractmethod
    def render(self):
        # ABSTRACTION
        # this method is intentionally left empty
        # every child class is FORCED to write its own render()
        # if a child class skips this, Python will throw an error
        pass


# CHILD CLASS - SalesDashboard
# This class inherits everything from StreamlitApp
#
# OOP Concepts here:
#   - INHERITANCE   : SalesDashboard(StreamlitApp) gets all parent methods
#   - POLYMORPHISM  : render_header() and render() are overridden here
#   - ABSTRACTION   : user just calls render(), complexity is hidden inside


class SalesDashboard(StreamlitApp):

    def __init__(self, title: str, data: pd.DataFrame):
        # calling parent constructor first so _title gets set
        super().__init__(title)

        # ENCAPSULATION
        # data is stored privately - only class methods can use it
        self._data = data

        # using DeltaGenerator directly from Streamlit library
        # this is composition - we are using a library class inside ours
        self._generator: DeltaGenerator = st._main

    def render_header(self):
        # POLYMORPHISM
        # parent render_header() only showed the title
        # we overrode it to show title + a welcome message
        # same method name, different and extended behavior
        super().render_header()
        st.caption("Clothes Online Store — Being Human Store")
        st.markdown("---")

    def render_metrics(self):
        # new method - does not exist in parent class
        # shows three summary cards: total, average, highest sales
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Sales",   f"Pkr = {self._data['sales'].sum():,.0f}")
        col2.metric("Average Sale",  f"Pkr = {self._data['sales'].mean():,.0f}")
        col3.metric("Highest Sale",  f"Pkr = {self._data['sales'].max():,.0f}")

    def render_chart(self):
        # new method - not in parent class
        # uses self._generator (DeltaGenerator) to draw the line chart
        # DeltaGenerator is Streamlit's core class - imported at the top
        st.subheader("Monthly Sales Chart")
        self._generator.line_chart(self._data)

    def render_table(self):
        # new method - shows the full data table below the chart
        # again using DeltaGenerator directly through self._generator
        st.subheader("Sales Data Table")
        self._generator.dataframe(self._data, use_container_width=True)

    def render(self):
        # POLYMORPHISM
        # parent had an empty abstract render()
        # we gave it full functionality here
        # same method name, completely different behavior
        #
        # ABSTRACTION
        # whoever uses this class just calls render()
        # they do not need to know what is happening inside
        self.render_header()
        self.render_metrics()
        self.render_chart()
        self.render_table()