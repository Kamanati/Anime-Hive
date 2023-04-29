import requests
from bs4 import BeautifulSoup
from termcolor import colored
import pyfiglet,os

while(1):
   os.system('clear')
   logo_text = "Anime-Scope"
   logo_ascii = pyfiglet.figlet_format(logo_text)
   print(logo_ascii)
   print("simple tool to get anime detials")
   print("")

   # Define the URL of the anime listing page
   url = "https://zoro.to/filter"
   
   # Send a request to the page and get the HTML content
   response = requests.get(url)
   content = response.content
   
   # Parse the HTML content using BeautifulSoup
   soup = BeautifulSoup(content, "html.parser")
   
   # Extract the options for each filter
   options = {}
   filters = ["type", "status", "rated", "score", "season", "language"]
   for filter_name in filters:
       filter_divs = soup.find_all("div", {"class": "cmb-item"})
       for filter_div in filter_divs:
           if filter_name in filter_div.find("div", {"class": "ni-head"}).text.lower():
               filter_options = filter_div.find_all("option")
               options[filter_name] = {}
               for option in filter_options:
                   options[filter_name][option.text.strip()] = option["value"]
   
   # Ask the user to select the filters
   selected_filters = {}
   for filter_name in options.keys():
       print(f"Select a {filter_name}:")
       print("")
       for i, option_name in enumerate(options[filter_name].keys()):
           print(f"{i+1}. {option_name}")
       while True:
           try:
               print("")
               selected_option = input("Select Filter (or press Enter for All): ")
               print("")
               if selected_option == "":
                   break
               selected_option = int(selected_option)
               if selected_option < 1 or selected_option > len(options[filter_name]):
                   raise ValueError
               break
           except ValueError:
               print("Invalid input, please try again.")
       if selected_option != "":
           selected_filters[filter_name] = list(options[filter_name].values())[selected_option-1]
   
   # Build the query string based on the selected filters
   query_string = ""
   for filter_name in selected_filters.keys():
       query_string += f"{filter_name}={selected_filters[filter_name]}&"
   
   # Print the final query string
   print("Selected filters:")
   if query_string == "":
       print("None")
   else:
       print("")
   print("")
   
   # search anime on Zoro.to
   url = f'https://zoro.to/filter?{query_string[:-1]}'
   response = requests.get(url)
   soup = BeautifulSoup(response.content, 'html.parser')
   
   # extract search results
   film_details = soup.find_all('div', class_='film-detail')
   num_results = len(film_details)
   print(f"{num_results} results found for Filter ")
   print("")
   # display search results
   for i, detail in enumerate(film_details):
       name_elem = detail.find('a', class_='dynamic-name')
       name = name_elem['data-jname'] if name_elem else ''
       print(f"{i+1}. {name}")
   
   # get user input to select anime
   selection = int(input("Enter the number of the anime to get details: "))
   selected_detail = film_details[selection-1]
   name_elem_x = selected_detail.find('a', class_='dynamic-name')
   name_x = name_elem_x['data-jname'] if name_elem else ''

   if selection <= 0 or selection > num_results:
       print("Invalid selection")
       sys.exit(0)
   else:
       anime_link = film_details[selection-1].find('a', class_='dynamic-name')['href']
       anime_url = f'https://zoro.to{anime_link}'
       anime_response = requests.get(anime_url)
       anime_soup = BeautifulSoup(anime_response.content, 'html.parser')
   
       # extract anime details
       anime_name = ''
       anime_synonyms = ''
       anime_aired = ''
       anime_premiered = ''
       anime_duration = ''
       anime_status = ''
       anime_score = ''
       anime_over1 = ''
       anime_over = ''
       quality = ''
       subbed = ''
       dubbed = ''
   
       try:
           anime_name = anime_soup.find_all('span', string='Japanese:')[0].find_next_sibling('span').string.strip()
       except:
           anime_name = "Not Availabe"
           pass
           
       try:
           anime_synonyms = anime_soup.find_all('span', string='Synonyms:')[0].find_next_sibling('span').string.strip()
       except:
           anime_synonyms = "Synonyms Not Availabe"
           pass
           
       try:
           anime_aired = anime_soup.find_all('span', string='Aired:')[0].find_next_sibling('span').string.strip()
       except:
           anime_aired= "Not Availabe"
           pass
           
       try:
           anime_premiered = anime_soup.find_all('span', string='Premiered:')[0].find_next_sibling('span').string.strip()
       except:
           anime_premiered = "Not Availabe"
           pass
           
       try:
           anime_duration = anime_soup.find_all('span', string='Duration:')[0].find_next_sibling('span').string.strip()
       except:
           anime_duration = "Not Availabe"
           pass
           
       try:
           anime_status = anime_soup.find('span', string='Status:').find_next_sibling('span').string.strip()
       except:
           anime_status = "Not Availabe"
           pass
           
       try:
           anime_score = anime_soup.find_all('span', string='MAL Score:')[0].find_next_sibling('span').string.strip()
       except:
           anime_score = "Not Availabe"
           pass
           
       try:
           anime_over = anime_soup.find_all('span', string='Overview:')[0].find_next_sibling('div').text.strip()
       except:
           anime_over = "Not Availabe"
           pass
           
       try:
           quality = anime_soup.find('div', class_='tick-quality').text.strip()
       except:
           quality = "Not Availabe"
           pass
           
       try:
           subbed = anime_soup.find('div', class_='tick-sub').text.strip()
       except:
           subbed = "Not Availabe"
           pass
           
       try:
           dubbed = anime_soup.find('div', class_='tick-dub').text.strip()
       except:
           dubbed = "Not Availabe"
           pass
       
       # find the the Genres
       genre_div = anime_soup.find('div', class_='item-list')
       genre_tags = genre_div.find_all('a')
       genres = [tag.text for tag in genre_tags]
       genre_str = ", ".join(genres)
       studio = ', '.join(a.text.strip() for a in anime_soup.select('div:has(> span.item-head:contains("Studios:")) a.name'))
       producers = ', '.join(a.text.strip() for a in anime_soup.select('div:has(> span.item-head:contains("Producers:")) a.name')) 
   
   # display anime details
       print("")
       print("---------------------------------------")
       print(colored("Over View: ", "yellow") + colored(anime_over, "cyan"))
       print("---------------------------------------")
       print("")
       print(colored("\nName: ", "yellow") + colored(anime_name, "cyan"))
       print(colored("Selected Name: ", "yellow") + colored(name_x, "cyan"))
       print(colored("Synonyms: ", "yellow") + colored(anime_synonyms, "cyan"))
       print(colored("Aired: ", "yellow") + colored(anime_aired, "cyan"))
       print(colored("Premiered: ", "yellow") + colored(anime_premiered, "cyan"))
       print(colored("Duration: ", "yellow") + colored(anime_duration, "cyan"))
       print(colored("Status: ", "yellow") + colored(anime_status, "cyan"))
       print(colored("MAL Score: ", "yellow") + colored(anime_score, "cyan"))
       print(colored("Quality: ", "yellow") + colored(quality, "cyan"))
       print(colored("Subbed: ", "yellow") + colored(subbed, "cyan"))
       print(colored("Dubbed: ", "yellow") + colored(dubbed, "cyan"))
       print(colored("Genres: ", "yellow") + colored(genre_str, "cyan"))
       print(colored("Studio: ", "yellow") + colored(studio, "cyan"))
       print(colored("Producers: ", "yellow") + colored(producers, "cyan"))
       print("____________________________________")
       with open('anime_ultra.txt', 'a') as f:
          f.write("``````````````````````````````````````````````````````````")
          f.write("\n")
          f.write("Ultra Filter Search")
          f.write("\n")
          f.write("---------------------------------------\n")
          f.write("Over View: " + anime_over + "\n")
          f.write("---------------------------------------\n\n")
          f.write("Name: " + anime_name + "\n")
          f.write("Selected Name: " + name_x + "\n")
          f.write("Synonyms: " + anime_synonyms + "\n")
          f.write("Aired: " + anime_aired + "\n")
          f.write("Premiered: " + anime_premiered + "\n")
          f.write("Duration: " + anime_duration + "\n")
          f.write("Status: " + anime_status + "\n")
          f.write("MAL Score: " + anime_score + "\n")
          f.write("Quality: " + quality + "\n")
          f.write("Subbed: " + subbed + "\n")
          f.write("Dubbed: " + dubbed + "\n")
          f.write("Genres: " + genre_str + "\n")
          f.write("Studio: " + studio + "\n")
          f.write("Producers: " + producers + "\n")
          f.write("____________________________________\n")

        # code to display the list of titles and their indices
       try:
             seasons_section = anime_soup.find('section', class_='block_area-seasons')
             season_links = seasons_section.find_all('a', class_='os-item')
             num_seasons = len(season_links)
      
      # display seasons
             print(f"\n{num_seasons} seasons found for '{name_x}':")
             with open("anime_history.txt", "a") as f:
                f.write(f"\nUltra Filter's {num_seasons} seasons found for '{anime_synonyms}':\n")
                for i, season_link in enumerate(season_links):
                       season_title = season_link.find('div', class_='title').text.strip()
                       print(f"\033[33m{i+1}\033[0m. \033[96m{season_title}\033[0m")
                       f.write(f"{i+1}. {season_title}\n")
#             for i, season_link in enumerate(season_links):
#                  season_title = season_link.find('div', class_='title').text.strip()
#                  print(f"\033[33m{i+1}\033[0m. \033[96m{season_title}\033[0m")
      
      # get user input to select a season
             selection = int(input("Enter the number of the season to get details: "))
             selected_detail_y = film_details[selection-1]
             name_elem_y = selected_detail_y.find('a', class_='dynamic-name')
             name_y = name_elem_y['data-jname'] if name_elem else ''

             if selection <= 0 or selection > num_seasons:
                  print("Invalid selection")
                  sys.exit(0)
             else:
                  selected_season_link = season_links[selection-1]['href']
                  selected_season_url = f'https://zoro.to{selected_season_link}'
                  selected_season_response = requests.get(selected_season_url)
                  selected_season_soup = BeautifulSoup(selected_season_response.content, 'html.parser')
                  
                  # extract anime details
                  anime_name = ''
                  anime_synonyms = ''
                  anime_aired = ''
                  anime_premiered = ''
                  anime_duration = ''
                  anime_status = ''
                  anime_score = ''
                  anime_over1 = ''
                  anime_over = ''
                  quality = ''
                  subbed = ''
                  dubbed = ''
           
                  try:
                      anime_name = selected_season_soup.find_all('span', string='Japanese:')[0].find_next_sibling('span').string.strip()
                  except:
                      anime_name = "Not Availabe"
                      pass
           
                  try:
                      anime_synonyms = selected_season_soup.find_all('span', string='Synonyms:')[0].find_next_sibling('span').string.strip()
                  except:
                      anime_synonyms = "Synonyms Not Availabe"
                      pass
           
                  try:
                      anime_aired = selected_season_soup.find_all('span', string='Aired:')[0].find_next_sibling('span').string.strip()
                  except:
                      anime_aired= "Not Availabe"
                      pass
           
                  try:
                      anime_premiered = selected_season_soup.find_all('span', string='Premiered:')[0].find_next_sibling('span').string.strip()
                  except:
                      anime_premiered = "Not Availabe"
                      pass
           
                  try:
                      anime_duration = selected_season_soup.find_all('span', string='Duration:')[0].find_next_sibling('span').string.strip()
                  except:
                      anime_duration = "Not Availabe"
                      pass
           
                  try:
                      anime_status = selected_season_soup.find('span', string='Status:').find_next_sibling('span').string.strip()
                  except:
                      anime_status = "Not Availabe"
                      pass
           
                  try:
                      anime_score = selected_season_soup.find_all('span', string='MAL Score:')[0].find_next_sibling('span').string.strip()
                  except:
                      anime_score = "Not Availabe"
                      pass
           
                  try:
                      anime_over = selected_season_soup.find_all('span', string='Overview:')[0].find_next_sibling('div').text.strip()
                  except:
                      anime_over = "Not Availabe"
                      pass
           
                  try:
                      quality = selected_season_soup.find('div', class_='tick-quality').text.strip()
                  except:
                      quality = "Not Availabe"
                      pass
           
                  try:
                      subbed = selected_season_soup.find('div', class_='tick-sub').text.strip()
                  except:
                      subbed = "Not Availabe"
                      pass
           
                  try:
                      dubbed = selected_season_soup.find('div', class_='tick-dub').text.strip()
                  except:
                      dubbed = "Not Availabe"
                      pass
                  
                  # find the the Genres
                  genre_div = selected_season_soup.find('div', class_='item-list')
                  genre_tags = genre_div.find_all('a')
                  genres = [tag.text for tag in genre_tags]
                  genre_str = ", ".join(genres)
                  studio = ', '.join(a.text.strip() for a in selected_season_soup.select('div:has(> span.item-head:contains("Studios:")) a.name'))
                  producers = ', '.join(a.text.strip() for a in selected_season_soup.select('div:has(> span.item-head:contains("Producers:")) a.name'))

                  print("")
                  print("---------------------------------------")
                  print(colored("Over View: ", "yellow") + colored(anime_over, "cyan"))
                  print("---------------------------------------")
                  print("")
                  print(colored("\nName: ", "yellow") + colored(anime_name, "cyan"))   
                  print(colored("Selected Name: ", "yellow") + colored(name_x, "cyan"))
                  print(colored("Synonyms: ", "yellow") + colored(anime_synonyms, "cyan"))  
                  print(colored("Aired: ", "yellow") + colored(anime_aired, "cyan"))
                  print(colored("Premiered: ", "yellow") + colored(anime_premiered, "cyan"))
                  print(colored("Duration: ", "yellow") + colored(anime_duration, "cyan"))
                  print(colored("Status: ", "yellow") + colored(anime_status, "cyan")) 
                  print(colored("MAL Score: ", "yellow") + colored(anime_score, "cyan"))
                  print(colored("Quality: ", "yellow") + colored(quality, "cyan"))
                  print(colored("Subbed: ", "yellow") + colored(subbed, "cyan"))
                  print(colored("Dubbed: ", "yellow") + colored(dubbed, "cyan"))
                  print(colored("Genres: ", "yellow") + colored(genre_str, "cyan"))
                  print(colored("Studio: ", "yellow") + colored(studio, "cyan"))
                  print(colored("Producers: ", "yellow") + colored(producers, "cyan"))
                  print("____________________________________")
                  try:
                       seasons_section = anime_soup.find('section', class_='block_area-seasons')
                       season_links = seasons_section.find_all('a', class_='os-item')
                       num_seasons = len(season_links)

       # display seasons                                                                              
                       print(f"\nRelated seasons found for '{anime_synonyms}':")
                       for i, season_link in enumerate(season_links):
                               season_title = season_link.find('div', class_='title').text.strip()
                               print(f"\033[33m{i+1}\033[0m. \033[96m{season_title}\033[0m")
                       kl=input("Press any key to continue....")
                  except:
                       print("")
                       print("No seasons Found!")
                       print("")
                       kl=input("Press any key to continue....")
       except:
                  print("")
                  print("No seasons Found!")
                  print("")
                  kl=input("Press any key to continue....")
   
