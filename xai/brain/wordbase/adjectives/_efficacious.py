

#calss header
class _EFFICACIOUS():
	def __init__(self,): 
		self.name = "EFFICACIOUS"
		self.definitions = [u'able to produce the intended result']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
