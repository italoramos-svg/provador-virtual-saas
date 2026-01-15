from backend.models.tryon_job import PipelineType
from backend.services.product_quality_checker import is_overlay_viable


def decide_pipeline(product_image_path: str, category: str) -> PipelineType:
    """
    Decide qual pipeline usar:
    - Camisa: IA generativa
    - Acessórios: overlay se possível, senão IA
    """

    if category == "top":
        return PipelineType.generative

    if is_overlay_viable(product_image_path, category):
        return PipelineType.overlay

    return PipelineType.generative
