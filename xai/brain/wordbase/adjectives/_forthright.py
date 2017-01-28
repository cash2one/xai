

#calss header
class _FORTHRIGHT():
	def __init__(self,): 
		self.name = "FORTHRIGHT"
		self.definitions = [u'(too) honest or direct in behaviour: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
