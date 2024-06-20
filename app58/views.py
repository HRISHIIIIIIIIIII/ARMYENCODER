# app58/views.py
from django.shortcuts import render
from datetime import datetime

def encode_message(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        today = datetime.now().day
        encoded_message = ''
        for char in message:
            if char.isalpha():
                if today % 2 == 0:  # Even day
                    encoded_message += str(500 + ord(char.upper()) - ord('A') + 1).zfill(3)
                else:  # Odd day
                    encoded_message += str(ord(char.upper()) - ord('A') + 1).zfill(2)
            else:
                encoded_message += char
        return render(request, 'app58/encoded_message.html', {'encoded_message': encoded_message})

    return render(request, 'app58/encode_message.html')
