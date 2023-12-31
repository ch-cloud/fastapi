from sqlalchemy.orm import Session

from sql_app import models


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()
