

#calss header
class _INSTRUCTIONAL():
	def __init__(self,): 
		self.name = "INSTRUCTIONAL"
		self.definitions = [u'(of an activity, book, etc.) designed to teach someone how to do something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
