from charts import show_graphs
from monitors import execute

options = {
    '1': {
        'method': execute,
        'text': 'Monitor your network',
        'extra_text': 'Only close this console to stop the monitor...'
    },
    '2': {
        'method': show_graphs,
        'text': 'Display data you have gathered',
        'extra_text': 'The data may take a while to display'
    }
}

if __name__ == "__main__":
    print('---- Simple Network Monitor ----')
    print('What do you want to execute?')

    for option in options:
        print(f'    {option} - {options[option]["text"]}')

    decision = input()
    print(options[decision]['extra_text'])
    options[decision]['method']()
