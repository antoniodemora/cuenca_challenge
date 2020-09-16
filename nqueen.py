from itertools import permutations
import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class NQueen(Base):
    __tablename__ = "nqueen"
    id = Column(Integer, primary_key=True)
    n = Column(Integer)
    solution_count = Column(Integer)

    def __repr__(self):
        return "Solutions for N={}: {}".format(str(self.n), str(self.solution_count))


def find_nqueen(n=8, display=True):
    if n<8:
        raise ValueError('n must be grater than or equal 8')
    sol = 0
    cols = range(n)
    result = []
    for combo in permutations(cols):                      
        if n == len(set(combo[i]+i for i in cols)) == len(set(combo[i]-i for i in cols)):
            sol += 1
            result.append(combo)
            if display:
                print('Solution {}: {}\n'.format(str(sol), str(combo)))
                print("\n".join(' o ' * i + ' X ' + ' o ' * (n-i-1) for i in combo) + "\n\n\n\n")
    
    return (sol, result)

if __name__ == '__main__':
    DB_HOST = os.environ.get("DB_HOST")
    DB_NAME = os.environ.get("DB_NAME")
    DB_USER = os.environ.get("DB_USER")
    DB_PASSWD = os.environ.get("DB_PASSWD")

    engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWD}@{DB_HOST}/{DB_NAME}")

    if not Base.metadata.tables[NQueen.__tablename__].exists(engine):
        Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    for i in range(8,12):
        solution_count, solution_set = find_nqueen(i, False)
        session = Session()
        n_queen = NQueen(n=i, solution_count=solution_count)
        session.add(n_queen)
        session.commit()
        print(n_queen)


