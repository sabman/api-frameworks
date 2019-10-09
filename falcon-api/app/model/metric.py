from sqlalchemy import Column, ForeignKey
from sqlalchemy import String, Integer, LargeBinary
from app.model import Base


class Metric(Base):
    id = Column(Integer, primary_key=True)
    value = Column(Integer, nullable=False)
    model_ref = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('user.user_id'))

    def __repr__(self):
        return "<Metric(value='%d', token='%d')>" % (
            self.value,
            self.model_ref,
        )

    FIELDS = {"value": int, "model_ref": int}
    FIELDS.update(Base.FIELDS)
