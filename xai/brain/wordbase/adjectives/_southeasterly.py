

#calss header
class _SOUTHEASTERLY():
	def __init__(self,): 
		self.name = "SOUTHEASTERLY"
		self.definitions = [u'towards the southeast: ', u'a wind that comes from the southeast']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
