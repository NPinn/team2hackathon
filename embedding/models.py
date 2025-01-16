from math import isnan
from numbers import Number
from typing import Annotated, Any, Optional, TypeVar

from pydantic import BaseModel
from pydantic.functional_validators import BeforeValidator


def coerce_nan_to_none(x: Any) -> Any:
    if isinstance(x, Number):
        if isnan(x):
            return None
    return x


T = TypeVar("T")

NoneOrNan = Annotated[Optional[T], BeforeValidator(coerce_nan_to_none)]


class PatientInfo(BaseModel):
    first_name: str
    last_name: str
    patient_id: str
    medical_clerking: NoneOrNan[str]
    discharge_note: NoneOrNan[str]
