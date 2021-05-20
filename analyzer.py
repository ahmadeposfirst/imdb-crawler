
def get_improved_pops(movie_list):
    improved_movies = []
    for movie in movie_list:
        if movie['popularity'][0] == '+':
            improved_movies.append({movie['name']: movie['popularity'][1:]})
            print(f"{movie['name']} improved position by {movie['popularity'][1:]}")
    return improved_movies

def get_prev_positions(movie_list):
    prev_ranks = []
    for movie in movie_list:
        pop_trend = movie['popularity'][0]
        pop = int(movie['popularity'][1:])
        pos = int(movie['position'])
        ops = {
            '+': [abs(pop - pos), "upgraded"],
            '-': [pop + pos, "downgraded"]
        }
        prev_ranks.append({movie['name']: ops[pop_trend][1]})
        print(f"{movie['name']} {ops[pop_trend][1]} from {ops[pop_trend][0]} to {pos} in popularity")
    return prev_ranks

def get_top_rated_genre(movie_list):
    gen_chart = {}
    for movie in movie_list:
        for gen in movie['genre']:
            if gen not in gen_chart:
                gen_chart[gen] = [int(movie['position'])]
            else:
                gen_chart[gen].append(int(movie['position']))

    gen_chart = [(gen, sum(count)//len(count)) for gen, count in gen_chart.items()]
    top_rated = sorted(gen_chart, key=lambda tup: tup[1], reverse=True)[0]
    print(f"{top_rated[0]} is most popular genre and has a score of {top_rated[1]}")
    return top_rated

