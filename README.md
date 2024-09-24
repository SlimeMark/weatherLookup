# Aeroweather lookup via CheckWX API

使用CheckWX API查询航空天气信息

#### //TODO:
- 经纬度METAR查询结果解析
- 带有半径的查询结果解析
- TAF查询结果解析
- AIRMET/SIGMET查询结果解析

#### 当前功能
- 查询指定ICAO机场的METAR信息，返回解码文本及原始METAR文本
- 按高度排序的云层信息

**返回的所有数据来自checkwx.com，本程序不对数据准确性负责**