

#calss header
class _JITTERY():
	def __init__(self,): 
		self.name = "JITTERY"
		self.definitions = [u'nervous: ', u'shaking and slightly uncontrolled: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
