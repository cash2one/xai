

#calss header
class _PARALLEL():
	def __init__(self,): 
		self.name = "PARALLEL"
		self.definitions = [u'If two or more lines, streets, etc. are parallel, the distance between them is the same all along their length: ', u'used to describe an event or situation that happens at the same time as and/or is similar to another one: ', u'sending through several bits (= units) of information at a time using a link with several channels (= wires or connections): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
