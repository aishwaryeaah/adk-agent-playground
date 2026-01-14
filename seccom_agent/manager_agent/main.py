from dotenv import load_dotenv
load_dotenv()

from manager_agent.agent import root_agent

def main():
    print("Starting Security Manager...")

    # Test the agent with a simple message
    response = root_agent.run("hello, test the security manager agent")
    print("Agent Response:", response)

if __name__ == "__main__":
    main()
