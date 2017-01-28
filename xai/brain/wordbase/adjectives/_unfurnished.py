

#calss header
class _UNFURNISHED():
	def __init__(self,): 
		self.name = "UNFURNISHED"
		self.definitions = [u'An unfurnished room, house, or other building has no furniture in it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
