

#calss header
class _SIC():
	def __init__(self,): 
		self.name = "SIC"
		self.definitions = [u'a word written in brackets after a word that you have copied to show that you know it has been spelled or used wrongly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
