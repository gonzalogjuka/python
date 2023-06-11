import openai

openai.api_key="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"

while True:
    prompt=input('\nIntroduce una pregunta: ')
    if prompt == "exit":
        break
    completion = openai.Completion.create(engine="text-davinci-003",
                         prompt=prompt,
                         max_tokens=2048)
    print(completion.choices[0].text) # type: ignore