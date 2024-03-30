"""
Описание моделей данных (DTO).
"""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class NewsItemDTO(BaseModel):
    """
    Модель данных для представления новости.

    .. code-block::

        NewsInfoDTO(
            source="BBC News",
            "author"="BBC News",
            "title"="What does the King's diagnosis mean for William, Harry and the other royals?",
            "description"="It's been a bleak midwinter for the Royal Family.
            Will the King's health news help to bring them together?",
            "url"="https://www.bbc.co.uk/news/uk-68211941",
            "published_at"="2024-02-06T12:37:22.3818701Z",
        )
    """



    source: str
    author: Optional[str]
    title: str
    description: Optional[str]
    url: Optional[str]
    published_at: datetime
