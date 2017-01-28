

#calss header
class _SUBMISSIVE():
	def __init__(self,): 
		self.name = "SUBMISSIVE"
		self.definitions = [u'A submissive person allows themselves to be controlled by other people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
