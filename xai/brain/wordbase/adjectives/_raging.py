

#calss header
class _RAGING():
	def __init__(self,): 
		self.name = "RAGING"
		self.definitions = [u'very severe or extreme: ', u'very strong or violent: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
