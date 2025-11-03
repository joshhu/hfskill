# HFSkill - Hugging Face Spaces 管理工具包

一個全面的命令列工具包，用於管理和操作 Hugging Face Spaces。本工具提供了易於使用的操作功能，透過 Python 腳本來列出、監控和控制 Hugging Face Spaces。

## 功能特色

- **列出 Spaces**：依作者或關鍵字搜尋和過濾 Spaces
- **Space 資訊**：取得任何 Space 的詳細元數據
- **執行環境管理**：重新啟動或暫停 Spaces
- **狀態監控**：檢查 Space 執行環境狀態和硬體配置
- **使用者 Spaces**：列出特定使用者擁有的所有 Spaces

## 安裝方式

1. 複製此倉庫：
```bash
git clone https://github.com/joshhu/hfskill.git
cd hfskill
```

2. 安裝相依套件：
```bash
pip install huggingface_hub
```

## 身份驗證

大多數操作需要 Hugging Face 存取權杖。使用以下其中一種方法配置身份驗證：

### 選項 1：環境變數（建議）
```bash
export HF_TOKEN="hf_your_token_here"
```

### 選項 2：命令列參數
```bash
python3 scripts/space_operations.py --token "hf_your_token_here" <command>
```

**權杖需求：**
- 讀取操作：公開 Spaces 可選擇性提供權杖
- 寫入操作（重新啟動/暫停）：必須提供具有寫入權限的權杖

## 使用方法

### 列出 Spaces
```bash
# 列出最近的 Spaces
python3 scripts/space_operations.py list --limit 10

# 列出特定作者的 Spaces
python3 scripts/space_operations.py list --author stabilityai

# 搜尋 Spaces
python3 scripts/space_operations.py list --search "chatbot"
```

### 取得 Space 資訊
```bash
python3 scripts/space_operations.py info stabilityai/stable-diffusion
```

### 重新啟動 Space
```bash
python3 scripts/space_operations.py restart myusername/my-space
```

### 暫停 Space
```bash
python3 scripts/space_operations.py pause myusername/my-space
```

### 取得 Space 執行狀態
```bash
python3 scripts/space_operations.py runtime stabilityai/stable-diffusion
```

### 列出使用者的 Spaces
```bash
python3 scripts/space_operations.py user stabilityai
```

## Space ID 格式

所有 Spaces 使用以下格式識別：`username/space-name`

範例：
- `stabilityai/stable-diffusion`
- `openai/whisper`
- `meta-llama/llama-2-chat`

## 常用工作流程

### 監控並重新啟動 Space
```bash
# 檢查 Space 狀態
python3 scripts/space_operations.py runtime myusername/my-space

# 如有需要則重新啟動
python3 scripts/space_operations.py restart myusername/my-space
```

### 搜尋並探索 Spaces
```bash
# 搜尋聊天機器人 Spaces
python3 scripts/space_operations.py list --search "chatbot" --limit 20

# 取得詳細資訊
python3 scripts/space_operations.py info username/interesting-space
```

## 專案結構

```
hfskill/
├── SKILL.md                    # 詳細技能文件
├── README.md                   # 本檔案
├── scripts/
│   └── space_operations.py     # 主要執行腳本
└── references/
    └── spaces_reference.md     # API 參考文件
```

## 錯誤處理

常見錯誤及解決方案：

- **"No HF_TOKEN found"**：設定環境變數或傳入 `--token`
- **401 Unauthorized**：權杖無效或已過期
- **403 Forbidden**：權限不足或非 Space 擁有者
- **404 Not Found**：Space 不存在或為私有
- **429 Too Many Requests**：超過速率限制，請稍後重試

## 文件

有關 Space 狀態、硬體選項和 API 詳細資訊，請參閱：
- `SKILL.md` - 完整技能文件
- `references/spaces_reference.md` - API 參考

## 系統需求

- Python 3.6+
- `huggingface_hub` 套件

## 授權

MIT License

## 貢獻

歡迎貢獻！請隨時提交 Pull Request。
