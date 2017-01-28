

#calss header
class _GIDDY():
	def __init__(self,): 
		self.name = "GIDDY"
		self.definitions = [u'\u2192\xa0 dizzy ', u'feeling silly, happy, and excited and showing this in your behaviour: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
