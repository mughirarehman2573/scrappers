from openai import OpenAI

client = OpenAI(api_key='')
from bs4 import BeautifulSoup


# Set up OpenAI API key


def read_html_file(file_path):
    with open(file_path, 'r') as file:
        html_content = file.read()
    return html_content


def extract_information(html_content):
    # Parse HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract relevant information
    # Replace the example logic with the actual logic to extract the information
    # For example, to extract text within <p> tags:
    paragraphs = soup.find_all('p')
    extracted_text = [p.get_text() for p in paragraphs]

    return extracted_text


def answer_question_with_gpt(question, context):
    response = client.completions.create(model="davinci-002",
                                         prompt=question + "\nContext: " + context + "\nAnswer:",
                                         temperature=0.5,
                                         max_tokens=100)
    answer = response.choices[0].text.strip()
    return answer


if __name__ == "__main__":
    file_path = 'test.html'  # Path to your HTML file
    html_content = read_html_file(file_path)
    extracted_information = extract_information(html_content)

    context = ' '.join(extracted_information)  # Join extracted text into a single string

    question = "What is the main content of the HTML file?"
    answer = answer_question_with_gpt(question, context)
    print(answer)
