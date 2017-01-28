

#calss header
class _MIRED():
	def __init__(self,): 
		self.name = "MIRED"
		self.definitions = [u'to be involved in a difficult situation, especially for a long period of time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
