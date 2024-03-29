import os
from langchain import PromptTemplate, FewShotPromptTemplate
from langchain import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

os.environ["OPENAI_API_KEY"] =""


demo_template='''I want you to act as a acting financial advisor for people.
In an easy way, explain the basics of {financial_concept}.'''

prompt=PromptTemplate(
    input_variables=['financial_concept'],
    template=demo_template
    )

prompt.format(financial_concept='income tax')


llm=OpenAI(temperature=0.7)
chain1=LLMChain(llm=llm,prompt=prompt)

chain1.run('GDP')

## Language Translation



template='''In an easy way translate the following sentence '{sentence}' into {target_language}'''
language_prompt = PromptTemplate(
    input_variables=["sentence",'target_language'],
    template=template,
)
language_prompt.format(sentence="How are you",target_language='hindi')

chain2=LLMChain(llm=llm,prompt=language_prompt)

chain2({'sentence':"Hello How are you",'target_language':'hindi'})




# First, create the list of few shot examples.
examples = [
    {"word": "happy", "antonym": "sad"},
    {"word": "tall", "antonym": "short"},
]

# Next, we specify the template to format the examples we have provided.
# We use the `PromptTemplate` class for this.
example_formatter_template = """Word: {word}
Antonym: {antonym}
"""

example_prompt = PromptTemplate(
    input_variables=["word", "antonym"],
    template=example_formatter_template,
)


few_shot_prompt = FewShotPromptTemplate(
    # These are the examples we want to insert into the prompt.
    examples=examples,
    # This is how we want to format the examples when we insert them into the prompt.
    example_prompt=example_prompt,
    # The prefix is some text that goes before the examples in the prompt.
    # Usually, this consists of intructions.
    prefix="Give the antonym of every input\n",
    # The suffix is some text that goes after the examples in the prompt.
    # Usually, this is where the user input will go
    suffix="Word: {input}\nAntonym: ",
    # The input variables are the variables that the overall prompt expects.
    input_variables=["input"],
    # The example_separator is the string we will use to join the prefix, examples, and suffix together with.
    example_separator="\n",
)

print(few_shot_prompt.format(input='big'))
chain=LLMChain(llm=llm,prompt=few_shot_prompt)
chain({'input':"big"})