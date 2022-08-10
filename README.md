# GenshinMap

[![License](https://img.shields.io/github/license/MingxuanGame/GenshinMap?style=flat-square)](https://github.com/MingxuanGame/GenshinMap/blob/master/LICENSE)
[![QQ群](https://img.shields.io/badge/QQ%E7%BE%A4-929275476-success?style=flat-square)](https://jq.qq.com/?_wv=1027&k=C7XY04F1)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/MingxuanGame/GenshinMap/master.svg)](https://results.pre-commit.ci/latest/github/MingxuanGame/GenshinMap/master)

GenshinMap 是一个米游社大地图 API 的包装，用于简易获取大地图数据

## 快速开始

```python
import asyncio

from genshinmap import utils, models, request


async def main():
    map_id = models.MapID.teyvat
    # 获取地图数据
    maps = await request.get_maps(map_id)
    # 获取资源列表
    labels = await request.get_labels(map_id)
    # 获取坐标
    points = await request.get_points(map_id)

    # 获取单片地图
    map_image = await utils.get_map_by_pos(maps.detail, 1024)
    # 获取传送锚点坐标
    transmittable = utils.get_points_by_id(3, points)
    # 转换坐标
    transmittable_converted = utils.convert_pos(
        transmittable, maps.detail.origin
    )


if __name__ == "__main__":
    asyncio.run(main())
```

## 许可

[MIT](./LICENSE)
