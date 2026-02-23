# 🧹 Zero-Byte Cleaner — Python Automation Project

**Zero-Byte Cleaner** is a Python automation script that scans directories, detects empty (zero-byte) files, deletes them automatically, generates a detailed log report, and sends an email notification with the execution summary.

This project demonstrates practical automation concepts such as filesystem operations, scheduling, logging, and SMTP email integration.

---

## 📌 Project Overview

Large directories and servers often accumulate unused empty files that waste storage and create clutter.
Zero-Byte Cleaner automates the process of identifying and removing such files while maintaining execution logs and sending automated reports.

The script runs at scheduled intervals and can be executed from the command line.

---

## ⚙️ Features

* ✅ Recursive directory scanning using `os.walk()`
* ✅ Automatic deletion of zero-byte files
* ✅ Scheduled execution using `schedule`
* ✅ Detailed log report generation
* ✅ Email notification with report attachment
* ✅ Error tracking during deletion
* ✅ Command-line based execution

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **Modules Used:**

  * `os`
  * `sys`
  * `time`
  * `schedule`
  * `smtplib`
  * `email.message`

---

## 📂 Project Structure

```
zero-byte-cleaner/
│
├── ZeroByteCleaner.py      # Main automation script
├── README.md               # Project documentation
└── LogReport_*.txt         # Generated log reports
```

---

## 🚀 Installation

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/zero-byte-cleaner.git
cd zero-byte-cleaner
```

### 2️⃣ Install Required Dependency

```
pip install schedule
```

---

## ▶️ Usage

Run the script using:

```
python ZeroByteCleaner.py <DirectoryName> <TimeInterval>
```

### Example:

```
python ZeroByteCleaner.py Marvellous 1
```

**Arguments:**

* `DirectoryName` → Target directory to scan
* `TimeInterval` → Execution interval in minutes

---

## ⏱️ How It Works

1. The script scans the provided directory recursively.
2. Detects files with size `0 bytes`.
3. Deletes empty files safely.
4. Generates a timestamped log report.
5. Sends an email notification with the log file attached.

---

## 📧 Email Notification Setup

Before running the script, configure your email credentials using environment variables.

### Windows (Command Prompt)

```
set EMAIL_USER=your_email@gmail.com
set EMAIL_PASS=your_app_password
set EMAIL_RECEIVER=receiver_email@gmail.com
```

### Linux / macOS

```
export EMAIL_USER=your_email@gmail.com
export EMAIL_PASS=your_app_password
export EMAIL_RECEIVER=receiver_email@gmail.com
```

> ⚠️ Never commit real credentials to GitHub.

---

## 📝 Log Report

Each execution generates a report file:

```
LogReport_YYYY_MM_DD_HH_MM_SS.txt
```

Report includes:

* Total files scanned
* Empty files found
* Files deleted
* Errors encountered
* Execution timestamp

---

## 🧪 Example Output

```
Scan Complete
Mail sent successfully with attachment
Directory Scanned at : Mon Feb 23 14:10:02 2026
```

---

## 🔮 Future Enhancements

* Dry-Run Mode (preview before deletion)
* Backup folder instead of permanent deletion
* Advanced logging module integration
* Config file support (JSON/YAML)
* Real-time monitoring using watchdog

---

## 👨‍💻 Author

**Umesh Shivaji Bhabad**
📫 [umeshbhabad9@gmail.com](mailto:umeshbhabad9@gmail.com)

---

## ⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub!
