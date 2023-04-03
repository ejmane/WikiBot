import openai
import wikipedia
import os
import youtube_transcript_api

# pass the api key
openai.api_key = os.environ.get('OPENAI_API_KEY')

# get user input
title = input('Title of the page: ')

# Get the wikipedia content
page = wikipedia.page(title=title, auto_suggest = False)

# define prompt
prompt = 'Write a summary of the following article: ' + page.content[:10000]
messages = []
messages.append({'role': 'user', 'content': prompt})

try:
    # make an api call
    response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=messages)

    # print the response
    print(response.choices[0].message.content)
    print("==================")
    print("Token usage =", response.usage.total_tokens)
    print("==================")

# authentication issue
except openai.error.AuthenticationError:
    print('no valid token / authentication error')

except openai.error.InvalidRequestError as e:
    print('invalid request, read the manual')
    print(e)