# Project my_project

One Paragraph of project description goes here

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## MakeFile

Run build make command with tests
```bash
make all
```

Build the application
```bash
make build
```

Run the application
```bash
make run
```
Create DB container
```bash
make docker-run
```

Shutdown DB Container
```bash
make docker-down
```

DB Integrations Test:
```bash
make itest
```

Live reload the application:
```bash
make watch
```

Run the test suite:
```bash
make test
```

Clean up binary from the last build:
```bash
make clean
```
## api 

# Todo + Pet API Design

## User

| API                          | Method | Description        |
| ---------------------------- | ------ | ------------------ |
| /users                       | POST   | 创建用户               |
| /users                       | GET    | 用户列表               |
| /users/{id}                  | GET    | 用户详情               |
| /users/{id}                  | PUT    | 修改用户               |
| /users/{id}                  | DELETE | 删除用户               |
| /users/{id}/assets       | GET    | 查看用户资产（积分、能量、宠物粮等） |
| /users/{id}/pets             | GET    | 用户拥有的宠物            |
| /users/{id}/tasks            | GET    | 用户任务记录             |
| /users/{id}/exchange-records | GET    | 用户兑换记录             |

---

## Pet

| API               | Method | Description |
| ----------------- | ------ | ----------- |
| /pets             | POST   | 创建宠物        |
| /pets             | GET    | 宠物列表        |
| /pets/{id}        | GET    | 宠物详情        |
| /pets/{id}        | PUT    | 修改宠物名称等信息   |
| /pets/{id}        | DELETE | 删除宠物        |
| /pets/{id}/feed   | POST   | 喂养宠物（消耗宠物粮） |
| /pets/{id}/rename | POST   | 修改宠物昵称（可选）  |

---

## Task（任务模板）

| API         | Method | Description |
| ----------- | ------ | ----------- |
| /tasks      | GET    | 任务列表        |
| /tasks      | POST   | 创建任务        |
| /tasks/{id} | GET    | 任务详情        |
| /tasks/{id} | PUT    | 修改任务        |
| /tasks/{id} | DELETE | 删除任务        |

---

## User Task（学生任务）

| API                               | Method | Description |
| --------------------------------- | ------ | ----------- |
| /users/{id}/tasks                 | GET    | 用户任务记录      |
| /users/{id}/tasks/{taskId}/finish | POST   | 完成任务        |
| /users/{id}/tasks/{taskId}/cancel | POST   | 取消完成（可选）    |

完成任务后：

* 增加 Score
* 增加 Energy
* 增加 PetFood
* 写入 StudentTask 记录

---

## Rule（兑换规则）

| API         | Method | Description |
| ----------- | ------ | ----------- |
| /rules      | GET    | 规则列表        |
| /rules      | POST   | 创建规则        |
| /rules/{id} | GET    | 查看规则        |
| /rules/{id} | PUT    | 修改规则        |
| /rules/{id} | DELETE | 删除规则        |

---

## Exchange（兑换）

| API                          | Method | Description |
| ---------------------------- | ------ | ----------- |
| /users/{id}/exchange         | POST   | 根据规则兑换资源    |
| /users/{id}/exchange-records | GET    | 查看兑换历史      |

请求示例：

POST /users/1/exchange

```json
{
    "rule_id": 3
}
```

---

## assets（资源）

如果以后资源越来越多（金币、钻石、经验等），建议把资产作为独立资源。

| API                          | Method | Description |
| ---------------------------- | ------ | ----------- |
| /users/{id}/assets       | GET    | 当前资源        |
| /users/{id}/assets-records | GET    | 资源流水        |

资源流水包括：

* 完成任务
* 兑换奖励
* 喂养宠物
* 系统赠送
* 管理员调整

---

## Statistics（统计，可选）

| API                    | Method | Description |
| ---------------------- | ------ | ----------- |
| /users/{id}/statistics | GET    | 用户统计        |
| /leaderboard           | GET    | 排行榜         |

统计信息例如：

* 已完成任务数
* 当前积分
* 已兑换次数
* 宠物数量
* 宠物最高等级
* 累计获得积分
* 累计获得宠物粮

---

# 推荐的 REST 风格

资源使用名词：

* /users
* /pets
* /tasks
* /rules

业务行为使用动作：

* /finish
* /feed
* /exchange

避免使用：

* /doTask
* /getUserInfo
* /createRule

保持 API 统一、易扩展，后续增加签到、商城、抽奖等功能时无需修改整体设计。
