# 🧹 Zero-Byte Cleaner — Python Automation Project

A lightweight **Python automation tool** that scans directories and automatically removes empty (zero-byte) files.
This project demonstrates filesystem automation, scheduling, logging, and **email notification alerts** using Python.

---

## 📌 Project Overview

**Zero-Byte Cleaner** is designed to maintain server hygiene by detecting and deleting unused empty files.
It runs on a scheduled interval, generates log reports, and sends email notifications after execution.

This automation is useful for:

* Server maintenance
* Cleaning temporary directories
* Log and build artifact cleanup
* Automated filesystem monitoring
* Learning Python-based DevOps automation

---

## ⚙️ Features

* ✅ Recursive directory scanning using `os.walk()`
* ✅ Automatic deletion of zero-byte files
* ✅ Scheduled execution using `schedule`
* ✅ Timestamp-based log file generation
* ✅ **Email notification after scan completion**
* ✅ Command-line execution
* ✅ Lightweight and customizable automation

---

## 📧 Email Notification Feature

The script sends an automated email summary containing:

* Total files scanned
* Empty files detected
* Files deleted
* Execution timestamp
* Log file details

This helps monitor automation remotely without manually checking logs.

Typical use cases:

* Server administrators receiving cleanup reports
* Automated maintenance alerts
* Remote monitoring of filesystem activity

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **Modules Used:**

  * `os`
  * `sys`
  * `time`
  * `schedule`
  * `smtplib` *(for email notifications)*
  * `email.mime` *(for formatted email content)*

---

## 📂 Project Structure

```
zero-byte-cleaner/
│
├── cleaner.py        # Main automation script
├── README.md         # Project documentation
└── logs/             # Generated log files (optional)
```

---

## 🚀 Installation

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/zero-byte-cleaner.git
cd zero-byte-cleaner
```

### 2️⃣ Install Dependencies

```
pip install schedule
```

---

## ▶️ Usage

Run the script by providing the target directory as an argument:

```
python cleaner.py <directory_name>
```

Example:

```
python cleaner.py Marvellous
```

The script will:

1. Scan the given directory.
2. Detect empty files.
3. Delete zero-byte files automatically.
4. Generate a log file.
5. Send an email notification with execution details.

---

## ⏱️ Scheduling Behavior

Currently, the automation runs:

```
Every 1 minute
```

You can modify this inside the script:

```
schedule.every(1).minute.do(DirectoryScanner)
```

---

## 📝 Log Output

A log file is generated for every execution containing:

* Total files scanned
* Number of empty files found
* Execution timestamp

Example log name:

```
Marvellous_Mon_Feb_19_12_30_00_2026.log
```

---

## 🔐 Email Configuration (Setup Required)

Before running the script, configure:

* Sender email address
* Receiver email address
* SMTP server settings
* App password or authentication credentials

Example SMTP providers:

* Gmail SMTP
* Outlook SMTP
* Custom Mail Server

> ⚠️ Do not commit real passwords or credentials to GitHub.
> Use environment variables or configuration files instead.

---

## 🔮 Future Improvements (Planned Upgrades)

* Dry-Run Mode (Preview before deletion)
* Backup/Recycle Folder Support
* Advanced Logging using `logging` module
* CLI arguments using `argparse`
* Real-time monitoring with `watchdog`
* Multi-directory scanning
* Docker container support

---

## 🤝 Contributing

Contributions, ideas, and improvements are welcome.
Feel free to fork the repository and submit a pull request.

---

## 👨‍💻 Author

**Umesh Bhabad**
📫 [umeshbhabad9@gmail.com](mailto:umeshbhabad9@gmail.com)

---

## ⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub!
