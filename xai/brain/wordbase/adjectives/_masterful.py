

#calss header
class _MASTERFUL():
	def __init__(self,): 
		self.name = "MASTERFUL"
		self.definitions = [u'able to control people and situations in a confident way: ', u'If an action is masterful, it is very skilful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
