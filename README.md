# MyFetch

**MyFetch** is a simple command-line utility written in Python that provides system information and enhances the display of key details. It's designed to be a minimalistic and customizable alternative to tools like `neofetch`.

## Features

- Display essential system information, including OS, release, hostname, and username.
- Show CPU usage and memory usage with color-coded output.
- Include storage information in GBs for better readability.
- Detect screen resolution and time zone.
- Optional network latency display, indicating whether the system is online/offline.

## Usage

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/SirSevrus/myfetch.git

## Adding MyFetch to System Path On Windows:

To make it even more convenient to use **MyFetch** across your system, you can easily add `myfetch.exe` to your system's PATH. Here's how:

1. Download the `add_to_path.exe` utility from the [releases page](https://github.com/SirSevrus/myfetch/releases).

2. Open a terminal or command prompt.

3. Navigate to the directory where you downloaded `add_to_path.exe`.

4. Run the following command:

   ```bash
   .\add_to_path.exe --add myfetch.exe
