from fastapi import APIRouter

from src.main.routes.dtos import InputDTO

router = APIRouter(prefix="/example", tags=["Example"])


def setup_routes(base_router: APIRouter):
    base_router.include_router(router)


class ExampleInputDTO(InputDTO):

    example_id: str


@router.post("/")
async def example(
    request: ExampleInputDTO,
) -> None:
    return "OK"
