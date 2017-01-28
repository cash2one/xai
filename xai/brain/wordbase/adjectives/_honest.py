

#calss header
class _HONEST():
	def __init__(self,): 
		self.name = "HONEST"
		self.definitions = [u'telling the truth or able to be trusted and not likely to steal, cheat, or lie: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
