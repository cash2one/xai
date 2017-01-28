

#calss header
class _BUREAUCRATIC():
	def __init__(self,): 
		self.name = "BUREAUCRATIC"
		self.definitions = [u'relating to a system of controlling or managing a country, company, or organization that is operated by a large number of officials: ', u'involving complicated rules and processes that make something slow and difficult: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
