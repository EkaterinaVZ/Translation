from transformers import pipeline

translator = pipeline("translation_en_to_ru", "Helsinki-NLP/opus-mt-en-ru")
translator("Get team access controls and discussions for your contributors in an organization")