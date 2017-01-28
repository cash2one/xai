

#calss header
class _CHIVALROUS():
	def __init__(self,): 
		self.name = "CHIVALROUS"
		self.definitions = [u'A chivalrous man is polite, honest, fair, and kind towards women.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
