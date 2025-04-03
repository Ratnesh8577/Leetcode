import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> list[int]:

    return list(players.shape)# # Returns [number of rows, number of columns]
    