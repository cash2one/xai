

#calss header
class _CRIMSON():
	def __init__(self,): 
		self.name = "CRIMSON"
		self.definitions = [u'having a dark, deep red colour', u'If you go/turn crimson, your face becomes red because you are very embarrassed or angry: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
