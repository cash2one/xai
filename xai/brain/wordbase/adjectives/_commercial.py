

#calss header
class _COMMERCIAL():
	def __init__(self,): 
		self.name = "COMMERCIAL"
		self.definitions = [u'related to buying and selling things: ', u'used to describe a record, film, book, etc. that has been produced with the aim of making money and as a result has little artistic value', u'A commercial product can be bought by or is intended to be bought by the general public.', u'used to refer to radio or television paid for by advertisements that are broadcast between and during programmes']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
