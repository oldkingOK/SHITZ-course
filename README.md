# 无情的抢课机器

整个代码就是依托史，且用户不友好，但是可以跑（截至2024-12-31）。感谢群友的*拼译中*api翻译

## 使用方法

### 准备

1. 安装油猴脚本 tample\show_id.js

```shell
python3 -m venv .venv
source ./.venv/bin/activate # pwsh 为 .\.venv\Scripts\activate
pip install -r requirements.txt
cp config.ini.example config.ini # 修改其中的参数
```

### 开始

```pwsh
ipython3
%run app.py
```

> 一般 ticket 的获取都会比较畅通

- `u_ticket()` ── 更新 ticket，如果长时间本研登录失败可以尝试
- `u_cookie()` ── 更新 cookie，同上（注：最好与 ticket 同时进行）
- `grab()` ── 开始爬课