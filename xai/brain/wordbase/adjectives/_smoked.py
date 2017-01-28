

#calss header
class _SMOKED():
	def __init__(self,): 
		self.name = "SMOKED"
		self.definitions = [u'Smoked glass or a smoked window has been made darker, as if by smoke: ', u'preserved using smoke from burning wood: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
