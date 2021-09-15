from django.shortcuts import render
from django.http import HttpResponse

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create your views here.

bot = ChatBot('chatbot', read_only=False, logic_adapters=['chatterbot.logic.BestMatch'])

stress = [
    "For each question choose from the following alternatives:<br>never<br>almost never<br>sometimes<br>fairly often<br>very often",
    "1. In the last month, how often have you been upset because of something that happened unexpectedly?",
    "2. In the last month, how often have you felt that you were unable to control the important things in your life?",
    "3. In the last month, how often have you felt nervous and stressed?",
    "4. In the last month, how often have you felt confident about your ability to handle your personal problems?",
    "5. In the last month, how often have you felt that things were going your way?",
    "6. In the last month, how often have you found that you could not cope with all the things that you had to do?",
    "7. In the last month, how often have you been able to control irritations in your life?",
    "8. In the last month, how often have you felt that you were on top of things?",
    "9. In the last month, how often have you been angered because of things that happened that were outside of your control?",
    "10. In the last month, how often have you felt difficulties were piling up so high that you could not overcome them?",
    ""
]

anxiety = [
    "For each question choose from the following alternatives:<br>never<br>almost never<br>sometimes<br>fairly often<br>very often",
    "1. Do you feel calm ?",
    "2. Do you feel secure ?",
    "3. Do you feel satisfied with yourself ?",
    "4. Do you feel comfortable ?",
    "5. Do you feel happy ?",
    "6. Do you feel content ?",
    "7. Do you feel pleasant ?",
    "8. Do you make decisions easily ?",
    "9. Can you concentrate on minute things without facing much difficulty ?",
    "10. Do you take part in social gatherings and try to join them often ?",
    ""
]

answer = [
    "Suggestions:<br>1. Can be performed right now! (For bot stress and anxiety)<br>2. Relaxation Exercise (take a deep breath, hold it for 5 counts, release it, repeat for 5 times)<br>3. Mediation (soothing music should play, in the background let a person guide the user: sit/lay down, close your eyes, try focusing on the middle area of your eyebrows and imagine a white spot, keep focusing, if you lose focus try regaining back focus)<br>4. Tea for stress/anxiety (Chamomile, Green, Rose, Peppermint, Lavender Tea)<br>5. Try Affirmations (say it out in a mild tone once, next say it out aloud in front of the mirror preferably)<br>I am calm<br>I am loved<br>I am in control<br>This too shall pass<br>I am blessed",
    "Suggestions:<br>1. Declutter your personal space regularly<br>2. Practice Journal writing everyday for 5 mins (you can incorporate a timer in the app to remind the user in a notification)<br>3. Set a daily schedule of your daily plan (which should include 8hrs sleep) (day planner can be incorporated)<br>4. Take out 15 mins to exercise everyday (a reminder can be incorporated)<br>5. Cut down on caffeine intake (to 1/day) and nicotine intake<br>6. Morning affirmations (try from the affirmations above)<br>7. Take out 15 mins for meditation (a reminder can be incorporated)<br>8. You can try engaging in your hobbies regularly",
    "Suggestions:<br>1. Declutter your personal space regularly<br>2. Practice Journal writing everyday for 5 mins (you can incorporate a timer in the app to remind the user in a notification)<br>3. Set a daily schedule of your daily plan (which should include 8hrs sleep) (day planner can be incorporated)<br>4. Take out 15 mins to exercise everyday (a reminder can be incorporated)<br>5. Cut down on caffeine intake (to one/day) and nicotine intake<br>6. Morning affirmations (try from the affirmations above)<br>7. Take out 15 mins for meditation (a reminder can be incorporated)<br>8. You can try engaging in your hobbies regularly<br>9. [Doctors near me]",
]


list_of_responses = []

def index(request):
    return render(request, './chatbot/index.html')

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    i = int(request.GET.get('loopVariable'))
    score = int(request.GET.get('score'))
    choice = request.GET.get('choice')
    
    if i == 11:
        return HttpResponse(result(score))

    if choice == 'anxiety':
        list_of_responses = anxiety.copy()

    elif choice == 'stress':
        list_of_responses = stress.copy()
    
    print(score)
    return HttpResponse(list_of_responses[i])

def result(score):
    message = ""
    if score <= 13:
        message = answer[0]
    if score > 13 and score <= 26:
        message = answer[1]
    else:
        message = answer[2]
    return message