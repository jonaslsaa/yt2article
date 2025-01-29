def transcript_prompt(transcript: str) -> str:
    return f"""<Transcript>
{transcript}
</Transcript>
Transcription note: this automated transcript might not be 100% correct, you can correct it where it makes sense.

Can you provide a comprehensive article/summary of the given text? The article should cover all the key points and main ideas presented in the original text, while also condensing the information into a concise and easy-to-understand format. Please ensure that the summary includes relevant details and examples that support the main ideas, while avoiding any unnecessary information or repetition. The length of the summary should be appropriate for the length and complexity of the original text, providing a clear and accurate overview without omitting any important information.
Format it as an personal article (as it were written by the author), take inspiration from the transcript. If it makes sense, format it as a "story" to be captivating (dont call it a story tho). Use bold and italics where it makes sense.
Make it VERY long to make sure EVERYTHING is covered. You can skip irrelevant stuff (like sponsor or repetative parts)

At the end add a "TLDR" part (objective on what the video was about, must naturally integrate the key parts which makes this video interesting - do NOT use markdown lists, DO **enbolden** keywords, use a markdown section)."""