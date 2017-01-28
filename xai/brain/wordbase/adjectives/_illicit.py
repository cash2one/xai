

#calss header
class _ILLICIT():
	def __init__(self,): 
		self.name = "ILLICIT"
		self.definitions = [u'illegal or disapproved of by society: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
