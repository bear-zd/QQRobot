from pypbbot import app, run_server, BaseDriver
from pypbbot.protocol import PrivateMessageEvent, GroupMessageEvent
from pypbbot.utils import Clips, LazyLock, sendBackClipsTo
from typing import Union
import asyncio
import NewsPlugins

i, lock = 0, LazyLock()
akkarin_url = 'https://ak1.picdn.net/shutterstock/videos/1006819771/thumb/6.jpg'
suck_url = 'https://tse3-mm.cn.bing.net/th/id/OIP.CAdgk6OhjOD70TtaGR0LWgAAAA?pid=ImgDet&rs=1'
async def replynew(event: Union[PrivateMessageEvent, GroupMessageEvent],include):
  global lock
  with await lock.lock(): # 加异步锁
    await sendBackClipsTo(event,NewsPlugins.News(include))

async def sayHello(event: Union[PrivateMessageEvent, GroupMessageEvent]):
  global i, lock
  with await lock.lock(): # 加异步锁
    await sendBackClipsTo(event, 'Hello, world! x {}'.format(i))
    await asyncio.sleep(1)
    await sendBackClipsTo(event,
    Clips.from_image_url(akkarin_url) + '\n\阿卡林/\阿卡林/\阿卡林/')
    i += 1

async def saySuck(event: Union[PrivateMessageEvent, GroupMessageEvent]):
  with await lock.lock():  # 加异步锁
    await sendBackClipsTo(event, '♂')
    await sendBackClipsTo(event,
    Clips.from_image_url(suck_url) )

class SimpleDriver(BaseDriver): # 驱动器类
  async def onPrivateMessage(self, event: PrivateMessageEvent):
    if event.raw_message.startswith('@弔机器人'):
      await sayHello(event)
    if event.raw_message.endswith('嗦牛子'):
      await saySuck(event)
  async def onGroupMessage(self, event: GroupMessageEvent):
    if event.raw_message.startswith('@f'):
      if '新闻' in event.raw_message:
        await replynew(event,event.raw_message)
      if '嗦牛子' in event.raw_message:
        await saySuck(event)

app.driver_builder = SimpleDriver # 注册驱动器

if __name__ == '__main__':
  run_server(app='__main__:app', host='localhost', port=6666, reload=True)