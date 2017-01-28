

#calss header
class _POISONOUS():
	def __init__(self,): 
		self.name = "POISONOUS"
		self.definitions = [u'very harmful and able to cause illness or death: ', u'A poisonous animal or insect uses poison in order to defend itself: ', u'very unpleasant and unkind: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
