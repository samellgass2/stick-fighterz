from utils.constants import NUM_COLUMNS, NUM_ROWS, TILE_SIZE
import math

def to_screen_position_x(percent: int) -> int:
    """Expects a PERCENTAGE value between 0 and 100 and rounds down to nearest int"""
    return math.floor(NUM_COLUMNS * TILE_SIZE * percent / 100)


def to_screen_position_y(percent: int) -> int:
    """Expects a PERCENTAGE value between 0 and 100 and rounds down to nearest int"""
    return math.floor(NUM_ROWS * TILE_SIZE * percent / 100)

def endpoint_to_width(start_percent: int, end_percent: int) -> int: 
    return math.floor((NUM_COLUMNS * TILE_SIZE) * (end_percent - start_percent) / 100)

def endpoint_to_height(start_percent: int, end_percent: int) -> int: 
    return math.floor((NUM_ROWS * TILE_SIZE) * (end_percent - start_percent) / 100)