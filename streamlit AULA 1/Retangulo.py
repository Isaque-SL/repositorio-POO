import streamlit as st
import math

class Retangulo:
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def calc_area(self):
        return self.b * self.h
    
    def calc_diagonal(self):
        return math.sqrt((self.b ** 2) + (self.h ** 2))
    
    def ToString(self):
        return f"Base: {self.b} - Altura: {self.h} - Área: {self.calc_area()} - Diagonal: {self.calc_diagonal()}"
    