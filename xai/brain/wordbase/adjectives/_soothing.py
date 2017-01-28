

#calss header
class _SOOTHING():
	def __init__(self,): 
		self.name = "SOOTHING"
		self.definitions = [u'making you feel calm: ', u'making something less painful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
