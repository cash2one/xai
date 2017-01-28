

#calss header
class _BACK():
	def __init__(self,): 
		self.name = "BACK"
		self.definitions = [u'at or near the back of something: ', u'paid after the end of a period of time when it should have been paid: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
