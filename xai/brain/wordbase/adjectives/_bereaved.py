

#calss header
class _BEREAVED():
	def __init__(self,): 
		self.name = "BEREAVED"
		self.definitions = [u'having a close relation or friend who has recently died: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
