

#calss header
class _NEANDERTHAL():
	def __init__(self,): 
		self.name = "NEANDERTHAL"
		self.definitions = [u'(of people or beliefs) very old-fashioned and not willing to change: ', u'(of people) rude or offensive']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
