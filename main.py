import analyzer
import crawler
import utils

def validate_choice(choice):
    if choice == 'n' or choice == 'N':
        print('Quiting the analyzer!')
        exit(0)

def main():
    movie_list = utils.read()

    features = {
        '0': crawler.start_scraper,
        '1': analyzer.get_improved_pops,
        '2': analyzer.get_prev_positions,
        '3': analyzer.get_top_rated_genre
    }
    
    while True:
        msg = '''
0: Enter 0 to fetch latest movies from popular movies list,
1: Enter 1 to veiw movie list that have improved in popularity,
2: Enter 2 to view previous week's positions,
3: Enter 3 to see top rated genre,
n: Enter n/N to exit: '''
        choice = input(msg)
        validate_choice(choice)
        
        func = features.get(choice)
        if func:
            result = func(movie_list=movie_list)
        else:
            print(f"Invalid operation: {choice}")
            result = None
        
        choice = input('Continue? (y/n): ')
        validate_choice(choice)

main()