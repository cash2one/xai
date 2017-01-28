

#calss header
class _COMATOSE():
	def __init__(self,): 
		self.name = "COMATOSE"
		self.definitions = [u'in a coma', u'very tired or in a deep sleep because of extreme tiredness, hard work, or too much alcohol: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
