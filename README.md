# YouTube Video Summarizer
YouTube Video Summarizer is a Python tool that leverages LangChain and Google PALM to automatically generate concise summaries of YouTube videos. This application uses advanced natural language processing techniques to extract meaningful information from video transcripts, providing users with quick insights without watching the entire content.

<img src="https://github.com/SejalKankriya/youtube-video-summarizer/assets/43418191/09ec05c1-1c07-4b85-b773-b12bea6908ff" width="60%" height="60%">


## Features
- Extracts video transcripts directly from YouTube URLs.
- Utilizes Google PALM through the LangChain library to summarize text.
- Handles large transcripts by splitting text into manageable chunks.

## Prerequisites

  * **Python 3.6+:** Ensure you have Python 3.6 or higher installed on your machine.
  * **Google Cloud Platform Account:** You need to have a Google Cloud Platform account with a project set up and an API Key enabled for accessing Google PALM services. Follow the instructions [here](https://cloud.google.com/docs/authentication/getting-started) to set up your account and project.
  * **Google API Key:** Obtain your API key by visiting [Google AI Studio API Key page](https://aistudio.google.com/app/apikey). This key will be used to authenticate your requests to Google PALM.

## Installation

  1. **Clone the Repository**

     ```bash
     git clone https://github.com/yourusername/youtube-video-summarizer.git
     cd youtube-video-summarizer
     ```

  2. **Set up a Virtual Environment** (Optional but recommended)

     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scripts\activate`
     ```

  3. **Install Dependencies**

     ```bash
     pip install -r requirements.txt
     pip install --no-deps google-generativeai
     ```

  4. **Environment Variables**
     - Create a .env file in the root directory of your project.
     - Add your Google API key to the .env file:

       ```bash
       GOOGLE_API_KEY=your_google_api_key_here
       ```

## Usage

Execute the the following command:
```bash
streamlit run main.py
````

Navigate to the provided local URL displayed in your command prompt or terminal to access the web interface. Enter a YouTube video URL into the input field and click the "Summarize" button to see the summary.

**Note**: The Google PALM LLM is presently in a research preview stage, which means access to the API could be restricted. Please ensure you adhere to Google's guidelines during this phase.
