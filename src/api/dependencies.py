from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.data_base import get_session

SessionDep = Annotated[AsyncSession, Depends(get_session)]
