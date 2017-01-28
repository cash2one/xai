

#calss header
class _GENUINE():
	def __init__(self,): 
		self.name = "GENUINE"
		self.definitions = [u'If something is genuine, it is real and exactly what it appears to be: ', u'If people or emotions are genuine, they are honest and sincere: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
