

#calss header
class _MUM():
	def __init__(self,): 
		self.name = "MUM"
		self.definitions = [u'to say nothing about a subject: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
