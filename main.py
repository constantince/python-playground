from langchain.llms import OpenAI
import os
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

os.environ["OPENAI_API_KEY"] = "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"

llm = OpenAI(temperature=0.9)

prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)

# text = prompt.format(product="colorful socks")

chain = LLMChain(llm=llm, prompt=prompt)

result = chain.run("colorful socks")

print(result)