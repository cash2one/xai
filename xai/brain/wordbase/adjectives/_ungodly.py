

#calss header
class _UNGODLY():
	def __init__(self,): 
		self.name = "UNGODLY"
		self.definitions = [u'extreme or unacceptable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
