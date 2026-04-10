# 🦁 Juumla
<div align="center">
    <img width="2266" height="1116" alt="image" src="https://github.com/user-attachments/assets/66bbf6b1-fa38-425b-bcb2-0395175a0a0c" />
</div>

<br>

<p align="center">
    <img src="https://img.shields.io/github/license/oppsec/juumla?color=yellow&logo=github&style=for-the-badge">
    <img src="https://img.shields.io/github/issues/oppsec/juumla?color=yellow&logo=github&style=for-the-badge">
    <img src="https://img.shields.io/github/stars/oppsec/juumla?color=yellow&label=STARS&logo=github&style=for-the-badge">
    <img src="https://img.shields.io/github/languages/code-size/oppsec/juumla?color=yellow&logo=github&style=for-the-badge">
</p>

___

<br>

<p> 🦁 <b>Juumla</b> Juumla is a python tool created to identify Joomla version, scan for vulnerabilities and sensitive files. </p>

[![Starlog](https://img.shields.io/badge/Starlog-Deep_Dive-00e5ff?style=flat&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0xMiAyTDkgOUgyTDcgMTRMNSAyMkwxMiAxN0wxOSAyMkwxNyAxNEwyMiA5SDE1TDEyIDJaIi8+PC9zdmc+)](https://starlog.is/articles/cybersecurity/0xdsm-juumla)

<br>

## ⚡ Installing / Getting started

<p> A quick guide on how to install and use Juumla. </p>

```
1. Clone the repository - git clone https://github.com/oppsec/juumla.git
2. Install the libraries - pip3 install -r requirements.txt
3. Run Juumla - python3 main.py -u https://example.com
```

<br>

### 🐳 Docker
If you want to run Juumla in a Docker container, follow these commands:

```
1. Clone the repository - git clone https://github.com/oppsec/juumla.git
2. Build the image - sudo docker build -t juumla:latest .
3. Run container - sudo docker run juumla:latest
```

If you want to create an Joomla environment in a Docker container, follow these commands:
```
1. Clone the repository - git clone https://github.com/oppsec/juumla.git (or download the docker-compose.yml file)
2. Install docker-compose (e.g: sudo apt install docker-compose)
3. sudo docker-compose up
4. Access http://localhost:8080/

The default root password is: example
The default database name is: joomladb
The default DBMS is: MySQL 5.6
```

<br><br>

### ⚙️ Pre-requisites
- [Python 3](https://www.python.org/downloads/) installed on your machine.
- Install the libraries with `pip3 install -r requirements.txt`

<br><br>

### ✨ Features
- Fast scan
- Low RAM and CPU usage
- Detect Joomla version
- Find config and backup files
- Scan for vulnerabilities based on the Joomla version
- Open-Source

<br><br>

### 📚 To-Do
- [ ] Update vulnerabilities database
- [x] Improve Joomla detection methods
- [x] Improve code optimization

<br><br>

### 🔨 Contributing

A quick guide on how to contribute to the project.

```
1. Create a fork from Juumla repository
2. Download the project with git clone https://github.com/your/juumla.git
3. Make your changes
4. Commit and makes a git push
5. Open a pull request
```

<br><br>

### ⚠️ Warning
- The developer is not responsible for any malicious use of this tool.
