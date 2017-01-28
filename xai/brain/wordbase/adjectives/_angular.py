

#calss header
class _ANGULAR():
	def __init__(self,): 
		self.name = "ANGULAR"
		self.definitions = [u'having or relating to one or more angles', u'having a clear shape with sharp points: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
