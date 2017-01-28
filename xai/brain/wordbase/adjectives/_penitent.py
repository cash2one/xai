

#calss header
class _PENITENT():
	def __init__(self,): 
		self.name = "PENITENT"
		self.definitions = [u'showing that you are sorry for something you have done because you feel it was wrong: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
