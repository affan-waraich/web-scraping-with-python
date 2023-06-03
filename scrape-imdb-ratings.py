from bs4 import BeautifulSoup
import requests, openpyxl

excel = openpyxl.Workbook()
print(excel.sheetnames)
sheet = excel.active  #holding the sheeting we want to work on
sheet.title = 'Top Rated Movies'  #changing excel sheet title to 'Top Rated Movies'
sheet.append(['Movie Rank', 'Movie Name', 'Year of Release', 'Rating', 'cgc'])  #Creating four desired columns 

try:
    source = requests.get("https://www.imdb.com/chart/top/")
    source.raise_for_status()

    #fetching all the html content of the desired webpage through beautiful soup
    soup = BeautifulSoup(source.text, 'html.parser')

    #selecting all the rows of the IMDBrating table and storing in 'movies' variable 
    movies = soup.find('tbody', class_="lister-list").find_all('tr')  
    
    #iterating through each row in html table
    for movie in movies:

        #selecting the table data tag of class(titleColumn) and then storing its text in variable
        name = movie.find('td', class_= "titleColumn").a.text

        #selecting the table data tag of class(titleColumn), then converting its text into list and then storing the 0th index value(rank) of list in variable
        rank = movie.find('td', class_= "titleColumn").get_text(strip=True).split('.')[0]

        #selecting the table data tag of class(titleColumn), then stripping parentheses from its text and storing it in variable
        year = movie.find('td', class_= "titleColumn").span.text.strip('()')

        #selecting the table data tag of class(ratingColumn) and then storing its text in variable
        rating = movie.find('td', class_= "ratingColumn imdbRating").strong.text

        print(f'{rank}  {name}  {year}  {rating}')
        sheet.append([rank, name, year, rating])

except Exception as e:
    print(e) 

excel.save('IMDB Movie Ratings.xlsx')