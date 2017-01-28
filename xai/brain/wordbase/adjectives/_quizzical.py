

#calss header
class _QUIZZICAL():
	def __init__(self,): 
		self.name = "QUIZZICAL"
		self.definitions = [u'seeming to ask a question without saying anything: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
