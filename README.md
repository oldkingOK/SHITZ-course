# 无情的抢课机器

整个代码就是依托史，且用户不友好，但是可以跑（截至2024-12-31）。感谢群友的*拼译中*api翻译

目前在自用，考完再继续优化和完善文档，目标是军备竞赛，推进学校选课平台的进化。

## 使用方法

### 准备

#### 获取课程信息

安装油猴脚本 tample\show_id.js

进入选课界面，会在中文课程名的下面看到一长串课程 ID，长度为 32 位，复制下来。修改 app.py 中的 ids

#### 运行环境准备

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