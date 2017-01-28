

#calss header
class _APOLOGETIC():
	def __init__(self,): 
		self.name = "APOLOGETIC"
		self.definitions = [u'showing that you feel sorry about having caused someone problems or unhappiness: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
