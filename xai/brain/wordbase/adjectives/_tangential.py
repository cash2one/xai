

#calss header
class _TANGENTIAL():
	def __init__(self,): 
		self.name = "TANGENTIAL"
		self.definitions = [u'of or along a tangent', u'(of a subject or activity) different from or not directly connected with the one you are talking about or doing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
