from PIL import Image


def is_overlay_viable(image_path: str, category: str) -> bool:
    """
    Avalia se a imagem do produto é boa o suficiente para overlay.
    MVP: regras simples baseadas em resolução.
    """

    try:
        with Image.open(image_path) as img:
            width, height = img.size

        # Regras mínimas por categoria
        if category == "glasses":
            return width >= 600 and height >= 300

        if category in ["earring", "necklace"]:
            return width >= 600 and height >= 600

        # Camisas não usam overlay
        if category == "top":
            return False

        return False

    except Exception:
        return False
