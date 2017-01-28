

#calss header
class _CHEERING():
	def __init__(self,): 
		self.name = "CHEERING"
		self.definitions = [u'used to describe something that encourages you and makes you feel happier: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
