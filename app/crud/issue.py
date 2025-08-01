from sqlalchemy.orm import Session
from app.models.issue import IssuedPart
from app.schemas.issue import IssueCreate
from app.models.spare_part import SparePart


def issue_part(db: Session, issue: IssueCreate):
    # Decrease quantity from inventory
    part = db.query(SparePart).filter(SparePart.id == issue.spare_part_id).first()
    if not part or part.quantity < issue.quantity:
        return None  # Not enough inventory

    part.quantity -= issue.quantity
    db_issue = IssuedPart(**issue.dict())
    db.add(db_issue)
    db.commit()
    db.refresh(db_issue)
    return db_issue


def get_all_issues(db: Session):
    return db.query(IssuedPart).all()
