from langchain.llms import GooglePalm
from langchain.chains.summarize import load_summarize_chain
import logging
from config import get_api_key

def summarize_video(transcript_chunks):
    """Summarize the provided chunks using Google PALM."""
    api_key = get_api_key()
    llm = GooglePalm(google_api_key=api_key, temperature=0.6)
    summarize_chain = load_summarize_chain(llm=llm, chain_type="refine")
    summary = summarize_chain.run(transcript_chunks)
    logging.info("Summarization complete")
    return summary