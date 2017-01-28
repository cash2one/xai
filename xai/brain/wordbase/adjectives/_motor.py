

#calss header
class _MOTOR():
	def __init__(self,): 
		self.name = "MOTOR"
		self.definitions = [u'connected with cars or other vehicles that have engines and use roads: ', u'relating to muscles that produce movement, or the nerves and parts of the brain that control these muscles: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
