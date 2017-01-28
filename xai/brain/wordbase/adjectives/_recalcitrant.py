

#calss header
class _RECALCITRANT():
	def __init__(self,): 
		self.name = "RECALCITRANT"
		self.definitions = [u'(of a person) unwilling to obey orders or to do what should be done, or (of an animal) refusing to be controlled']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
