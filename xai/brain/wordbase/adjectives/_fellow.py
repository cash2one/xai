

#calss header
class _FELLOW():
	def __init__(self,): 
		self.name = "FELLOW"
		self.definitions = [u'used to refer to someone who has the same job or interests as you, or is in the same situation as you: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
