# Personal OpenClash rules

个人使用的 Mihomo/OpenClash 补充规则。只包含公开业务域名及公共服务 IP 匹配，不包含家庭设备、订阅、代理节点或认证信息。

`rules/` 为规则维护源；`manifest.json` 为迁移基线清单，记录初始数量和 SHA-256（后续编辑规则后需重生成清单）。规则采用 Mihomo rule-provider YAML `payload` 格式。策略组和规则优先顺序由使用方主配置决定。

## 使用方式

```yaml
rule-providers:
  local-openai-domain:
    type: http
    behavior: classical
    format: yaml
    url: https://raw.githubusercontent.com/orangebyy-cell/openclash-rules/main/rules/local-openai-domain.yaml
    path: ./rule_provider/local-openai-domain.yaml
    interval: 21600
    proxy: 自动选择
```

同名 provider 保留原有主规则位置和策略组。第三方社区规则继续使用原作者仓库，本仓库只维护个人补充部分。GitHub 更新后，OpenClash 在下一次成功更新时加载；已经下载的本地缓存可用于临时断网，但全新安装仍需要首次下载。

## 修改与回退

在 GitHub 编辑对应文件，保持 `payload` 列表及原有 `behavior` 兼容；提交前运行 `python scripts/validate.py`。需要回退时恢复相关文件的旧版本并提交，之后刷新对应 provider。修改策略组、规则顺序或节点仍须单独更新主配置。

本仓库由个人业务需求整理，规则归属判断可能需要随服务变化调整，不代表相关网站的安全性背书。
