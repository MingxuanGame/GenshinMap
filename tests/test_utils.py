import json
from pathlib import Path

DIR = Path(__file__).parent


def test_get_points_by_id() -> None:
    from genshinmap.models import Point, XYPoint
    from genshinmap.utils import get_points_by_id

    with open(DIR / "points.json") as f:
        points = [Point.parse_obj(i) for i in json.load(f)["point_list"]]
    assert get_points_by_id(298, points) == [
        XYPoint(114, 514),
        XYPoint(1919, 810),
    ]


def test_convert_pos() -> None:
    from genshinmap.models import XYPoint
    from genshinmap.utils import convert_pos

    points = [XYPoint(1200, 5000), XYPoint(-4200, 1800)]
    origin = [4844, 4335]
    assert convert_pos(points, origin) == [
        XYPoint(x=6044, y=9335),
        XYPoint(x=644, y=6135),
    ]
