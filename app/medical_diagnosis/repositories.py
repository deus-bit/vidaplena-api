from app.medical_diagnosis.models import MedicalDiagnosisModel, MedicalDiagnosisAttribute
from app.base.repositories import BaseRepository, SQLRepository
from app.base.models import FindQuery, FilterBy
from app.exceptions import *
from app.config import settings
from app.utils import Interval, RegEx
from sqlmodel import create_engine
from datetime import datetime
from typing import override
from abc import ABC

class MedicalDiagnosisFilterBy(FilterBy, total=False):
    id: Interval[int]
    created_at: Interval[datetime]
    patient_id: Interval[int]
    doctor_id: Interval[int]
    disease: RegEx


class MedicalDiagnosisFindQuery(FindQuery[MedicalDiagnosisFilterBy, MedicalDiagnosisAttribute]):
    ...


class MedicalDiagnosisRepository(BaseRepository[MedicalDiagnosisModel, MedicalDiagnosisFindQuery], ABC):
    ...


class InMemoryMedicalDiagnosisRepository(SQLRepository[MedicalDiagnosisModel, MedicalDiagnosisFindQuery]):
    @override
    def __init__(self) -> None:
        super().__init__(
            model=MedicalDiagnosisModel,
            engine=create_engine(url="sqlite://", connect_args={
                'timeout': 2.0,
                'cached_statements': 512
            }),
            page_size_max=64
        )


class SupabaseMedicalDiagnosisRepository(SQLRepository[MedicalDiagnosisModel, MedicalDiagnosisFindQuery]):
    @override
    def __init__(self) -> None:
        super().__init__(
            model=MedicalDiagnosisModel,
            engine=create_engine(url=settings.supabase_url),
            page_size_max=64
        )
