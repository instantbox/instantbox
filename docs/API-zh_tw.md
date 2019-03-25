<p align="right">繁體中文 | <a href="./API-zh_.md">简体中文</a></p>

# instantbox 服務API文件

文件版本：0.0.3

修訂歷史：

- 0.0.1：初稿 2018/12/11

- 0.0.2：修改狀態碼 2018/12/11

- 0.0.3：修改 webshell 生成方式，改進 API，支持 Ubuntu/CentOS/Alpine 的大部分鏡像 2018/12/18

  主要改進如下:

  ​	1. API 從 <font color=#DC143C>/v1/superspire/</font> -> <font color=#DC143C>/v2/superinspire/</font>

  ​	2. 支援 Ubuntu 14.04~18.04, CentOS6.10, CentOS7, Alpine latest

  ​	3. 支援 nginx 頻率控制，預設返回 503 錯誤


## API請求方式說明

- 目前所有的提交類接口僅支援 POST 方式，查詢類接口僅支援 GET 方式 [暫時都開放]
- 所有參數在傳入時應當使用：**UTF-8 編碼**


### 請求的URL

格式：
```
/v2/superinspire/{relative_path}?{query_string}
```

舉例：
```
/v2/superinspire/getOS?os=10000
```

### 參數說明

| **參數名稱** | **描述** |
| ----------- | ------- |
| relative_path | API 操作相對路徑，如：`getOS` |
| query_string  | 放在 HTTP header傳入的參數，必須經過 UrlEncode 編碼 |

### HTTP GET 和 POST 方式使用說明

| 請求方式  | GET | POST |
| -------- | --- | ---- |
| URL | `/v2/superinspire/{relative_path}?{query_string}` | `/v2/superinspire/{relative_path}?{query_string}` |
| 請求參數 | 全部攜帶在 HTTP 請求header的 query_string 中。 | 既可攜帶在 query_string 中，也可攜帶在 HTTP Body 中。攜帶在 query_string 中的參數的值，必須進行 UrlEncode 編碼；  攜帶在 HTTP Body 中的參數，則不需要進行 UrlEncode 編碼。 |
| HTTP BODY | 不攜帶 HTTP Body | multipart/form-data |

註：

- 如果 HTTP Body 和 query_string 存在相同的參數，則以 query_string 中的參數為準。
- HTTP URL 長度有限，若參數值長度過長，建議將參數放在 HTTP Body 中進行傳輸


### API 回應格式說明

|           | 正常請求 | 異常請求 |
| --------- | ------- | ------- |
| HTTP狀態碼 | 1 OK | 4** : 用戶請求錯誤。 5** : server 服務失敗。 |
| HTTP BODY | API 響應內容。除特殊說明外，為 JSON 字符串，例如：`{"statusCode":1, "message": "SUCCESS"}` | JSON 字符串，例如：`{"statusCode":404, "message": "Not support OS!"}` |


## 狀態碼

**狀態碼**用於指示錯誤類型。即：回應體(json 格式)的 `statusCode` 字段。

| 狀態碼 (statusCode) | 描述        |
| ------------------ | ---------- |
| 1                  | 操作執行成功 |
| 0                  | 操作執行失敗 |


## API列表

### 容器列表

```
GET /getOSList
```

#### 請求參數

| 參數名 | 類型 | 描述 | 必選 |
| ----- | --- | ---- | --- |
| 無    | 無   | 無   | 無  |

#### 返回

| 參數名    | 類型      | 必選 |
| -------- | -------- | --- |
| json 數據 | json 類型 | 是  |

返回範例
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

#### 請求參數

| 參數名   | 類型          | 描述                                     | 必選  | 例子       |
| ------- | ------------ | ---------------------------------------- | ---- | ---------- |
| os      | string       | 指定系統請求編碼                            | 是   | 10000      |
| timeout | string       | 容器最長存活時間時間戳 [當前時間戳+存活時間長度] | 否   | 1544514176 |
| cpu     | string(Core) | 請求給予 CPU 資源使用限制                    | 否   | 1          |
| mem     | string(MB)   | 請求給予內存資源使用限制                      | 否   | 512        |
| port    | string       | 開放的Port，目前只允許開放一個Port              | 否   | 80         |

#### 返回

| 參數名       | 類型     | 描述                                    | 必選 |
| ----------- | ------- | --------------------------------------- | --- |
| statusCode  | integer | 狀態碼 (1, 302, 403, 404)                | 是  |
| message     | string  | 狀態解讀                                 | 是  |
| shareUrl    | string  | 容器 Url 地址                            | 否  |
| containerId | string  | 容器標識碼                               | 否  |
| openPort    | string  | 若要測試帶Port的應用，給予臨時Port(預設不提供) | 否  |


### 刪除容器

```
GET /rmOS
```

#### 請求參數

| 參數名       | 類型    | 描述        | 必選 |
| ----------- | ------ | ----------- | --- |
| containerId | string | 容器標識碼    | 是  |
| shareUrl    | string | 容器 Url 地址 | 是  |
| timestamp   | string | 當前時間戳    | 是  |

#### 返回

| 參數名      | 類型     | 描述              | 必選 |
| ---------- | ------- | ----------------- | --- |
| statusCode | integer | 狀態碼 (1, 2, 302) | 是   |
| message    | string  | 狀態解讀           | 是   |

