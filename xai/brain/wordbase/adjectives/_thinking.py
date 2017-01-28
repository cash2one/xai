

#calss header
class _THINKING():
	def __init__(self,): 
		self.name = "THINKING"
		self.definitions = [u'Thinking people use their minds to consider things carefully: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
