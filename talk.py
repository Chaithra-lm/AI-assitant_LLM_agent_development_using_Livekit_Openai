# talk.py
import asyncio
from livekit.agents import AgentSession
from livekit.plugins import openai
from agent import Assistant

def _print_msg_content(content):
    # content can be str or List[str] depending on provider
    if isinstance(content, (list, tuple)):
        print("\n".join(map(str, content)))
    else:
        print(str(content))

async def main():
    async with openai.LLM(model="gpt-4o-mini") as model, AgentSession(llm=model) as session:
        await session.start(Assistant())
        print("Agent ready. Type messages (Ctrl+C to exit).")

        while True:
            user = input("> ")
            result = await session.run(user_input=user)

            for ev in result.events:
                if ev.type == "message":
                    msg = ev.item  # ChatMessage model
                    if getattr(msg, "role", None) == "assistant":
                        _print_msg_content(msg.content)

                elif ev.type == "function_call":
                    fc = ev.item  # FunctionCall model
                    print(f"[tool call] {fc.name}({fc.arguments})")

                elif ev.type == "function_call_output":
                    out = ev.item  # FunctionCallOutput model
                    # Some providers return .output, others .result; guard both
                    payload = getattr(out, "output", None) or getattr(out, "result", None)
                    print(f"[tool result] {out.name}: {payload}")

            print()  # spacing between turns

if __name__ == "__main__":
    asyncio.run(main())

