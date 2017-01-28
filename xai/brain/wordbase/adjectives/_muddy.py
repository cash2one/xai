

#calss header
class _MUDDY():
	def __init__(self,): 
		self.name = "MUDDY"
		self.definitions = [u'covered by or containing mud (= wet, sticky earth): ', u'Muddy colours are dark and not bright: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
