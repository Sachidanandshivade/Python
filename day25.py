import day24 as a

print(a.s1.marks)  # Output: 30
print(a.s2.marks)  # Output: 50
print(a.s1 + a.s2)  # Output: 80
print(a.s1)  # Output: <__main__.Student object at 0x...>


# 1. User-Defined ModulesThese are custom Python files (.py) created by you or your team.Example: A file named math_module.py containing custom arithmetic functions:Python# math_module.py
# def add(a, b):
#     return a + b
# Usage:Pythonimport math_module

# print(math_module.add(10, 20))
# 2. Built-in / Standard Library ModulesPython comes with a rich set of 
# built-in modules pre-installed out of the box.Commonly Used Standard ModulesCategoryModulesPurpose
# Mathematics & Numbers math, random, statistics, decimal, fractionsMath constants/functions, random number generation, statistical calculations.
# Date & Timedatetime, time, calendarHandling dates, timestamps, delays, and calendar layouts.
# File & OS Operationsos, sys, shutil, pathlibOperating system interactions, command-line arguments, file system management.
# Data Formats & Parsingjson, csv, xml, re (Regex)Working with JSON/CSV data and regular expressions for text searching.
# Data Structures & Utilitiescollections, itertools, functoolsAdvanced data types (Counter, defaultdict), iterators, and higher-order functions.
# Networking & Weburllib, http, socketMaking HTTP requests and low-level network communication.
# Threading & Concurrencythreading, multiprocessing, asyncioParallel execution and asynchronous programming.
# 
# 3. Third-Party ModulesThese are external packages created by the Python community. 
# They must be installed using a package manager like pip before importing.
# Popular Third-Party PackagesData Science & Machine Learning:
#  numpy, pandas, matplotlib, scikit-learn, torch, tensorflow
# Web Development: django, flask, fastapiWeb Scraping & HTTP Requests: requests, beautifulsoup4, scrapyAutomation & Utilities: pillow (image processing), pytest (testing)
# Abstraction is the process of hiding implementation details and showing only the essential features to the user
# Car, Tv
# Using : ABC (abstract class) , abstract methods (ABC - obj cannot be created)
# Why we need to make abstract methods in abstract class?
from abc import ABC, abstractmethod

class Vechile(ABC):
    # methods that as a body (concrete/normal methods)
    # methods that doesnot have a body (abstract methods) - @abstractmethod
    @abstractmethod
    def start(self):
        pass

    def stop(self):
        print("Vechile manually stops")

class Car(Vechile):
    # Override
    def start(self):
        print("Car Automatically starts")

    def stop(self):
        print("Car automatically stops")

# v = Vechile()
# v.start()
# v.stop()
c = Car()
c.start()
c.stop()