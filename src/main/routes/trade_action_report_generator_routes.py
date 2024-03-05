from fastapi import APIRouter

from src.factories.trade_action_report_generator_controller import (
    make_trade_action_report_generator_controller,
)

router = APIRouter(prefix="/trade-action", tags=["Trade Action"])


def setup_routes(base_router: APIRouter):
    base_router.include_router(router)


@router.post("/")
async def generate_trade_action_report() -> None:
    controller = make_trade_action_report_generator_controller()

    return await controller.handle()
