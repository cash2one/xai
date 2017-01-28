

#calss header
class _STATEWIDE():
	def __init__(self,): 
		self.name = "STATEWIDE"
		self.definitions = [u'in every part of a state: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
