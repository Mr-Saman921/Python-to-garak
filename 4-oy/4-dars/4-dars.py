"""
data class
"""

from dataclasses import dataclass
from typing import Any, List, Dict, Union, Optional
@dataclass(frozen=True)
class User:
    name: str
    surname: str
    login: str
    password: str
    email: str
    info: Dict[Optional[Union[str, int]], Any]

user = User(name="Samandar", surname="Siddiqov", login="MrSaman456", password="mrsaman456", email="ssiddiqov@gmail.com", info=[1, 11])
print(user)
