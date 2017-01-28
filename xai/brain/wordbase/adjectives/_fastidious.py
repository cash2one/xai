

#calss header
class _FASTIDIOUS():
	def __init__(self,): 
		self.name = "FASTIDIOUS"
		self.definitions = [u'giving too much attention to small details and wanting everything to be correct and perfect: ', u'having a strong dislike of anything dirty or unpleasant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
