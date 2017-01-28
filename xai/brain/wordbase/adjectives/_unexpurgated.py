

#calss header
class _UNEXPURGATED():
	def __init__(self,): 
		self.name = "UNEXPURGATED"
		self.definitions = [u'An unexpurgated book, article, film, etc. is complete and contains everything, including parts considered likely to cause offence.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
