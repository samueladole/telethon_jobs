
# 📦 Telethon Jobs

A **Telegram automation script** built with Python and **Telethon** to run scheduled jobs, filter messages, and send email notifications.  
This project is designed to help you automate tasks on Telegram using Telethon’s MTProto API.

---

## 🚀 Features

- 📨 **Email notifications** via `emailer.py`
- 📑 **Flexible message filtering** in `filters.py`
- 🤖 **Telegram job runner** in `main.py`
- 🛠️ Configurable with environment variables or config file
- 🔄 Designed to be scheduled (e.g., with cron or GitHub Actions)

---

## 🧩 Requirements

- Python 3.8+
- Telethon library (`pip install telethon`)
- [Telegram API credentials](https://my.telegram.org) (*api_id* and *api_hash*)
---

## 🛠️ Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/samueladole/telethon_jobs.git
   cd telethon_jobs