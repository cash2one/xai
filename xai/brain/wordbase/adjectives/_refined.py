

#calss header
class _REFINED():
	def __init__(self,): 
		self.name = "REFINED"
		self.definitions = [u'A refined substance has been made pure by removing other substances from it: ', u'improved because of many small changes that have been made: ', u'very polite and showing knowledge of social rules']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
