from Bot import ai

def translate_text(text, lang_code='si'):
    """
    Translates the given text to the target language using an external translation API.
    
    Args:
        text (str): The text to be translated.
        target_language (str): The language code to translate the text into.
        
    Returns:
        str: The translated text.
    """    
    response = ai.generate_content(f'Translate the following into native {lang_code}. Do not modify or translate any HTML tags, links (starting with http/https), or inline code. Only translate human-readable text. Return only the translated result of: "{text}"')
    return response.text
    
