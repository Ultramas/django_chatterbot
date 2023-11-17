from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
import spacy


chatterbot = ChatBot('Example ChatterBot')
trainer = ListTrainer(chatterbot)

trainer.train([
    "Hi",
    "Hello",
    "How are you?",
    "I am good.",
    "That is good to hear.",
    "Thank you",
    "You are welcome.",
])

from gtts import gTTS
from io import BytesIO
import os

from django.http import FileResponse, HttpResponse


class ChatterBotView(views.APIView):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        data = {
            'error': 'You should make a POST request to this endpoint.'
        }
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        input_statement = request.data.get('text')
        response_statement = chatterbot.get_response(input_statement)
        response_data = {
            'text': response_statement.text,
            'confidence': response_statement.confidence,
            # include all attributes that you want to serialize
        }

        # Store the response text in the session data
        request.session['response_text'] = response_statement.text

        return Response(response_data, status=status.HTTP_200_OK)

from django.views import View
from gtts import gTTS
from io import BytesIO
from django.http import HttpResponse


class AudioView(View):
    def get(self, request, *args, **kwargs):
        # Get the text to be converted to speech from the session data
        text = request.session.get('response_text', 'Hello, world!')

        # Convert the text to speech
        tts = gTTS(text, lang='en')
        mp3_fp = BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)

        # Create a response with the audio file
        response = HttpResponse(mp3_fp.read(), content_type='audio/mpeg')

        # No need to read from mp3_fp again
        return response
