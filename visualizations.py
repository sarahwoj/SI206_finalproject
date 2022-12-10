import matplotlib.pyplot as plt

def create_visualization_1():
    x = ["under 30", "30-70", "70-100", "over 100"]
    h = [6.3, 6.7, 6.5, 6.5]
    plt.bar(x, h)
    plt.xlabel("Movie Budget Group (in millions)")
    plt.ylabel("Average IMDB Movie Rating")
    plt.title("Average Movie Rating for Different Budget Groups")
    plt.show()

def create_visualization_2():
    x = ["6", "60", "55", "23", "25", "41", "47", "61", "75", "70"]
    h = [5.1, 5.7, 8.4, 7.9, 7, 6.2, 6.9, 6, 6.5, 6.4]
    plt.bar(x, h)
    plt.xlabel("Movie ID")
    plt.ylabel("IMDB Rating")
    plt.title("Top 10 Highest Budgeted Movies and Their Ratings")
    plt.show()

def create_visualization_3():
    x = ["92", "7", "66", "95", "28", "5", "93", "49", "10", "64"]
    h = [7, 6.3, 6.2, 6.4, 6.6, 6.9, 7.1, 6, 5.5, 6.9]
    plt.bar(x, h)
    plt.xlabel("Movie ID")
    plt.ylabel("IMDB Rating")
    plt.title("Top 10 Lowest Budgeted Movies and Their Ratings")
    plt.show()

create_visualization_1()
create_visualization_2()
create_visualization_3()





