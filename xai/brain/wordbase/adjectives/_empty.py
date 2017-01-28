

#calss header
class _EMPTY():
	def __init__(self,): 
		self.name = "EMPTY"
		self.definitions = [u'not containing any things or people: ', u'not sincere or without any real meaning: ', u'without purpose or interest: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
