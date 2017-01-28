

#calss header
class _WEARISOME():
	def __init__(self,): 
		self.name = "WEARISOME"
		self.definitions = [u'causing a person to be tired and/or bored: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
