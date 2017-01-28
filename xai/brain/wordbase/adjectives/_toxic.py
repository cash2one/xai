

#calss header
class _TOXIC():
	def __init__(self,): 
		self.name = "TOXIC"
		self.definitions = [u'poisonous: ', u'very unpleasant or unacceptable', u'causing you a lot of harm and unhappiness over a long period of time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
