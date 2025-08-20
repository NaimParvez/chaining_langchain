# chaining_langchain — LangChain Learning Project

## Overview
This repository contains my learning journey with **LangChain**, a framework for building applications with language models.  
The code and resources here are based on the [LangChain YouTube Playlist](https://youtube.com/playlist?list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0).  

This project serves as a collection of notes, code examples, and projects I build while following the tutorials to understand LangChain's capabilities, including chaining prompts, integrating with external tools, and building AI-powered applications.

---

## Purpose

- Document my progress in learning LangChain.  
- Provide working code examples for LangChain concepts like **chains, agents, memory, and embeddings**.  
- Serve as a reference for others learning LangChain or exploring its features.  

---

## Prerequisites

To run the code in this repository, you'll need:

- **Python 3.8 or higher**  
- **Virtual environment** (recommended)  
- Required Python packages (listed in `requirements.txt`)  

---

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/NaimParvez/chaining_langchain.git
   cd langchain-learning
   ````

2. **Set up a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **(Optional) Configure environment variables**
   Create a `.env` file for API keys (e.g., OpenAI, Hugging Face):

   ```bash
   echo "OPENAI_API_KEY=your-api-key" > .env
   ```



## How to Use

* Explore the `notebooks/` or `scripts/` folder for code corresponding to specific videos in the playlist.
* Each file is named to reflect the video or concept it covers (e.g., `01_basic_chain.ipynb` for the first tutorial).
* Follow the comments in the code for explanations of LangChain components.
* Run the scripts or notebooks after setting up the environment and API keys.

---

## Learning Resources

* 🎥 [YouTube Playlist: LangChain Tutorial Playlist](https://youtube.com/playlist?list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0)
* 📚 [LangChain Documentation](https://python.langchain.com/)
* 🐍 [Python Virtual Environment Setup Guide](https://docs.python.org/3/library/venv.html)

---

## Contributing

This is a **personal learning project**, but suggestions or improvements are welcome!

* Open an issue for bugs or questions.
* Submit a pull request with enhancements or additional examples.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
