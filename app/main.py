from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Union

from app.retrieval import retrieve_resumes

app = FastAPI()


class QueryRequest(BaseModel):
    query: str
    required_skills: List[str]
    top_k: int = 5


class ResumeResponse(BaseModel):
    file_name: str
    candidate_name: Optional[str]
    skills: List[str]
    years_of_experience: Optional[Union[str, int]]


@app.post("/retrieve_resumes/", response_model=List[ResumeResponse])
async def get_resumes(request: QueryRequest):

    try:
        dataset_path = "hub://smruthisumanthrao/text_embed"

        results = retrieve_resumes(
            request.query,
            dataset_path,
            top_k=request.top_k
        )

        filtered_resumes = []

        for resume in results:

            if all(
                skill in resume['skills']
                for skill in request.required_skills
            ):
                filtered_resumes.append(resume)

        return filtered_resumes

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@app.get("/")
def home():
    return {"message": "TalentSync API Running"}