import streamlit as st
from youtube_loader import load_and_chunk_transcript
from summarizer import summarize_video

st.set_page_config(page_title="YouTube Video Summarizer", page_icon="📹", layout="wide")

st.title("YouTube Video Summarizer 🎥")
st.markdown("""
Welcome to the YouTube Video Summarizer! This tool uses advanced AI to create concise summaries of YouTube videos. 
Just paste the URL of the video you're interested in below, and hit summarize.
""")

with st.sidebar:
    st.header("Summarize a Video")
    video_url = st.text_input("Enter YouTube Video URL:")
    summarize_button = st.button("Summarize", key="summarize_sidebar")

if summarize_button:
    if video_url and "youtube.com" in video_url:
        try:
            with st.spinner("Summarizing... Please wait."):
                transcript_chunks = load_and_chunk_transcript(video_url)
                yt_summary = summarize_video(transcript_chunks)
                st.subheader("Summary")
                st.markdown(yt_summary)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a valid YouTube video URL.")
