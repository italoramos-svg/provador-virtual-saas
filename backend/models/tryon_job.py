from enum import Enum
from datetime import datetime
from uuid import uuid4


class JobStatus(str, Enum):
    queued = "queued"
    processing = "processing"
    done = "done"
    failed = "failed"


class PipelineType(str, Enum):
    overlay = "overlay"
    generative = "generative"


class TryOnJob:
    def __init__(
        self,
        user_image_path: str,
        product_image_path: str,
        product_category: str,
        pipeline: PipelineType
    ):
        self.id = str(uuid4())
        self.user_image_path = user_image_path
        self.product_image_path = product_image_path
        self.product_category = product_category
        self.pipeline = pipeline
        self.status = JobStatus.queued
        self.created_at = datetime.utcnow()
        self.result_image_path = None
