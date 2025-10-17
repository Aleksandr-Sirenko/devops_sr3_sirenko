import sys

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--help":
        print("Usage: python sys_tool.py\nPrints 'командна строка' when run directly.")
        return
    print("командна строка")

if __name__ == "__main__":
    main()