

#calss header
class _HURRIED():
	def __init__(self,): 
		self.name = "HURRIED"
		self.definitions = [u'done very or too quickly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
