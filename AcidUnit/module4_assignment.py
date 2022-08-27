import sqlite3


SURVIVED_TITANIC_COUNT = """
SELECT count(survived)
FROM titanic_table
WHERE survived == 1
"""

DID_NOT_SURVIVE_TITANIC_COUNT = """
SELECT count(survived)
FROM titanic_table
WHERE survived == 0
"""

FIRST_CLASS = """
SELECT count(pclass)
From titanic_table
WHERE pclass = 1
"""

SECOND_CLASS = """
SELECT count(pclass)
From titanic_table
WHERE pclass = 2
"""

THIRD_CLASS = """
SELECT count(pclass)
From titanic_table
WHERE pclass = 3
"""

FIRST_CLASS_SURVIVED = """
SELECT count(*)
From titanic_table
WHERE pclass = 1
 AND survived = 1
"""

FIRST_CLASS_DIED = """
SELECT count(*)
From titanic_table
WHERE pclass = 1
 AND survived = 0
"""

SECOND_CLASS_SURVIVED = """
SELECT count(*)
From titanic_table
WHERE pclass = 2
 AND survived = 1
"""

SECOND_CLASS_DIED = """
SELECT count(*)
From titanic_table
WHERE pclass = 2
 AND survived = 0
"""

THIRD_CLASS_SURVIVED = """
SELECT count(*)
From titanic_table
WHERE pclass = 3
 AND survived = 1
"""

THIRD_CLASS_DIED = """
SELECT count(*)
From titanic_table
WHERE pclass = 3
 AND survived = 0
"""