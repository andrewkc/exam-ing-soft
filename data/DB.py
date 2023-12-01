from models.Account import Account
from models.Operation import Operation
from typing import List

DB: List[Account] = []
DB.append(Account('21345', 'Arnaldo', 200, ['123', '456']))
DB.append(Account('123', 'Luisa', 400, ['456']))
DB.append(Account('456', 'Andrea', 300, ['21345']))

Ops: List[Operation] = []