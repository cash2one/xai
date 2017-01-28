

#calss header
class _UNCOORDINATED():
	def __init__(self,): 
		self.name = "UNCOORDINATED"
		self.definitions = [u'with different parts failing to work or move well together: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
