

#calss header
class _UP():
	def __init__(self,): 
		self.name = "UP"
		self.definitions = [u'moving up: ', u'When a system, computer, or similar machine is up, it is operating, especially in its usual way: ', u'feeling happy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
