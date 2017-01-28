

#calss header
class _DEADLOCKED():
	def __init__(self,): 
		self.name = "DEADLOCKED"
		self.definitions = [u'If a situation is deadlocked, agreement in an argument cannot be reached because neither side will change its demands or accept any of the demands of the other side: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
