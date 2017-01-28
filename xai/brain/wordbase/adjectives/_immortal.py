

#calss header
class _IMMORTAL():
	def __init__(self,): 
		self.name = "IMMORTAL"
		self.definitions = [u'living or lasting for ever: ', u'very special and famous and therefore likely to be remembered for a long time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
