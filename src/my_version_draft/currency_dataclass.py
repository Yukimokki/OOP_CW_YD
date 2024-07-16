from dataclasses import dataclass
from dataclasses import astuple, asdict

@dataclass(frozen=True)
class Currency:
    currency_name: str = 'RUR'
    currency_rate: float = '1.0'

cur = Currency()
print(astuple(cur))
print(asdict(cur))
