

#calss header
class _INCIDENTAL():
	def __init__(self,): 
		self.name = "INCIDENTAL"
		self.definitions = [u'less important than the thing something is connected with or part of: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
