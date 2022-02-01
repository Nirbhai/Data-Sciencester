#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""



Author	: Nirbhai Singh
E-Mail	: chittamor@gmail.com


*********************************

Run below commands to verify you are in correct environment and branch:
    !conda info -e
    !git branch -a

*********************************


"""

from typing import Tuple, List, Sequence, Any, Dict, Iterator, Callable
from collections import defaultdict

# some type aliases for later use
Row = Dict[str, Any]                            # A database row
WhereClause = Callable[[Row], bool]             # Predicate for a single row
HavingClause = Callable[[list[Row]], bool]      # Predicate for multiple rows

class Table:
    def __init__(self, columns: List[str], types: List[type]) -> None:
        assert len(columns) == len(types), "# of columns must == # of types"
        
        self.columns = columns              # Names of columns
        self.types = types                  # Data types of columns
        self.rows: List[Row] = []           # no data yet, so empty list of rows
    
    def col_to_type(self, col: str) -> type:
        idx = self.columns.index(col)           # Find the index of column
        return self.types[idx]                  # return its type
    
    def insert(self, values: list) -> None:
        # check for right # of values
        if(len(values) != len(self.types)):
            raise ValueError(f"You need to provide {len(self.types)} values")
        # check for right type of values
        for value, typ in zip(values, self.types):
            if not (isinstance(value, typ) and value is not None):
                raise TypeError(f"Expected type {typ} but got {value}")
        # add the corresponding dict as row
        self.rows.append(dict(zip(self.columns, values)))
    
    def __getitem__(self, idx: int) -> Row:
        return self.rows[idx]
    
    def __iter__(self) -> Iterator[Row]:
        return iter(self.rows)
    
    def __len__(self) -> int:
        return len(self.rows)
    
    def __repr__(self) -> str:
        """a representation of the table: first columns then rows"""
        rows = "\n".join(str(row) for row in self.rows)
        return f"{self.columns}\n{rows}"
    
    def update(self,
               updates: Dict[str, Any],
               predicate: WhereClause = lambda row: True) -> None:
        # first we need to make sure updates have valid names and types
        for column, new_value in updates.items():
            if column not in self.columns:
                raise ValueError(f"invalid column: {column}")
            typ = self.col_to_type(column)
            if not (isinstance(new_value, typ) and new_value is not None):
                raise TypeError(f"Expected type {typ} but got {new_value}")
        
        # if all good, then we add
        # notice the smart use of lambda fxn here
        for row in self.rows:
            if predicate(row):
                for column, new_value in updates.items():
                    row[column] = new_value




# constructor requires column names and types
users = Table(['user_id', 'name', 'num_friends'], [int, str, int])
users.insert([0,  "Hero",  0])
users.insert([1,  "Dunn",  2])
users.insert([2,  "Sue",   3])
users.insert([3,  "Chi",   3])
users.insert([4,  "Thor",  3])
users.insert([5,  "Clive", 2])
users.insert([6,  "Hicks", 3])
users.insert([7,  "Devin", 2])
users.insert([8,  "Kate",  2])
users.insert([9,  "Klein", 3])
users.insert([10, "Jen",   1])

print (users)

assert len(users) == 11
assert users[1]['name'] == "Dunn"

assert users[1]['num_friends'] == 2

users.update({'num_friends' : 3},
             lambda row: row['user_id'] == 1)
# notice the smart use of lambda fxn above

assert users[1]['num_friends'] == 3












































