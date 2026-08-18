# Guide to FFmpeg installation

In this file you can find full manual, how to install FFmpeg on any OS.

### Windows

To install FFmpeg, open PowerShell app and type following command:

```powershell
winget install ffmpeg
```

...and wait for the command to finish its work.

### MacOS

Open Terminal and type:

```zsh
brew install ffmpeg
```

when command finished its work, FFmpeg is install and ready to work!

### Linux

On Linux, use command specific for your distro:

```bash
# Ubuntu/Debian
sudo apt install ffmpeg
# Fedora/RHEL
sudo dnf install ffmpeg
# Arch
sudo pacman -S ffmpeg
```

### FreeBSD

Use the following command:

```tcsh
pkg install ffmpeg
```

### Android (Termux)

Use the following command:

```bash
pkg install ffmpeg
```