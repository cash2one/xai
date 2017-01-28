

#calss header
class _VALID():
	def __init__(self,): 
		self.name = "VALID"
		self.definitions = [u'based on truth or reason; able to be accepted: ', u'A ticket or other document is valid if it is based on or used according to a set of official conditions that often include a time limit: ', u'having legal force: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
