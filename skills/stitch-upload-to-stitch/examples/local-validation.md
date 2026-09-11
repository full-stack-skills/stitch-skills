# 上传本地资产到 Stitch：本地应用验证

以下是完整的中文请求与预期响应契约，使用演示资料；不是远程执行记录。不调用 Stitch 写操作即可检索、模拟应用并审阅结果。

## 快速开始

输入：“上传脱敏的门店预约页 HTML。只用演示素材，先返回本地结果与验证范围。”

输出：离线 Markdown 输入 eA== → {screen:{htmlCode:{fileContentBase64:'eA==',mimeType:'text/markdown'},screenType:'DOCUMENT',isCreatedByClient:true,generatedBy:'UserUploadedDesignMd'}}。

验证：argv/日志/报告不含密钥、base64 或完整响应；若示例无远程环境，明确远程状态未执行。

## 典型场景

输入：“上传品牌 DESIGN.md 供系统创建；范围限当前需求。”

输出：按顺序列出从 STITCH_API_KEY 环境变量取凭据；不搜索其他客户端配置，不让用户把密钥粘到会话。 执行脚本前用 --help 核对参数；HTML title 使用路由，generated-by 使用实际生产者。 脚本通过 HTTPS 单次发送；禁止自动跟随重定向及重复写入，响应只输出下游所需标识。 最后返回已处理对象与来源，未运行的项目单列。

验证：PNG/HTML/Markdown 分别映射 screenshot/htmlCode。

## 高级场景

输入：“上传用户提供的演示稿 PNG；定制参数为title、generated-by、文件路径、经确认的 HTTPS 服务根地址。”

输出：保留所选参数、环境凭据；小输出 ID 交接；无自动重试和重定向，提供返回的 screen/instance 标识可用于后续流程的判据；假设不冒充实际配置。

## 异常处理

输入：“上传脱敏的门店预约页 HTML，但暂时缺少真实 projectId。”

输出：“先给本地假设草案。需要补充：真实 projectId，用于确定真实来源；未执行依赖该来源的写操作。”不返回空答复，也不伪造成功。

## 避免误触发与验证

输入：“远程套用设计系统，不扩大任务。”

输出：“使用stitch-manage-design-system；交接当前素材和请求，当前入口不执行额外动作。”

检查：以上五种请求分别检索快速、典型、高级、失败、边界路径；检查输出中的 ID、token、运行结论是否均有输入/回执依据。此人工应用检查不等价于独立模型触发率统计。
