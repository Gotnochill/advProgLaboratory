# Function that returns sum, average, max, and min of a list
def list_stats(lst):
    return sum(lst), sum(lst)/len(lst), max(lst), min(lst)

lst = [5, 10, 15, 20, 25]
sum_, avg, max_, min_ = list_stats(lst)
print(f"Sum: {sum_}, Average: {avg}, Max: {max_}, Min: {min_}")
