#from scholarly import scholarly, ProxyGenerator

#pg = ProxyGenerator()
#pg.FreeProxies(timeout=5)        # uses a free rotating proxy
#scholarly.use_proxy(pg)

#search_query = scholarly.search_author('Steven A. Cholewiak')

#author = next(search_query, None)

#if author:
#    print(author["name"])
#else:
#    print("Still blocked by Google Scholar")

#print(type(search_query))
#for i in range(3):
#    try:
#        print(next(search_query))
#    except StopIteration:
#        print("No results returned")
#        break


#print(next(scholarly.search_author('Steven A. Cholewiak')))

#search_query = scholarly.search_author('A')
#author = scholarly.fill(search_query)
#print(author)