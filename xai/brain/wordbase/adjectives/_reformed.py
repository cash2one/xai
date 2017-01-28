

#calss header
class _REFORMED():
	def __init__(self,): 
		self.name = "REFORMED"
		self.definitions = [u'(especially of a person) changed and improved because of no longer doing something harmful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
