import streamlit.web.cli as stcli
import sys

def main():    
    sys.argv = ["streamlit", "run", "leitor/leitor_app.py"]    
    stcli.main()

if __name__ == "__main__":
    main()