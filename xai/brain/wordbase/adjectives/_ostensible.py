

#calss header
class _OSTENSIBLE():
	def __init__(self,): 
		self.name = "OSTENSIBLE"
		self.definitions = [u'appearing or claiming to be one thing when it is really something else: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
