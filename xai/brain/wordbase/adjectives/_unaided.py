

#calss header
class _UNAIDED():
	def __init__(self,): 
		self.name = "UNAIDED"
		self.definitions = [u'without any help from anyone else; independently: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
