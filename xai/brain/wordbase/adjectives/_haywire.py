

#calss header
class _HAYWIRE():
	def __init__(self,): 
		self.name = "HAYWIRE"
		self.definitions = [u'to stop working, often in a way that is very sudden and noticeable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
