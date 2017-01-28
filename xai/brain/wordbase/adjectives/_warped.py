

#calss header
class _WARPED():
	def __init__(self,): 
		self.name = "WARPED"
		self.definitions = [u'strange and unpleasant: ', u'bent because of damage by heat or water: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
