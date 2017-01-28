

#calss header
class _INWARD():
	def __init__(self,): 
		self.name = "INWARD"
		self.definitions = [u'on or towards the inside: ', u'inside your mind and not expressed to other people: ', u'relating to money coming into a country rather than leaving it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
