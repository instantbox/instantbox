# instantbox 服务API文档

文档版本：0.0.3

修订历史：

- 0.0.1：初稿 2018/12/11

- 0.0.2：修改状态码 2018/12/11

- 0.0.3：修改了 webshell 生成方式，改进 API，支持 Ubuntu/CentOS/Alpine 的大部分镜像 2018/12/18

  主要改进如下:

  ​	1. API 从 <font color=#DC143C>/v1/superspire/</font> -> <font color=#DC143C>/v2/superinspire/</font>

  ​	2. 支持 Ubuntu 14.04~18.04, CentOS6.10, CentOS7, Alpine latest

  ​	3. 支持 nginx 频率控制，默认返回 503 错误


## API请求方式说明

- 目前所有的提交类接口仅支持 POST 方式，查询类接口仅支持 GET 方式 [暂时都开放]
- 所有参数在传入时应当使用：**UTF-8 编码**


### 请求的URL

格式：
```
/v2/superinspire/{relative_path}?{query_string}
```

举例：
```
/v2/superinspire/getOS?os=10000
```

### 参数说明

| **参数名称** | **描述** |
| ----------- | ------- |
| relative_path | API 操作相对路径，如：`getOS` |
| query_string  | 放在 HTTP 头部传入的参数，必须经过 UrlEncode 编码 |

### HTTP GET 和 POST 方式使用说明

| 请求方式  | GET | POST |
| -------- | --- | ---- |
| URL | `/v2/superinspire/{relative_path}?{query_string}` | `/v2/superinspire/{relative_path}?{query_string}` |
| 请求参数 | 全部携带在 HTTP 请求头部的 query_string 中。 | 既可携带在 query_string 中，也可携带在 HTTP Body 中。携带在 query_string 中的参数的值，必须进行 UrlEncode 编码；  携带在 HTTP Body 中的参数，则不需要进行 UrlEncode 编码。 |
| HTTP BODY | 不携带 HTTP Body | multipart/form-data |

注：

- 如果 HTTP Body 和 query_string 存在相同的参数，则以 query_string 中的参数为准。
- HTTP URL 长度有限，若参数值长度过长，建议将参数放在 HTTP Body 中进行传输


### API 响应格式说明

|           | 正常请求 | 异常请求 |
| --------- | ------- | ------- |
| HTTP状态码 | 1 OK | 4** : 用户请求错误。 5** : server 服务失败。 |
| HTTP BODY | API 响应内容。除特殊说明外，为 JSON 字符串，例如：`{"statusCode":1, "message": "SUCCESS"}` | JSON 字符串，例如：`{"statusCode":404, "message": "Not support OS!"}` |


## 状态码

**状态码**用于指示错误类型。即：响应体(json 格式)的 `statusCode` 字段。

| 状态码 (statusCode) | 描述        |
| ------------------ | ---------- |
| 1                  | 操作执行成功 |
| 0                  | 操作执行失败 |


## API列表

### 容器列表

```
GET /getOSList
```

#### 请求参数

| 参数名 | 类型 | 描述 | 必选 |
| ----- | --- | ---- | --- |
| 无    | 无   | 无   | 无  |

#### 返回

| 参数名    | 类型      | 必选 |
| -------- | -------- | --- |
| json 数据 | json 类型 | 是  |

返回范例
```json
[
    {
        "label": "Ubuntu",
        "value": "Ubuntu",
        "logoUrl": "https://cdn.jsdelivr.net/gh/instantbox/instantbox-images/icon/ubuntu.png",
        "subList": [
            {
                "label": "12.04",
                "osCode": "10000"
            },
            {
                "label": "14.04",
                "osCode": "10001"
            },
            {
                "label": "16.04",
                "osCode": "10002"
            },
            {
                "label": "18.04",
                "osCode": "10003"
            },
            {
                "label": "latest",
                "osCode": "10004"
            }
        ]
    },
    {
        "label": "CentOS",
        "value": "CentOS",
        "logoUrl": "https://cdn.jsdelivr.net/gh/instantbox/instantbox-images/icon/centos.png",
        "subList": [
            {
                "label": "6.10",
                "osCode": "20000"
            },
            {
                "label": "7",
                "osCode": "20001"
            },
            {
                "label": "latest",
                "osCode": "20002"
            }
        ]
    },
    {
        "label": "Arch Linux",
        "value": "Arch Linux",
        "logoUrl": "https://cdn.jsdelivr.net/gh/instantbox/instantbox-images/icon/arch.png",
        "subList": [
            {
                "label": "2018.12.01",
                "osCode": "30000"
            },
            {
                "label": "latest",
                "osCode": "30001"
            }
        ]
    },
    {
        "label": "Debian",
        "value": "Debian",
        "logoUrl": "https://cdn.jsdelivr.net/gh/instantbox/instantbox-images/icon/debian.png",
        "subList": [
            {
                "label": "9.6.0",
                "osCode": "40000"
            },
            {
                "label": "latest",
                "osCode": "40001"
            }
        ]
    },
    {
        "label": "Fedora",
        "value": "Fedora",
        "logoUrl": "https://cdn.jsdelivr.net/gh/instantbox/instantbox-images/icon/fedora.png",
        "subList": [
            {
                "label": "28",
                "osCode": "50000"
            },
            {
                "label": "29",
                "osCode": "50001"
            },
            {
                "label": "latest",
                "osCode": "50002"
            }
        ]
    },
    {
        "label": "Alpine",
        "value": "Alpine",
        "logoUrl": "https://cdn.jsdelivr.net/gh/instantbox/instantbox-images/icon/alpine.png",
        "subList": [
            {
                "label": "latest",
                "osCode": "60000"
            }
        ]
    }
]
```


### 生成容器

```
GET /getOS
```

#### 请求参数

| 参数名   | 类型          | 描述                                     | 必选  | 例子       |
| ------- | ------------ | ---------------------------------------- | ---- | ---------- |
| os      | string       | 指定系统请求编码                            | 是   | 10000      |
| timeout | string       | 容器最长存活时间时间戳 [当前时间戳+存活时间长度] | 否   | 1544514176 |
| cpu     | string(Core) | 请求赋予 CPU 资源使用限制                    | 否   | 1          |
| mem     | string(MB)   | 请求赋予内存资源使用限制                      | 否   | 512        |
| port    | string       | 开放的端口，目前只允许开放一个端口              | 否   | 80         |

#### 返回

| 参数名       | 类型     | 描述                                    | 必选 |
| ----------- | ------- | --------------------------------------- | --- |
| statusCode  | integer | 状态码 (1, 302, 403, 404)                | 是  |
| message     | string  | 状态解读                                 | 是  |
| shareUrl    | string  | 容器 Url 地址                            | 否  |
| containerId | string  | 容器标识码                               | 否  |
| openPort    | string  | 若要测试带端口的应用，授予临时端口(默认不提供) | 否  |


### 销毁容器

```
GET /rmOS
```

#### 请求参数

| 参数名       | 类型    | 描述        | 必选 |
| ----------- | ------ | ----------- | --- |
| containerId | string | 容器标识码    | 是  |
| shareUrl    | string | 容器 Url 地址 | 是  |
| timestamp   | string | 当前时间戳    | 是  |

#### 返回

| 参数名      | 类型     | 描述              | 必选 |
| ---------- | ------- | ----------------- | --- |
| statusCode | integer | 状态码 (1, 2, 302) | 是   |
| message    | string  | 状态解读           | 是   |
