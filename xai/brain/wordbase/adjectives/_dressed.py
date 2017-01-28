

#calss header
class _DRESSED():
	def __init__(self,): 
		self.name = "DRESSED"
		self.definitions = [u'wearing clothes and not naked: ', u'wearing clothing of a particular type: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
