

#calss header
class _ITCHY():
	def __init__(self,): 
		self.name = "ITCHY"
		self.definitions = [u'having or causing an itch: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
