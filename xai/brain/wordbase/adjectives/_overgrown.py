

#calss header
class _OVERGROWN():
	def __init__(self,): 
		self.name = "OVERGROWN"
		self.definitions = [u'covered with plants that are growing thickly and in an uncontrolled way: ', u'used to describe something that has grown too large: ', u'used to describe an adult who behaves like a child: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
