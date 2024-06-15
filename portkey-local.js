import OpenAI from 'openai';
import {createHeaders} from 'portkey-ai'

const openai = new OpenAI({
  apiKey: "<api key of open ai >",
  baseURL: "http://localhost:8787/",
  defaultHeaders: createHeaders({
    provider: "openai",
    // apiKey: "<api key of portkey-ai>"
  })
});

async function main() {
  const chatCompletion = await openai.chat.completions.create({
    messages: [{role: "user", content: "What's the significance of 1729?"}],
    model: 'gpt-3.5-turbo',
  });

  console.log(chatCompletion.choices);
}

main();

