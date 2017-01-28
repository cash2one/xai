

#calss header
class _UNDERSTANDING():
	def __init__(self,): 
		self.name = "UNDERSTANDING"
		self.definitions = [u'An understanding person who has the ability to know how other people are feeling, and can forgive them if they do something wrong: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
