# HorseAI

<p align="center">
  <img src="assets/banner.png" alt="HorseAI Banner" width="100%">
</p>

<p align="center">
  <strong>A modern local AI chat application powered by WebLLM and WebGPU.</strong>
</p>

<p align="center">
  Run large language models directly in your browser with no backend required.
</p>

<p align="center">
  <a href="https://github.com/TheNotMichi/HorseAI/stargazers">
    <img src="https://img.shields.io/github/stars/TheNotMichi/HorseAI?style=for-the-badge" alt="Stars">
  </a>
  <a href="https://github.com/TheNotMichi/HorseAI/network/members">
    <img src="https://img.shields.io/github/forks/TheNotMichi/HorseAI?style=for-the-badge" alt="Forks">
  </a>
  <a href="https://github.com/TheNotMichi/HorseAI/issues">
    <img src="https://img.shields.io/github/issues/TheNotMichi/HorseAI?style=for-the-badge" alt="Issues">
  </a>
  <img src="https://img.shields.io/badge/WebGPU-Required-orange?style=for-the-badge" alt="WebGPU">
  <img src="https://img.shields.io/badge/WebLLM-Powered-blue?style=for-the-badge" alt="WebLLM">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="MIT">
</p>

---

## Overview

HorseAI is a local AI chat application built with **WebLLM**, allowing large language models to run directly in the browser using **WebGPU**.

The application provides a modern interface with support for multiple conversations, multiple models, streaming responses, and persistent chat history while keeping all processing on the user's device.

## Features

* Modern and responsive interface
* Multi-chat support
* Multiple AI models
* Real-time streaming responses
* Automatic conversation history
* Local execution using WebGPU
* No backend server required
* Custom WebLLM model support
* Automatic model loading
* Fast and lightweight launcher

## Screenshots

<p align="center">
  <img src="assets/screenshot.png" alt="HorseAI Screenshot" width="90%">
</p>

## Installation

Clone the repository:

```bash
git clone https://github.com/TheNotMichi/HorseAI.git
cd HorseAI
```

Run the launcher:

```bash
python launch.py
```

The launcher will automatically:

* Start a local HTTP server
* Open your default web browser
* Load HorseAI

## Requirements

* Python 3.8 or newer
* A browser with WebGPU support
* Windows, Linux or macOS

## Project Structure

```text
HorseAI/
│
├── launch.py
├── source.html
├── assets/
│   ├── banner.png
│   └── screenshot.png
│
├── LICENSE
└── README.md
```

## Technologies

* HTML5
* CSS3
* JavaScript (ES Modules)
* WebLLM
* WebGPU
* Tailwind CSS
* Python

## Roadmap

* [x] Multi-chat support
* [x] Multiple AI models
* [x] Streaming responses
* [x] Local execution
* [x] Custom model support
* [ ] Markdown rendering
* [ ] File attachments
* [ ] Voice input
* [ ] Image understanding
* [ ] Plugin system

## License

This project is licensed under the MIT License.

---

<p align="center">
Developed by <strong>TheNotMichi</strong>
</p>
