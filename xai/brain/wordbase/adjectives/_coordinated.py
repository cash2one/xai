

#calss header
class _COORDINATED():
	def __init__(self,): 
		self.name = "COORDINATED"
		self.definitions = [u'effectively organized so that all the parts work well together: ', u'If a person is coordinated, they move in a very easy and controlled way, especially when playing sports or dancing: ', u'arranged so that the colours, etc. match or look attractive together: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
