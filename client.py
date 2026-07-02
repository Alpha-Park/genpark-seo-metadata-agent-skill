from typing import Dict, Any

class SEOMetadataGeneratorClient:
    def generate_metadata(self, title: str, description: str, tags: list) -> Dict[str, Any]:
        clean_title = f"{title} | GenPark Store"
        meta_description = description[:155] + "..." if len(description) > 155 else description
        keywords = ", ".join(tags)
        return {
            "title_tag": clean_title[:60],
            "meta_description": meta_description,
            "meta_keywords": keywords
        }
