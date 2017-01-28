

#calss header
class _RECEIVED():
	def __init__(self,): 
		self.name = "RECEIVED"
		self.definitions = [u'generally accepted as being right or correct because it is based on authority: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
