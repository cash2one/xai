

#calss header
class _PLUM():
	def __init__(self,): 
		self.name = "PLUM"
		self.definitions = [u'very good and worth having: ', u'having a dark reddish-purple colour: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
