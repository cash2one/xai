

#calss header
class _AWAKE():
	def __init__(self,): 
		self.name = "AWAKE"
		self.definitions = [u'not sleeping: ', u'If you are awake to something, you know about it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
