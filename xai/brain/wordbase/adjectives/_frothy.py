

#calss header
class _FROTHY():
	def __init__(self,): 
		self.name = "FROTHY"
		self.definitions = [u'(of a liquid) with small white bubbles on the surface: ', u'entertaining and easily understood, but not serious or intended to make you think: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
