

#calss header
class _UNFETTERED():
	def __init__(self,): 
		self.name = "UNFETTERED"
		self.definitions = [u'not limited by rules or any other controlling influence: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
