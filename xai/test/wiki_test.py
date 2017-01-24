#!/usr/bin/evn python
import wikipedia
print wikipedia.summary("cat")
ny = wikipedia.page("cat")
print(ny.title)
print('\n')
print(ny.url)
print('\n')
print(ny.content)
print('\n')
print(ny.links[0])