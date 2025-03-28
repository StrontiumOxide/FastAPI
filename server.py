import os
import asyncio
from fastapi import FastAPI
from schema import (
    CreateAnnouncementRequest, 
    GetAnnouncementResponse, 
    UpdateAnnouncementRequest, 
    SearchFieldsAnnouncementRequest
)
from database import Session, Announcement


app = FastAPI(
    title='Сервис объявлений купли/продажи',
    description='Домашнее задание'
)


@app.post(path='/api/', tags=['Announcement'])
async def create_announcement(data: CreateAnnouncementRequest):
    """Функция для создания записи об объявлении в БД"""

    with Session() as session:
        session.add(Announcement(**data.model_dump()))
        session.commit()

    return {'status': 'success'}


@app.get(path=r'/api/{id}', tags=['Announcement'])
async def get_announcement(announcement_id: int) -> GetAnnouncementResponse | dict:
    """Функция для получения записи об объявлении из БД"""

    with Session() as session:
        announcement = session.get(Announcement, announcement_id)

    if announcement:
        return GetAnnouncementResponse(**announcement.__dict__)
    else:
        return {'status': 'unsuccess'}


@app.delete(path=r'/api/', tags=['Announcement'])
async def delete_announcement(announcement_id: int) -> dict:
    """Функция для удалению записи об объявлении из БД"""

    with Session() as session:
        announcement = session.get(Announcement, announcement_id)

        if announcement:
            session.delete(announcement)
            session.commit()
            return {'status': 'success'}

        return {'status': 'unsuccess'}
    

@app.patch(path=r'/api/', tags=['Announcement'])
async def patch_announcement(announcement_id: int, data: UpdateAnnouncementRequest) -> dict:
    """Функция для обновления записи об объявлении из БД"""

    with Session() as session:
        announcement = session.get(Announcement, announcement_id)

        if announcement:
            
            if data.title:
                announcement.title = data.title

            if data.description:
                announcement.description = data.description

            if data.price:
                announcement.price = data.price

            if data.author:
                announcement.author = data.author

            session.commit()

            return {'status': 'success'}
        
        return {'status': 'unsuccess'}


@app.get(path=r'/api/', tags=['AnnouncementFields'])
async def get_fields_announcement(data: SearchFieldsAnnouncementRequest) -> dict:
    """Функция для получения записи об объявлении из БД"""
    pass


async def main() -> None:
    """Главная функция"""

    os.system(command='uvicorn server:app --port 8000')


if __name__ == '__main__':
    asyncio.run(main())
