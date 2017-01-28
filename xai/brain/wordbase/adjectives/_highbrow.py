

#calss header
class _HIGHBROW():
	def __init__(self,): 
		self.name = "HIGHBROW"
		self.definitions = [u'(of books, plays, etc.) involving serious and complicated or artistic ideas, or (of people) interested in serious and complicated subjects']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
