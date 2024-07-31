from dataclasses import dataclass, field
from typing import List, Optional
@dataclass
class ReqStampingDetailApproverDto:
    fullname: Optional[str] = None
    status: Optional[str] = None
    timestamp: Optional[str] = None


@dataclass
class ReqStampingDto:
    title: Optional[str] = None
    documentId: Optional[str] = None
    status: Optional[str] = None
    information: Optional[str] = None
    detailApprover: List[ReqStampingDetailApproverDto] = field(default_factory=list)
    fileBase64: Optional[str] = None
