

#calss header
class _IMPRACTICABLE():
	def __init__(self,): 
		self.name = "IMPRACTICABLE"
		self.definitions = [u'If a course of action, plan, etc. is impracticable, it is impossible to do in an effective way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
