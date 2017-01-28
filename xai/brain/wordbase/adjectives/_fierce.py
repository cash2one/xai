

#calss header
class _FIERCE():
	def __init__(self,): 
		self.name = "FIERCE"
		self.definitions = [u'physically violent and frightening: ', u'strong and powerful: ', u'showing strong feeling or energetic activity: ', u'difficult: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
