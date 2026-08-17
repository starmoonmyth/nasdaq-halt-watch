# Nasdaq Halt Watch（纳斯达克停牌监控）

一个用于监控 **Nasdaq Trader 官方交易停牌 RSS** 的开源 Python 项目。

它负责把官方停牌和计划复牌记录转换成结构化事件，供其他程序接入通知、日志、网页或研究流程使用。

## 项目解决什么问题？

很多行情软件会把“没有报价”“成交不活跃”“数据源故障”和“交易所正式停牌”混在一起。这个项目只使用 Nasdaq Trader 官方停牌信息，不根据价格不变或行情缺失猜测停牌状态。

## 当前功能

- 读取 Nasdaq Trader 官方 Trade Halt RSS
- 解析停牌日期、时间、股票代码、公司名称、市场和 Reason Code
- 解析计划复牌日期、Quote Time 和 Trade Time
- 保留数据来源、发布时间和原始记录 ID
- 生成稳定的事件 ID
- 对重复的停牌/复牌状态进行去重
- 强制最短 60 秒轮询间隔
- 支持 Python 3.11、3.12 和 3.13
- GitHub Actions 自动运行测试和代码检查

Nasdaq 官方说明该 RSS 在交易日大约每分钟更新一次，并要求使用者不要超过每分钟查询一次。项目遵循这一限制。

## 明确不做什么

本项目不是：

- 行情或逐笔成交数据服务
- 券商交易系统
- 自动下单工具
- 投资建议或收益预测工具
- 根据价格变化推断停牌的程序

项目不包含个人账户、API Key、持仓信息或交易策略。

## 安装

```bash
python -m pip install nasdaq-halt-watch
```

开发环境：

```bash
python -m pip install -e '.[dev]'
pytest
ruff check .
```

## 最小示例

```python
from datetime import UTC, datetime

from nasdaq_halt_watch import HaltMonitor

monitor = HaltMonitor()
events = monitor.poll(now=datetime.now(UTC))

for event in events:
    print(
        event.state,
        event.record.symbol,
        event.record.reason_code,
        event.record.halt_time,
    )
```

应用程序应在发送通知前持久化 `event.event_id`，避免服务重启后重复提醒。

## 事件状态

- `halted`：记录当前被官方 RSS 标识为停牌，或尚未出现复牌时间
- `resumed`：记录中包含官方计划复牌交易时间

复牌时间只表示交易所公布的计划时间，不保证实际成交一定在该时刻发生。

## 开源协作

欢迎提交 Issue 和 Pull Request。新增解析逻辑时，请附上脱敏的官方 RSS fixture 和测试，不要提交 API Key、账户信息、私人仓库内容或券商数据。

详见：

- [贡献指南](CONTRIBUTING.md)
- [行为准则](CODE_OF_CONDUCT.md)
- [安全政策](SECURITY.md)
- [项目边界](docs/PROJECT_READINESS.md)

## 许可证

本项目使用 MIT License。

## 官方来源

- [Nasdaq Trader Trade Halt RSS](https://www.nasdaqtrader.com/Trader.aspx?id=TradeHaltRSS)
- [Nasdaq Trader Trading Halt Codes](https://www.nasdaqtrader.com/Trader.aspx?id=TradeHaltCodes)

