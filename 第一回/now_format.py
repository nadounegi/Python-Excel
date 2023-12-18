from datetime import datetime

t = datetime.now()
fmt = t.strftime("%Y年%m月%d日 %H時%M分%S秒")
print(fmt)
