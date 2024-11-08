# https://github.com/openai/openai-python
from openai import OpenAI
import time

api = 'your key'
client = OpenAI(api_key = api)

assistant = client.beta.assistants.create(
      name="Teacher",
      instructions="你现在是信息技术专业伦理专业的老师，负责和你下面的学生进行沟通",
      tools=[{"type": "code_interpreter"}],
      model="gpt-3.5-turbo-1106"
  )

def create_thread():
    thread = client.beta.threads.create()
    return thread.id #str

def add_message_and_running(user_inputs, thread_id):
    message = client.beta.threads.messages.create(
        thread_id = thread_id,
        role = "user",
        content = user_inputs
    )
    
    run = client.beta.threads.runs.create(
    thread_id = thread_id,
    assistant_id = assistant.id,
    # instructions="Please address the user as Jane Doe. The user has a premium account."
    )

    while run.status != 'completed':
        time.sleep(2)
        run = client.beta.threads.runs.retrieve(
        thread_id = thread_id,
        run_id = run.id
        )

        if run.status in ['cancelling', 'cancelled', 'failed', 'expired']:
            print(run.status + f': {run.last_error}')
            error = run.status + f': {run.last_error}'
            return error
        
        elif run.status == 'completed':
            break

        else:
            continue
        

    messages = client.beta.threads.messages.list(
    thread_id=thread_id
    )

    res = messages.data[0].content[0].text.value

    return res