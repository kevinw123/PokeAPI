import requests, six
import lxml.html as lh
import json

url='http://pokemondb.net/pokedex/all'


def str_bracket(word):
    '''Add brackets around second term'''
    list = [x for x in word]
    for char_ind in range(1, len(list)):
        if list[char_ind].isupper():
            list[char_ind] = ' ' + list[char_ind]
    fin_list = ''.join(list).split(' ')
    length = len(fin_list)
    if length > 1:
        fin_list.insert(1, '(')
        fin_list.append(')')
    return ' '.join(fin_list)


def str_break(word):
    '''Break strings at upper case'''
    list = [x for x in word]
    for char_ind in range(1, len(list)):
        if list[char_ind].isupper():
            list[char_ind] = ' ' + list[char_ind]
    fin_list = ''.join(list).split(' ')
    return fin_list

def main():
    #Create a handle, page, to handle the contents of the website
    page = requests.get(url)

    #Store the contents of the website under doc
    doc = lh.fromstring(page.content)

    #Parse data that are stored between <tr>..</tr> of the site's HTML code
    tr_elements = doc.xpath('//tr')

    #Check the length of the first 12 rows
    [len(T) for T in tr_elements[:12]]

    tr_elements = doc.xpath('//tr')

    #Store header strings
    headers=[]
    i=0

    data = []
    #First row is the header
    for t in tr_elements[0]:
        i+=1
        name=t.text_content()
        headers.append((name))

    # Since our first row is the header, data is stored on the second row onwards
    for j in range(1, len(tr_elements)):
        # T is our j'th row
        T = tr_elements[j]

        # If row is not of size 10, the //tr data is not from our table
        if len(T) != 10:
            break

        # i is the index of our column
        i = 0
        pokemonData = []
        # Iterate through each element of the row
        for t in T.iterchildren():
            rowElement = t.text_content().strip()
            # Check if row is empty
            if i > 0:
                # Convert any numerical value to integers
                try:
                    rowElement = int(rowElement)
                except:
                    pass

            pokemonData.append(rowElement)
            # Increment i for the next column
            i += 1

        jsonObj = {}
        for x  in  range(0, len(pokemonData)):
            if headers[x] == "Name":
                jsonObj[headers[x]] = str_bracket(pokemonData[x])
            elif headers[x] == "Type":
                jsonObj[headers[x]] = str_break(pokemonData[x])
            else:
                jsonObj[headers[x]] = pokemonData[x]
                
        data.append(jsonObj)

    with open('PokemonData.json', 'w') as outfile:
        json.dump(data, outfile)

if __name__ == "__main__":
    main()