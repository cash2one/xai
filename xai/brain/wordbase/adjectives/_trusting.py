

#calss header
class _TRUSTING():
	def __init__(self,): 
		self.name = "TRUSTING"
		self.definitions = [u'always believing that other people are good or honest and will not harm or deceive you: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
