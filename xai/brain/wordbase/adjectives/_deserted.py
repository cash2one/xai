

#calss header
class _DESERTED():
	def __init__(self,): 
		self.name = "DESERTED"
		self.definitions = [u'If a place is deserted, there are no people in it: ', u'left alone in a difficult situation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
