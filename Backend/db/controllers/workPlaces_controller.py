from __future__ import annotations
from sqlalchemy.orm import Session
from Backend.db.controllers.base_controller import BaseController
from Backend.db.models import WorkPlace
from Backend.db.repositories.workPlaces_repository import WorkPlacesRepository
from Backend.db.services.workPlaces_service import WorkPlacesService

from typing import List, Tuple  # Importing List and Tuple from typing module


class WorkPlacesController(BaseController):
    """
    WorkPlacesController Class

    Controller class for managing workPlaces entities.
    """

    def __init__(self, db: Session):
        """
        Initializes the WorkPlacesController with a database session.

        Parameters:
            db (Session): SQLAlchemy Session for database interactions.
        """
        self.repository = WorkPlacesRepository(db)
        self.service = WorkPlacesService(self.repository)
        super().__init__(self.repository, self.service)

    def get_active_workers_by_workplace_id(self, workplace_id: int):
        """
        Retrieves the names and IDs of all active workers in the specified workplace.

        Parameters:
            workplace_id (int): ID of the workplace.

        Returns:
            List[Tuple[int, str]]: A list of tuples containing worker IDs and names.
        """
        # Utilize the service method to get active workers by workplace ID
        return self.service.get_active_workers_by_workplace_id(workplace_id)

    def get_active_workers_for_user(self, user_id: int) -> List[Tuple[int, str]]:
        """
        Retrieves the names and IDs of all active workers in the workplace where the specified user works.

        Parameters:
            user_id (int): ID of the user.

        Returns:
            List[Tuple[int, str]]: A list of tuples containing worker IDs and names.
        """
        # Retrieve the workplace ID for the specified user
        workplace_id = self.repository.get_workplace_id_by_user_id(user_id)

        if workplace_id is not None:
            # Utilize the service method to get active workers by workplace ID
            return self.service.get_active_workers_by_workplace_id(workplace_id)
        else:
            # If the user does not work in any workplace, return an empty list
            return []

    def get_workplace_by_worker_id(self, user_id: int) -> WorkPlace:
        """
        Retrieves the workplace where the specified user works.

        Parameters:
            user_id (int): ID of the user.

        Returns:
            WorkPlace: The workplace where the user works.
        """
        # Utilize the service method to get the workplace name by user ID
        return self.repository.get_workplace_by_worker_id(user_id)

    def get_workplace_id_by_user_id(self, user_id: str) -> str | None:
        """
        Retrieves the workplace ID for the specified user.

        Parameters:
            user_id (str): ID of the user.

        Returns:
            str | None: The workplace ID if the user works in a workplace, else None.
        """
        # Utilize the repository method to get the workplace ID by user ID
        return self.repository.get_workplace_id_by_user_id(user_id)

    def get_workplace_name_by_worker_id(self, user_id: str) -> str:
        """
        Retrieves the name of the workplace where the specified user works.

        Parameters:
            user_id (str): ID of the user.

        Returns:
            str: The name of the workplace.
        """
        return self.repository.get_workplace_name_by_worker_id(user_id)

    def get_all_workers_by_workplace_id(self, workplace_id: str):
        """
        Retrieves all active users working in the specified workplace.

        Parameters:
            workplace_id (int): ID of the workplace.

        Returns:
            List[User]: A list of active users working in the specified workplace.
        """
        return self.repository.get_users_by_workplace_id(workplace_id)
