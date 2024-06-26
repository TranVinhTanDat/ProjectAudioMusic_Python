# Music Player Application

The Music Player Application is a software designed for playing music files using PyQt5 and pygame libraries, along with additional dependencies such as ffmpeg, mysql-connector-python, mutagen, etc.

## Purpose
The purpose of the Music Player Application is to provide users with a convenient and efficient tool for playing their favorite music files. Users can easily navigate through their music library, create playlists, and enjoy their music collection with ease.

## Features
- **Playback Controls**: Users can play, pause, stop, and skip tracks using intuitive playback controls.
- **Playlist Management**: Users can create, edit, and delete playlists to organize their music collection.
- **Library Browser**: Users can browse through their music library and select songs to play.
- **Search Functionality**: Users can search for specific songs or artists within their music library.
- **Customization Options**: Users can customize the appearance and behavior of the application to suit their preferences.
## Introductory website
- Introductory website: [https://tranvinhtandat.github.io/WebMusicIntroduction/ ](https://tranvinhtandat.github.io/WebMusicIntroduction/)
## Download the Project
- **Clone the repository with the following**
- ```bash
  - git clone https://github.com/TranVinhTanDat/ProjectAudioMusic_Python.git

## System Requirements
- **Operating System**: The Music Player Application is compatible with Windows, macOS, and Linux operating systems.
- **Dependencies**: The application requires the installation of PyQt5, pygame, ffmpeg, mysql-connector-python, mutagen, and other dependencies. Please refer to the documentation for detailed installation instructions.
## System Requirements
    - Operating System: The Music Player Application is compatible with Windows, macOS, and Linux operating systems.
    - Dependencies: The application requires the installation of the following dependencies:
    - mysql-connector
    - mutagen
    - ffmpeg-python==0.2.0
    - mysql-connector-python
    - pygame
    - PyQt5==5.15.9
    - python-dotenv
    - requests
    - sip
    Please refer to the documentation for detailed installation instructions.
## Installation
### For Windows:
1. **Install Python 3.9.0 from the official Python website.**
2. **Install XAMPP and MySQL Server:**
   - Visit the Apache Friends website and download XAMPP.
   - Follow the on-screen instructions to install XAMPP and start MySQL Server.
3. **Configure MySQL Database Connection:**
   - Import the `musicplay.sql` file into MySQL.
   - Modify the connection parameters in the source code.
4. **Set up a virtual environment (optional but recommended):**
   - Create a virtual environment: `python -m venv myenv`
   - Activate the virtual environment: `myenv\Scripts\activate`
5. **Install dependencies from requirements.txt:**
   ```bash
   pip install -r requirements.txt
## After installing the required libraries, you can run the project successfully.

### For Linux (Ubuntu):
1. **Install Python 3.9.0 using pyenv:**
    - sudo apt update
    - sudo apt install -y git curl build-essential libssl-dev zlib1g-dev libbz2-dev
    libreadline-dev libsqlite3-dev llvm libncurses5-dev libncursesw5-dev
    xz-utils tk-dev libffi-dev liblzma-dev python-openssl
    - curl https://pyenv.run | bash
    - echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
    echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
    echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
    source ~/.bashrc
    - pyenv install 3.9.0

2. **Install XAMPP and MySQL Server (similar to Windows).**
3. **Configure MySQL Database Connection (similar to Windows).**
4. **Set up a virtual environment (optional but recommended):**
   - Create a virtual environment: python3 -m venv myenv
   - Activate the virtual environment: source myenv/bin/activate
4. **Install dependencies from requirements.txt:**
    ```bash  
    - pip install -r requirements.txt
## After installing the required libraries, you can run the project successfully.
## Download report latex
- [Tải xuống báo cáo LaTeX](https://drive.google.com/file/d/1x_45a2oFLvnSBh3TvFbir9Acx5BmwU0X/view?usp=sharing)

