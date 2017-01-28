

#calss header
class _IMPETUOUS():
	def __init__(self,): 
		self.name = "IMPETUOUS"
		self.definitions = [u'likely to do something suddenly, without considering the results of your actions: ', u'said or done suddenly, without considering the likely results: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
