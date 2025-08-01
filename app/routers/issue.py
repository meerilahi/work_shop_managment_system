from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.issue import IssueCreate, IssueOut
from app.crud import issue as crud
from app.db.deps import get_db
from typing import List

router = APIRouter(prefix="/issues", tags=["Issued Parts"])


@router.post("/", response_model=IssueOut)
def issue_part(issue: IssueCreate, db: Session = Depends(get_db)):
    result = crud.issue_part(db, issue)
    if not result:
        raise HTTPException(status_code=400, detail="Not enough quantity or invalid part")
    return result


@router.get("/", response_model=List[IssueOut])
def get_issues(db: Session = Depends(get_db)):
    return crud.get_all_issues(db)
