

#calss header
class _SUP():
	def __init__(self,): 
		self.name = "SUP"
		self.definitions = [u'written abbreviation for supine (= lying face up)']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
