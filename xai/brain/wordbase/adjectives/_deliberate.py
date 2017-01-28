

#calss header
class _DELIBERATE():
	def __init__(self,): 
		self.name = "DELIBERATE"
		self.definitions = [u'(often of something bad) intentional or planned: ', u'A deliberate movement, action, or thought is done carefully without hurrying: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
