

#calss header
class _INCURIOUS():
	def __init__(self,): 
		self.name = "INCURIOUS"
		self.definitions = [u'not interested in knowing what is happening, or not wanting to discover anything new: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
