#!/usr/bin/env python

#	Copyright 2013 AlchemyAPI
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


from __future__ import print_function
from alchemyapi import AlchemyAPI
import json


demo_text = 'Yesterday dumb Bob destroyed my fancy iPhone in beautiful Denver, Colorado. I guess I will have to head over to the Apple Store and buy a new one.'
demo_url = 'http://www.npr.org/2013/11/26/247336038/dont-stuff-the-turkey-and-other-tips-from-americas-test-kitchen'
demo_html = '<html><head><title>Python Demo | AlchemyAPI</title></head><body><h1>Did you know that AlchemyAPI works on HTML?</h1><p>Well, you do now.</p></body></html>'
image_url = 'http://demo1.alchemyapi.com/images/vision/football.jpg'

print('')
print('')
print(
    '            ,                                                                                                                              ')
print(
    '      .I7777~                                                                                                                              ')
print(
    '     .I7777777                                                                                                                             ')
print(
    '   +.  77777777                                                                                                                            ')
print(
    ' =???,  I7777777=                                                                                                                          ')
print(
    '=??????   7777777?   ,:::===?                                                                                                              ')
print(
    '=???????.  777777777777777777~         .77:    ??           :7                                              =$,     :$$$$$$+  =$?          ')
print(
    ' ????????: .777777777777777777         II77    ??           :7                                              $$7     :$?   7$7 =$?          ')
print(
    '  .???????=  +7777777777777777        .7 =7:   ??   :7777+  :7:I777?    ?777I=  77~777? ,777I I7      77   +$?$:    :$?    $$ =$?          ')
print(
    '    ???????+  ~777???+===:::         :7+  ~7   ?? .77    +7 :7?.   II  7~   ,I7 77+   I77   ~7 ?7    =7:  .$, =$    :$?  ,$$? =$?          ')
print(
    '    ,???????~                        77    7:  ?? ?I.     7 :7     :7 ~7      7 77    =7:    7  7    7~   7$   $=   :$$$$$$~  =$?          ')
print(
    '    .???????  ,???I77777777777~     :77777777~ ?? 7:        :7     :7 777777777:77    =7     7  +7  ~7   $$$$$$$$I  :$?       =$?          ')
print(
    '   .???????  ,7777777777777777      7=      77 ?? I+      7 :7     :7 ??      7,77    =7     7   7~ 7,  =$7     $$, :$?       =$?          ')
print(
    '  .???????. I77777777777777777     +7       ,7???  77    I7 :7     :7  7~   .?7 77    =7     7   ,77I   $+       7$ :$?       =$?          ')
print(
    ' ,???????= :77777777777777777~     7=        ~7??  ~I77777  :7     :7  ,777777. 77    =7     7    77,  +$        .$::$?       =$?          ')
print(
    ',???????  :7777777                                                                                77                                       ')
print(
    ' =?????  ,7777777                                                                               77=                                        ')
print(
    '   +?+  7777777?                                                                                                                           ')
print(
    '    +  ~7777777                                                                                                                            ')
print(
    '       I777777                                                                                                                             ')
print(
    '          :~                                                                                                                               ')


# Create the AlchemyAPI Object
alchemyapi = AlchemyAPI()

print('')
print('')
print('############################################')
print('#   Entity Extraction Example              #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.entities('text', demo_text, {'sentiment': 1})

if response['status'] == 'OK':
    print('## Response Object ##')
    print(json.dumps(response, indent=4))

    print('')
    print('## Entities ##')
    for entity in response['entities']:
        print('text: ', entity['text'].encode('utf-8'))
        print('type: ', entity['type'])
        print('relevance: ', entity['relevance'])
        print('sentiment: ', entity['sentiment']['type'])
        if 'score' in entity['sentiment']:
            print('sentiment score: ' + entity['sentiment']['score'])
        print('')
else:
    print('Error in entity extraction call: ', response['statusInfo'])


print('')
print('')
print('')
print('############################################')
print('#   Keyword Extraction Example             #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.keywords('text', demo_text, {'sentiment': 1})

if response['status'] == 'OK':
    print('## Response Object ##')
    print(json.dumps(response, indent=4))

    print('')
    print('## Keywords ##')
    for keyword in response['keywords']:
        print('text: ', keyword['text'].encode('utf-8'))
        print('relevance: ', keyword['relevance'])
        print('sentiment: ', keyword['sentiment']['type'])
        if 'score' in keyword['sentiment']:
            print('sentiment score: ' + keyword['sentiment']['score'])
        print('')
else:
    print('Error in keyword extaction call: ', response['statusInfo'])


print('')
print('')
print('')
print('############################################')
print('#   Concept Tagging Example                #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.concepts('text', demo_text)

if response['status'] == 'OK':
    print('## Object ##')
    print(json.dumps(response, indent=4))

    print('')
    print('## Concepts ##')
    for concept in response['concepts']:
        print('text: ', concept['text'])
        print('relevance: ', concept['relevance'])
        print('')
else:
    print('Error in concept tagging call: ', response['statusInfo'])


print('')
print('')
print('')
print('############################################')
print('#   Sentiment Analysis Example             #')
print('############################################')
print('')
print('')

print('Processing html: ', demo_html)
print('')

response = alchemyapi.sentiment('html', demo_html)

if response['status'] == 'OK':
    print('## Response Object ##')
    print(json.dumps(response, indent=4))

    print('')
    print('## Document Sentiment ##')
    print('type: ', response['docSentiment']['type'])

    if 'score' in response['docSentiment']:
        print('score: ', response['docSentiment']['score'])
else:
    print('Error in sentiment analysis call: ', response['statusInfo'])


print('')
print('')
print('')
print('############################################')
print('#   Targeted Sentiment Analysis Example    #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.sentiment_targeted('text', "vexatious", 'vexatious')

if response['status'] == 'OK':
    print('## Response Object ##')
    print(json.dumps(response, indent=4))

    print('')
    print('## Targeted Sentiment ##')
    print('type: ', response['docSentiment']['type'])

    if 'score' in response['docSentiment']:
        print('score: ', response['docSentiment']['score'])
else:
    print('Error in targeted sentiment analysis call: ',
          response['statusInfo'])
