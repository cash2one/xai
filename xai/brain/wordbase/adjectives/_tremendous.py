

#calss header
class _TREMENDOUS():
	def __init__(self,): 
		self.name = "TREMENDOUS"
		self.definitions = [u'very great in amount or level, or extremely good: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
