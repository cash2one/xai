

#calss header
class _SEDUCTIVE():
	def __init__(self,): 
		self.name = "SEDUCTIVE"
		self.definitions = [u'intended to seduce someone: ', u'making you want to do, have, or believe something, because of seeming attractive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
