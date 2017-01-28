

#calss header
class _PETRIFIED():
	def __init__(self,): 
		self.name = "PETRIFIED"
		self.definitions = [u'extremely frightened: ', u'having changed to a substance like stone: ', u'used to describe something that has stopped changing and developing, and often belongs to the past']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
