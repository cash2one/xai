

#calss header
class _RAFFISH():
	def __init__(self,): 
		self.name = "RAFFISH"
		self.definitions = [u'not following usual social standards of behaviour or appearance, especially in a careless and attractive way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
