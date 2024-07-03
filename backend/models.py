import uuid
from datetime import date, datetime

from sqlalchemy import (
    UUID,
    Boolean,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    MetaData,
    String,
    func,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

metadata = MetaData()


class BaseModel(DeclarativeBase):
    __abstract__ = True
    metadata = metadata

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)

    def to_dict(self):
        return {field.name: getattr(self, field.name) for field in self.__table__.c}


class User(BaseModel):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    guid: Mapped[uuid.UUID] = mapped_column(String(36), unique=True, default=uuid.uuid4)
    password: Mapped[str] = mapped_column(String(128))
    username: Mapped[str] = mapped_column(String(150), unique=True)
    name: Mapped[str] = mapped_column(String(150), default="")
    email: Mapped[str] = mapped_column(String(254), unique=True)
    last_login: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)

    tasks: Mapped[list["Task"]] = relationship(back_populates="user")


class Task(BaseModel):
    __tablename__ = "task"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    guid: Mapped[uuid.UUID] = mapped_column(String(36), unique=True, default=uuid.uuid4)
    priority: Mapped[int] = mapped_column(Integer)
    text: Mapped[str] = mapped_column(String(50))
    completed: Mapped[bool] = mapped_column(Boolean, default=False)
    posted_at: Mapped[date] = mapped_column(Date)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="tasks")


class PetUsers(BaseModel):
    __tablename__ = "pet_users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(30))
    phone: Mapped[str] = mapped_column(String(30))
    wechat: Mapped[str] = mapped_column(String(30))
    pic: Mapped[str] = mapped_column(String(30))
    sex: Mapped[int] = mapped_column(Integer)
    reg_time: Mapped[DateTime] = mapped_column(DateTime)
    actived: Mapped[bool] = mapped_column(Boolean)