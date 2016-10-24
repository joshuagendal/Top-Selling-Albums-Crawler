#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient

client = MongoClient('mongodb://joshuagendal:treetree1@ds063946.mlab.com:63946/gendal_albums')
db = client['gendal_albums']
collection = db['gendal_albums']

r = requests.get('https://simple.wikipedia.org/wiki/List_of_best-selling_albums_worldwide')
soup = BeautifulSoup(r.content, 'html.parser')
cells = soup.find_all('td')
cells = cells[6:]


artist = []
album = []
year = []
genre = []
copies_sold = []
dummy_rank = []
dummy_rank_1 = []
rank = []

for cell in cells[::6]:
    artist.append(cell.get_text())
for cell in cells[1::6]:
    album.append(cell.get_text())
for cell in cells[2::6]:
    year.append(cell.get_text())
for cell in cells[3::6]:
    genre.append(cell.get_text())
for cell in cells[4::6]:
    copies_sold.append(cell.get_text())
for cell in cells[5::6]:
    dummy_rank.append(cell.get_text())
for r in dummy_rank:
    dummy_rank_1.append(r.replace('[', ''))
for r in dummy_rank_1:
    rank.append(r.replace(']', ''))
###must authenticate


counter = 0
while counter < 69:
    post = {
        'artist' : artist[counter],
        'album' : album[counter],
        'year' : year[counter],
        'genre' : genre[counter],
        'copies_sold' : copies_sold[counter],
        'rank' : rank[counter],
    }
    db['gendal_albums'].insert_one(post)
    counter += 1


#
# """
# a = cells[0]
# a
# for cell in cells:
#     print cell.text
# cells_1 = cells[3:]
# cells_1
# for cell in cells_1:
#     print cell.text
# cells_2 = cells_1[2:]
# cells_2
# for cell in cells_2:
#     print cell.text'
# for cell in cells_2:
#     print cell.text
# cells_3 = cells_2[1:]
# cells_3
# for cells in cells_3:
#     print cells.text
# for cells in cells_3:
#     print cells
# for cells in cells_3:
#     print cells.text
# for cells in cells_3:
#     print cells[0]
# a = cells_3[0]
# a
# a = cells_3[0].get_text()
# a
# print a
# type(Cells_3)
# type(cells_3)
# for cell in cells_3:
#     print cell[0]
# for cell in cells_3:
#     print cell.text
# for cell in cells_3[::6]:
#     print cell.text
# for cell in cells_3[1:6]:
#     print cell.text
# for cell in cells_3[1::6]:
#     print cell.text
# for cell in cells_3[::6]:
#     artist = cell.get_text()
# artisr
# artist
# cells_3
# for cell in cells_3[1::6]:
#     print cell.text
# for cell in cells_3[1::6]:
#     album_names = cell
# album_names
# for cell in cells_3[::6]:
#     print cell.text
# for cell in cells_3[::6]:
#     arists = cell.text
# arists
# artists = cells_3[::6].get_text
# artists = cells_3[::6].get_text()
# cells_not_list = soup.find_all('td')
# cells_not_list
# for cell in cells_not_list:
#     print cell.text
# artists = cells_3[::6].text
# artists = cells_3[::6]
# artists
# artists.string
# cells_not_list
# for cell in cells_not_list[5:]:
#     print cell
# for cell in cells_not_list[5:]:
#     print cell.text
# type(cells_not_list)
# for cell in cells_not_list[6::6]:
#     print cell.text
# for cell in cells_not_list[6::6]:
#     artists = cell
# artists
# artists = []
# for cell in cells_not_list[6::6]:
#     artists = cell
# artists
# type(artists)
# for cell in cells_not_list[6::6]:
#     type(cell)
# for cell in cells_not_list[6::6]:
#     print type(cell)
# type(artists)
# for cell in cells_not_list[6::6]:
#     artists = cell.get_text()
# artists
# for cell in cells_not_list[6::6]:
#     artists = cell.text
# artists
# for cell in cells_not_list[6::6]:
#     artists = cell.get_text
# artists
# artists = []
# type(artists)
# for cell in cells_not_list[6::6]:
#     artists.append(cell)
# artists
# for cell in cells_not_list[6::6]:
#     artists.append(cell.get_text())
# artists
# artists = []
# artists
# for cell in cells_not_list[6::6]:
#     artists.append(cell.get_text())
# artists
# for i in artists:
#     print i
# albums = []
# for cell in cells_not_list[7::6]:
#     print cell.text
# len(artists)
# for cell in cells_not_list[7::6]:
#     albums.append(cell.get_text())
# albums
# for album in albums:
#     print album
# %hist
# for cell in cells_not_list[8::6]:
#     print cell.text
# year = []
# for cell in cells_not_list[8::6]:
#     year.append(cell)
# year
# year = []
# for cell in cells_not_list[8::6]:
#     year.append(cell.get_text())
# year
# for yr in year:
#     print yr
# %hist
# history
# """