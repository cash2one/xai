

#calss header
class _ALTRUISTIC():
	def __init__(self,): 
		self.name = "ALTRUISTIC"
		self.definitions = [u'showing a wish to help or bring advantages to others, even if it results in disadvantage for yourself: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
