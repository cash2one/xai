

#calss header
class _ELDERLY():
	def __init__(self,): 
		self.name = "ELDERLY"
		self.definitions = [u'polite word for old: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
