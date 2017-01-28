

#calss header
class _FACILE():
	def __init__(self,): 
		self.name = "FACILE"
		self.definitions = [u'A facile remark or theory is too simple and has not been thought about enough: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
