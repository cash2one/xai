

#calss header
class _HANGDOG():
	def __init__(self,): 
		self.name = "HANGDOG"
		self.definitions = [u'(of an expression on a face) unhappy or ashamed, especially because of feeling guilty: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
