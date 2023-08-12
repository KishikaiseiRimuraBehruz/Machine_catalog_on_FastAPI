from sqlalchemy import Column,String, Integer,DateTime, BigInteger


from __init__ import Base


class Car(Base):
    __tablename__ = 'cars'
    id = Column(BigInteger,
                autoincrement=True,
                primary_key=True
)
    name = Column(String,
                  nullable=True
)
    model = Column(String,
                   nullable=False
)
    year = Column(Integer,
                  nullable=True
)
    reg_date = Column(DateTime,
                      nullable=True)


