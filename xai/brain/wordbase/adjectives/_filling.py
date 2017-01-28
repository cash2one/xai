

#calss header
class _FILLING():
	def __init__(self,): 
		self.name = "FILLING"
		self.definitions = [u'If food is filling, you feel full after you have eaten only a little of it.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
