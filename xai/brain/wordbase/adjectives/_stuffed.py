

#calss header
class _STUFFED():
	def __init__(self,): 
		self.name = "STUFFED"
		self.definitions = [u'A stuffed animal or bird is filled with special material so that it keeps the shape it had when it was alive: ', u'(of a person) having eaten enough or too much: ', u'filled with a stuffing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
