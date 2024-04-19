from langchain.document_loaders import YoutubeLoader
from langchain.text_splitter import TokenTextSplitter
import logging

def load_and_chunk_transcript(video_url):
    """Load YouTube video transcript and split into manageable chunks."""
    logging.info("Starting video transcript loading")
    yt_loader = YoutubeLoader.from_youtube_url(video_url)
    transcript = yt_loader.load()
    logging.info("Transcript loaded successfully")

    splitter = TokenTextSplitter(chunk_size=1000, chunk_overlap=100)
    return splitter.split_documents(transcript)