import json
from collections import namedtuple

data = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'
data2 = "{\"filter\":[{\"left\":\"change\",\"operation\":\"nempty\"}],\"symbols\":{\"query\":{\"types\":[]}},\"columns\":[\"name\",\"Recommend.Other\",\"ADX\",\"AO\",\"ATR\",\"CCI20\",\"MACD.macd\",\"MACD.signal\",\"Mom\",\"RSI\",\"Stoch.K\",\"Stoch.D\",\"description\",\"name\",\"subtype\",\"ADX\",\"ADX+DI\",\"ADX-DI\",\"ADX+DI[1]\",\"ADX-DI[1]\",\"AO\",\"AO[1]\",\"CCI20\",\"CCI20[1]\",\"MACD.macd\",\"MACD.signal\",\"Mom\",\"Mom[1]\",\"RSI\",\"RSI[1]\",\"Stoch.K\",\"Stoch.D\",\"Stoch.K[1]\",\"Stoch.D[1]\"],\"sort\":{\"sortBy\":\"change\",\"sortOrder\":\"desc\"},\"options\":{\"lang\":\"en\"},\"range\":[0,150]}"
# Parse JSON into an object with attributes corresponding to dict keys.
x = json.loads(data2, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
#print(x.name, x.hometown.name, x.hometown.id)
# print(x.filter[0].left,x.filter[0].operation,x.symbols.query.types,x.columns[0],
# x.columns[1],
# x.columns[2],
# x.columns[3],
# x.columns[4],
# x.columns[5],
# x.columns[6],
# x.columns[7],
# x.columns[8],
# x.columns[9],
# x.columns[10],
# x.columns[11],
# x.columns[12],
# x.columns[13],
# x.columns[14],
# x.columns[15],
# x.columns[16],
# x.columns[17],
# x.columns[18],
# x.columns[19],
# x.columns[20],
# x.columns[21],
# x.columns[22],
# x.columns[23],
# x.columns[24],
# x.columns[25],
# x.columns[26],
# x.columns[27],
# x.columns[28],
# x.columns[29],
# x.columns[30],
# x.columns[31],
# x.columns[32],
# x.columns[33],x.sort.sortBy,x.sort.sortOrder,x.options.lang,x.range)
#,x.columns[1],x.columns[2],x.columns[3]

# for i in range(0,34):
#     print("x.columns["+str(i)+"],")

print(*(x.columns[i] for i in range(1, 34)))
