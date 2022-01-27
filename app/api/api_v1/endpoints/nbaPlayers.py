from fastapi import APIRouter, HTTPException

from crud.crudNBAPlayers import crudNBAPlayers

router = APIRouter()

@router.get("/pairHeightPlayers/{height}")
def heighPlayers(height: int):

    nbaplayer = crudNBAPlayers()

    nbaplayer.pairHeights(height)

    response = nbaplayer.displayResult()

    return {
        "status": 200,
        "data": response
    }

