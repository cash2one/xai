

#calss header
class _UNDERLYING():
	def __init__(self,): 
		self.name = "UNDERLYING"
		self.definitions = [u'real but not immediately obvious: ', u'used to describe something on which something else is based: ', u'positioned under the surface of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
