from fastapi import APIRouter
from app.models import ChargebackCreate
from app.database import chargebacks_collection

router = APIRouter(
    prefix="/chargebacks",
    tags=["Chargebacks"]
)


@router.post("/")
def create_chargeback(chargeback: ChargebackCreate):

    chargeback_data = chargeback.model_dump()

    result = chargebacks_collection.insert_one(
        chargeback_data
    )

    return {
        "message": "Chargeback created successfully",
        "id": str(result.inserted_id)
    }


@router.get("/")
def get_chargebacks():

    chargebacks = list(
        chargebacks_collection.find(
            {},
            {"_id": 0}
        )
    )

    return chargebacks