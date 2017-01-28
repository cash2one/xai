

#calss header
class _FORMIDABLE():
	def __init__(self,): 
		self.name = "FORMIDABLE"
		self.definitions = [u'causing you to have fear or respect for something or someone because that thing or person is large, powerful, or difficult: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
